from os import stat
import orodja
import re
#<td class="name">TEAM
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

def poisci_tekme_v_html(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as dat:
        besedilo = dat.read()

    rx = re.compile(r"(?=tekma(.*?)tekma)",re.DOTALL)
    tekme = re.findall(rx, besedilo)
    return tekme

def izlusci_statistiko_tekme(id, ekipe, tekma):
    gesla = ['FG','3PT', 'FT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS']
    imeni = re.findall(r'<td class="team-name">(?P<Team>.+?)</td>', tekma)
    rx = re.compile(r'<td class="name">TEAM</td><td class="min"></td>'
                    r'<td class="fg">(?P<FG>.*?)</td>'
                    r'<td class="3pt">(?P<THREEPT>.*?)</td>'
                    r'<td class="ft">(?P<FT>.*?)</td>'
                    r'<td class="oreb">(?P<OREB>.*?)</td>'
                    r'<td class="dreb">(?P<DREB>.*?)</td>'
                    r'<td class="reb">(?P<REB>.*?)</td>'
                    r'<td class="ast">(?P<AST>.*?)</td>'
                    r'<td class="stl">(?P<STL>.*?)</td>'
                    r'<td class="blk">(?P<BLK>.*?)</td>'
                    r'<td class="to">(?P<TO>.*?)</td>'
                    r'<td class="pf">(?P<PF>.*?)</td>'
                    r'<td class="plusminus"></td>'
                    r'<td class="pts">(?P<PTS>.*?)</td>',
                    re.DOTALL)

    statistika = re.findall(rx, tekma)

    if len(statistika) == 0 or len(imeni) == 0: ###Pri nekaterih tekmah ni statistike oz. imen ekipe, ker 
        return []                               ###je bila tekma preložena zaradi zaznane okužbe s COVID-om
                                                ###pri kakšnem izmed igralcev
    
    #if id == 8:
    #    with open("test.html","w",encoding="utf-8") as dat:
    #        dat.write(tekma)
    dict1 = {gesla[i] : statistika[0][i] for i in range(len(gesla))}
    dict2 = {gesla[i] : statistika[1][i] for i in range(len(gesla))}
    
    if imeni[0] not in ekipe.keys():
        ekipe[imeni[0]] = len(ekipe) + 1

    if imeni[1] not in ekipe.keys():
        ekipe[imeni[1]] = len(ekipe) + 1

    dict1["Team"] = ekipe[imeni[0]]
    dict2["Team"] = ekipe[imeni[1]]
    dict1["Tekma"] = id
    dict2["Tekma"] = id
    return [dict1, dict2]

def main(redownload=True, reparse=True):
    # Najprej v lokalno datoteko shranimo glavno stran
    #################shrani_tekme_v_html(id_prve_redne_tekme,id_zadnje_redne_tekme,html_tekme_redne,True)
    #################razbij_datoteko_na_tri(html_tekme_redne, html_tekme_redne1, html_tekme_redne2, html_tekme_redne3)
    #################shrani_tekme_v_html(id_prve_playoff_tekme, id_zadnje_playoff_tekme, html_tekme_playoff, True)
    # Iz lokalne (html) datoteke preberemo podatke
    tekme_v_html = []
    tekme_v_html.extend(poisci_tekme_v_html(html_tekme_redne1))
    tekme_v_html.extend(poisci_tekme_v_html(html_tekme_redne2))
    tekme_v_html.extend(poisci_tekme_v_html(html_tekme_redne3))
    tekme = []
    ekipe = {}
    #print(len(tekme_v_html))
    
    for i in range(len(tekme_v_html)):
        #print(tekme_v_html[i])
        #print(str(i) + " ", end='')
        tekme.extend(izlusci_statistiko_tekme(i, ekipe, str(tekme_v_html[i])))
   # print(tekme)
    gesla = ['Tekma', 'Team' ,'FG', '3PT', 'FT', 'OREB', 'DREB', 'REB', 
                                    'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS']
    orodja.zapisi_csv(tekme, gesla, csv_tekme_redni_del)
    # Podatke preberemo v lepšo obliko (seznam slovarjev)

    # Podatke shranimo v csv datoteko

    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
    # in enako za pretvorbo
    #raise NotImplementedError()


if __name__ == '__main__':
    main()
#<td class="name">TEAM</td><td class="min"></td><td class="fg">.*?</td><td class="3pt">.*?</td><td class="ft">.*?</td><td class="oreb">.*?</td><td class="dreb">.*?</td><td class="reb">.*?</td><td class="ast">.*?</td><td class="stl">.*?</td><td class="blk">.*?</td><td class="to">.*?</td><td class="pf">.*?</td><td class="plusminus"></td><td class="pts">.*?</td>
#<td class="name">TEAM</td><td class="min"></td><td class="fg">(?<FG>.*?)</td><td class="3pt">(?<THREEPT>.*?)</td><td class="ft">(?<FT>.*?)</td><td class="oreb">(?<OREB>.*?)</td><td class="dreb">(?<DREB>.*?)</td><td class="reb">(?<REB>.*?)</td><td class="ast">(?<AST>.*?)</td><td class="stl">(?<STL>.*?)</td><td class="blk">(?<BLK>.*?)</td><td class="to">(?<TO>.*?)</td><td class="pf">(?<PF>.*?)</td><td class="plusminus"></td><td class="pts">(?<PTS>.*?)</td>