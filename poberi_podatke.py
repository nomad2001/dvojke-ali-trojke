import orodja

url = "https://www.espn.com/nba/boxscore/_/gameId/"
url_wrong = "https://www.espn.com/nba/scoreboard"
html_tekme_redne = "tekme_redne.html"
html_tekme_playoff = "tekme_playoff.html"
csv_tekme_redni_del = "tekme_redne.csv"
csv_tekme_playoff = "tekme_playoff.csv"
csv_ekipe = "ekipe.csv"
id_prve_redne_tekme = 401266805
id_zadnje_redne_tekme = 401307891
id_prve_playoff_tekme = 401327715
id_zadnje_playoff_tekme = 401344140

def shrani_tekme_v_html(zacetni_id, koncni_id, ime_datoteke, vsili_prenos = False):
    for i in range(zacetni_id, koncni_id + 1):
        orodja.shrani_spletno_stran(url + str(i), ime_datoteke, vsili_prenos)
    print(orodja.count)
    orodja.count = 0