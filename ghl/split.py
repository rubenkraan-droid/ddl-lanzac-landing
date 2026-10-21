#!/usr/bin/env python3
"""Splitst een landingspagina in drie zelfstandige blokken voor de GHL-builder.

De twee native GHL-formulieren komen tussen de blokken te staan, dus wordt er
geknipt op de twee <div class="placeholder"> blokken in de slot-CTA. Elk blok
krijgt zijn eigen <link> naar de fonts en zijn eigen <style>, omdat het
Custom CSS-veld van GHL lange stylesheets afkapt.

Gebruik:  python3 ghl/split.py index.html ghl/blok     -> ghl/blok-{a,b,c}-compleet.html
          python3 ghl/split.py genot.html ghl/genot-blok
"""
import re, sys

FONT = ('<link href="https://fonts.googleapis.com/css2?'
        'family=Instrument+Sans:wght@500;600;700&'
        'family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n')

# GHL verminkt losse tekens, dus staan de symbolen als CSS-escape in de stijl.
EXTRA = '''
  .eu::before{content:"\\20AC"}
  .dot::before{content:"\\00B7"}
  .ico.ok::before{content:"\\2713"}
  .ico.no::before{content:"\\2715"}
  .vw-lijst li::before,.fac li::before{content:"\\2713"}
  img,svg,video,iframe,table{max-width:100%}
  *,*::before,*::after{box-sizing:border-box}
  .cta-vlak{background:#1B2A14;color:#fff}
  .cta-vlak > .container > h2{color:#fff}'''

SLUIT = '\n      </div>\n    </div>\n  </div>\n</section>\n'
WRAP  = '<section class="section cta-final cta-vlak"><div class="container"><div class="forms">\n'


def ascii_safe(t):
    """GHL verminkt alles buiten ASCII. Symbolen gaan daarom als leeg span mee,
    met het teken in de stijl (zie EXTRA)."""
    t = t.replace('<span class="ico">\u2713</span>', '<span class="ico ok"></span>')
    t = t.replace('<span class="ico">\u2715</span>', '<span class="ico no"></span>')
    t = t.replace('&euro;', '<span class="eu"></span>')
    t = t.replace('\u20ac', '<span class="eu"></span>')
    t = t.replace('\u00b7', '<span class="dot"></span>')
    t = t.replace('\u2713', '').replace('\u2715', '')
    # entiteiten die GHL in de editor terugvertaalt naar een los teken
    t = t.replace('&#39;', "'")
    t = t.replace('&copy;', 'Copyright ')
    return t


def split(bron, voorvoegsel):
    s = open(bron, encoding='utf-8').read()
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    css = css.replace('content:"\u2713"', 'content:""') + EXTRA
    body = ascii_safe(s[s.find('<body>') + 6: s.find('</body>')])

    # knippunten: begin van elke placeholder, en het einde van zijn comment
    i1 = body.find('<div class="placeholder">')
    j1 = body.find('</div>', body.find('-->', i1)) + 6
    i2 = body.find('<div class="placeholder">', j1)
    j2 = body.find('</div>', body.find('-->', i2)) + 6
    if min(i1, j1, i2, j2) < 0:
        raise SystemExit('Twee placeholders verwacht, niet gevonden in ' + bron)

    # het losse </div> aan het begin sluit de formulierkaart van het vorige blok;
    # laat je het staan, dan krijg je een leeg wit kaartje bovenaan
    schoon = lambda t: re.sub(r'^\s*</div>\s*', '\n', t, count=1)

    blokken = [('a', body[:i1] + SLUIT),
               ('b', WRAP + schoon(body[j1:i2]) + SLUIT),
               ('c', WRAP + schoon(body[j2:]))]

    uit = []
    for letter, inhoud in blokken:
        doc = FONT + '<style>\n' + css + '\n</style>\n' + inhoud
        if not doc.isascii():
            raak = [r for r in doc.splitlines() if not r.isascii()][:3]
            raise SystemExit('Blok %s is niet ASCII: %s' % (letter, raak))
        for tag in ('div', 'section', 'figure', 'span', 'a', 'p', 'ul', 'li', 'article'):
            o = len(re.findall(r'<%s[ >]' % tag, doc))
            c = len(re.findall(r'</%s>' % tag, doc))
            if o != c:
                raise SystemExit('Blok %s: <%s> %d open, %d dicht' % (letter, tag, o, c))
        pad = '%s-%s-compleet.html' % (voorvoegsel, letter)
        open(pad, 'w', encoding='utf-8').write(doc)
        uit.append((pad, len(doc)))
    return uit


if __name__ == '__main__':
    bron = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
    voor = sys.argv[2] if len(sys.argv) > 2 else 'ghl/blok'
    for pad, n in split(bron, voor):
        print('%-40s %7d tekens' % (pad, n))
