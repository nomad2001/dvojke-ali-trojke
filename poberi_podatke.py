import orodja
import re

url = "https://www.espn.com/nba/boxscore/_/gameId/"
url_wrong = "https://www.espn.com/nba/scoreboard"
html_tekme_redne = "tekme_redne.html"
html_tekme_redne1 = "tekme_redne1.html"
html_tekme_redne2 = "tekme_redne2.html"
html_tekme_redne3 = "tekme_redne3.html"
html_tekme_playoff = "tekme_playoff.html"
csv_tekme_redni_del = "tekme_redne.csv"
csv_tekme_playoff = "tekme_playoff.csv"
csv_ekipe = "ekipe.csv"
id_prve_redne_tekme = 401266805
id_zadnje_redne_tekme = 401307891
id_prve_playoff_tekme = 401327715
id_zadnje_playoff_tekme = 401344140
#shrani_tekme_v_html(id_prve_redne_tekme,id_zadnje_redne_tekme,html_tekme_redne,True)
def shrani_tekme_v_html(zacetni_id, koncni_id, ime_datoteke, vsili_prenos = False):
    for i in range(zacetni_id, koncni_id + 1):
        orodja.shrani_spletno_stran(url + str(i), ime_datoteke, vsili_prenos)
    print(orodja.count)
    orodja.count = 0

def razbij_datoteko_na_tri(ime_datoteke, ciljna_dat1, ciljna_dat2, ciljna_dat3):
    orodja.pripravi_imenik(ciljna_dat1)
    orodja.pripravi_imenik(ciljna_dat2)
    orodja.pripravi_imenik(ciljna_dat3)
    
    with open(ime_datoteke, "r", encoding="utf-8") as dat:
        besedilo = dat.read()
    
    tekme = besedilo.split("tekma")
    stevilo_tekem = len(tekme)

    with open(ciljna_dat1, "w", encoding="utf-8") as dat:
        for i in range(1,stevilo_tekem//3):
            dat.write(f"{i}. tekma\n")
            dat.write(tekme[i])
    
    with open(ciljna_dat2, "w", encoding="utf-8") as dat:
        for i in range(stevilo_tekem//3, 2 * stevilo_tekem//3):
            dat.write(f"{i + 1}. tekma\n")
            dat.write(tekme[i])
    
    with open(ciljna_dat3, "w", encoding="utf-8") as dat:
        for i in range(2 * stevilo_tekem//3, stevilo_tekem):
            dat.write(f"{i + 1}. tekma\n")
            dat.write(tekme[i])

def main(redownload=True, reparse=True):
    # Najprej v lokalno datoteko shranimo glavno stran
    #################shrani_tekme_v_html(id_prve_redne_tekme,id_zadnje_redne_tekme,html_tekme_redne,True)
    razbij_datoteko_na_tri(html_tekme_redne, html_tekme_redne1, html_tekme_redne2, html_tekme_redne3)
    # Iz lokalne (html) datoteke preberemo podatke

    # Podatke preberemo v lepšo obliko (seznam slovarjev)

    # Podatke shranimo v csv datoteko

    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
    # in enako za pretvorbo


if __name__ == '__main__':
    main()