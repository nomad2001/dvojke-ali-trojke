# Igra pod košem ali metanje trojk?

Za projektno nalogo pri predmetu Programiranje 1 sem preučil, kakšen vpliv ima metanje za tri točke
v NBA ligi.

## O podatkih

Podatki, ki sem jih analiziral, se nahajajo v mapi *statistika-v-csv*. V njej se v vsaki CSV datoteki nahajajo naslednji podatki:
* V datoteki *ekipe.csv* sta za vsako ekipo v svoji vrstici navedena unikaten id ekipe in unikatna okrajšava imena ekipe. Ekipi z identifikacijskimi številkami 31 in 32 sta ekipi zvezdnikov, ki sta nastopili le na All-Star tekmi, in ne bosta vključeni v analizo.
* V datoteki *tekme_redne.csv* so podatki za vsako posamezno tekmo iz rednega dela sezone navedeni v dveh vrsticah. Obe vrstici se začneta z unikatno identifikacijsko številko tekme. V prvi vrstici sta za tem navedena id gostujoče ekipe ter njena statistika. V drugi vrstici sta za identifikacijsko številko tekme navedena id domače ekipe in njena statistika. Okrajšave v statistiki imajo naslednje pomene:
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

## O analizi

Analiza se nahaja v datoteki *analiza.ipynb*.

Analiziral sem vse tekme lige NBA iz rednega dela sezone 2020/2021 na strani
[ESPN](https://www.espn.com/nba/scoreboard).

Na podlagi podatkov presnetih s te spletne strani, sem izračunal še nekatere druge podatke,
s pomočjo katerih sem analiziral tekme.

Osrednja vprašanja, na katera sem odgovorjal so bila:

* Katere ekipe so imele uspešnejši redni del sezone - tiste, ki so pretežno metale za dve točki ali za tri točke? Kako je vplivala uspešnost meta za tri točke?
* Ali so bile v medsebojnih tekmah uspešnejše ekipe, ki so več metale za dve točki ali za tri točke? Kako je vplivala uspešnost meta za tri točke?
* Ali obstaja povezava med dominantnim načinom igre na posamezni tekmi (igra pod košem ali igra z meti za tri točke) in končnim številom točk na tej tekmi?

V okviru zadnjega vprašanja, pa sem še spisal program, ki poskuša