# Domaine de Lanzac, opgesplitst voor de GHL-builder

De pagina is in drie custom-code blokken geknipt, met ruimte voor de twee
natieve GHL-formulieren ertussen.

```
BLOK A   blok-a-boven.html    nav, hero, alles t/m de kop "Vraag de brochure aan"
                              en het kadertje "wat er daarna gebeurt"
FORM 1   natief GHL-formulier "Brochure Domaine de Lanzac"
BLOK B   blok-b-tussen.html   kop "Meld u aan voor 7 november" en het kadertje
FORM 2   natief GHL-formulier "Aanmelding 7 november, Postillion Breda"
BLOK C   blok-c-footer.html   telefoonregel en footer
```

## Plaatsen
1. Sectie -> element Custom Code -> plak blok A. Rij op volle breedte, padding 0.
2. Nieuwe sectie -> Formulier -> brochureformulier.
3. Nieuwe sectie -> Custom Code -> blok B.
4. Nieuwe sectie -> Formulier -> aanmeldformulier.
5. Nieuwe sectie -> Custom Code -> blok C.

## Formulieren
| Formulier | Velden | Tag | Pipeline |
|---|---|---|---|
| Brochure | voornaam, e-mail, telefoon | ddl-lanzac-brochure | Frankrijk > Brochure aangevraagd |
| Aanmelding | voornaam, achternaam, e-mail, telefoon, aantal personen (geen sessiekeuze) | ddl-lanzac-7nov | Frankrijk > Informatiedag 7 nov |

## Let op
- Alle drie de blokken zijn volledig ASCII. GHL verhaspelt niet-ASCII tekens,
  dus de euro, de punt-scheiding en de vinkjes komen uit CSS (.eu, .dot, .ico).
  Niets in deze bestanden met de hand vervangen door een echt euroteken.
- Elk blok bevat de volledige stijl, zodat de volgorde in de builder niet uitmaakt.
- Alle beelden komen uit GHL Media Storage, dus er is geen externe afhankelijkheid.
- De knoppen verwijzen naar #aanvragen, dat in blok A zelf staat.
