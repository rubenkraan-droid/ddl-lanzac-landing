# Domaine de Lanzac in de GHL-builder

Twee manieren. De tweede is schoner en wordt aangeraden.

## Aanbevolen: stijl in de header, drie kleine blokken

1. **Stijl eenmalig plaatsen.** Funnel of website -> Settings -> Custom CSS.
   Plak de inhoud van `header-css.css`. Dat geldt dan voor alle stappen.
   Werkt je versie met "Tracking Code" in plaats van Custom CSS? Gebruik dan
   `header-css.html` in het Head-veld; daar zitten de `<style>`-tags al omheen.
2. Daarna per sectie een Custom Code-element met:

```
BLOK A   blok-a-markup.html   30.109 tekens
FORM 1   natief GHL-formulier "Brochure Domaine de Lanzac"
BLOK B   blok-b-markup.html      635 tekens
FORM 2   natief GHL-formulier "Aanmelding 7 november, Postillion Breda"
BLOK C   blok-c-markup.html    2.990 tekens
```

## Alternatief: alles in de blokken

`blok-a-boven.html`, `blok-b-tussen.html` en `blok-c-footer.html` bevatten
elk de volledige stijl. Handig als je niet bij de Custom CSS kunt, maar de
stijl staat dan drie keer op de pagina.

## Formulieren
| Formulier | Velden | Tag | Pipeline |
|---|---|---|---|
| Brochure | voornaam, e-mail, telefoon | ddl-lanzac-brochure | Frankrijk > Brochure aangevraagd |
| Aanmelding | voornaam, achternaam, e-mail, telefoon, aantal personen (geen sessiekeuze) | ddl-lanzac-7nov | Frankrijk > Informatiedag 7 nov |

## Let op
- Alles is volledig ASCII. GHL verhaspelt accenten, dus de euro, de
  scheidingspunt en de vinkjes komen uit CSS (.eu, .dot, .ico). Vervang die
  niet met de hand door echte tekens.
- De CSS laat de secties uit de GHL-kolom breken naar 100vw, met
  overflow-x:hidden om een horizontale balk te voorkomen. Je hoeft aan de
  breedte-instelling niets te doen.
- Zet de sectie- en rijpadding in de builder wel op 0, anders houd je een
  witte rand boven en onder elk blok. Let op: GHL heeft aparte padding voor
  mobiel.
- De lettertypen worden door de CSS zelf geladen via een @import.
- Alle beelden komen uit Media Storage, dus geen externe afhankelijkheid.
