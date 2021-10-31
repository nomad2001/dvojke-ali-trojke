# Igra pod košem ali metanje trojk?

Analiziral bom vse tekme lige NBA iz sezone 2020/2021 na strani
[ESPN](https://www.espn.com/nba/scoreboard).

Podatki, ki jih bom analiziral, se nahajajo v mapi statistika-v-csv. V vsaki CSV datoteki se
nahajajo naslednji podatki:
* V datoteki ekipe.csv sta za vsako ekipo v svoji vrstici navedena unikaten id ekipe in unikatna okrajšava imena ekipe. Ekipi z identifikacijskimi številkami 31 in 32 sta ekipi zvezdnikov, ki sta nastopili le na All-Star tekmi, in ne bosta vključeni v analizo.
* V datoteki tekme_redne.csv so podatki za vsako posamezno tekmo iz rednega dela sezone navedeni v dveh vrsticah. Obe vrstici se začneta z unikatno identifikacijsko številko tekme. V prvi vrstici sta za tem navedena unikaten id gostujoče ekipe ter njena statistika. V drugi vrstici sta za identifikacijsko številko tekme navedena unikaten id domače ekipe in njena statistika. Okrajšave v statistiki imajo naslednje pomene:
    * FG - število uspešnih in vseh metov iz igre (za dve in za tri točke skupaj, brez prostih metov)
    * 3PT - število uspešnih in vseh metov za tri točke
    * FT - število uspešnih in vseh prostih metov
    * OREB - skoki v napadu
    * DREB - skoki v obrambi
    * REB - vsi skoki (v napadu in obrambi skupaj)
    * AST - asistence
    * STL - ukradene žoge
    * BLK - blokirani meti na koš
    * TO - izgubljene žoge
    * PF - osebne napake
    * PTS - končno število točk
* V datoteki tekme_playoff.csv podatki navedeni na enak način kot v tekme_redne.csv, le da vsebujejo statistiko za tekme iz končnice.

Delovne hipoteze:
* Katere ekipe so imele uspešnejšo sezono - tiste, ki so pretežno metale za dve točki ali za tri točke?
* Ali so bile v medsebojnih tekmah uspešnejše ekipe, ki so več metale za dve točki ali za tri točke?
* Ali obstaja povezava med dominantnim načinom igre (igra pod košem ali igra z meti za tri točke) in ostalimi pomembnimi statističnimi podatki?