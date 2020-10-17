import re
import datetime

story1 = "Vanaf 29 augustus 1939? In maart 1942 werden in Amsterdam 786.000 bonkaarten uitgerijkt, in december 1943 706.000, een afname dus van 80.000.<span class='italic'>'Deze cijfers illustreren voldoende de tragedie van gedeporteerde Joden en arbeiders die in Duitsland werkten'</span> meent de schrijver van het boekje <span class='italic'>Amsterdams distrubutiedienst zoald de Duitsers hem niet kenden!</span>, dat in 1945 verscheen. Personeel van de distributiedienst werkten soms samen met de illegaliteit om onderduikers van bonkaarten te voorzien. Het gebouw is afgebroken."
story2 = "Toen hier mensen op 21 februari 1945 bezig waren houten blokjes uit het wegdek te stelen, trok een agent zijn dienstpistool om ze weg te jagen. Koopman Peter Wienese van Singel 384 rukte het pistool uit handen van de agent en wierp het in de Herengracht. 'Aan de politie zal verzocht worden naar het aldus verloren gegane wapen te dreggen', meldt het politierapport"
story3 = "Boekhandel en uitgeverij van de uit Duitsland gevluchte Louis lamm.<span class='italic'>'Grösste jüd Antiquariat in Europa'</span> volgens een advertentie <span class='italic'>Het Joodse Weekblad</span> in 1941. Bovenbuurman Cas Oorthuys had een onderduikadres voor Lamm gevonden, maar daar wilde hij niet aan. De Einsatztab Reichsleiter  Rosenberg 'zuiverde' het antiquariaat na zijn deportatie in oktober 1943. 'Toen ze weggevoerd waren, stonden er plotseling ladders tegen de gevel en hing er er een lange houten goot uit het raam die over de kade naar een dekschuit liep', vertelt Lydia Oorthuys-Krienen in het boek <span class='italic'>Cas Oorthuys Amsterdam</span>.'Dagenlang hebben ze toen alle kostbare boeken als oud vuil door die goot op die schuit gesmakt'. Lamm werd vermoord in Auschwitz in november 1943. Afgebroken."
story4 = "Huis van Cas Oorthuys en Lydia Oorthuys-Krienen. Oorthuys was een van de fotografen van De Ondergedoken camera, een illegale groep die de Duitse bezetting wilde documenteren. Hij maakte ook pasfoto's voor valse persoonsbewijzen. Lydia Oorthuys vertelde na de oorlog in een boek over Oorhuys' Amsterdam: <span class='italic'>'Het huis aan de Amstel stortte soms bijna in van alle onderduikers. We hebben ze niet geteld of bijgehouden. Sommigen bleven twee of drie nachten, anderen kwamen voor één nacht, maar bleven de hele oorlog. Van de meeste mensen wist je de namen niet en die wilde je ook niet weten, dan kon je ze bij een eventuele verhoor ook niet verraden.'</span> Tot de onderduikers behoorde onder meer de Duits-Joodse communist Nathan Notowicz van de Groep Oosteinde. Cas Oorthuys werd in mei 1944 gearresteerd en naar Kamp Amersfoort gebracht. Hij kwam na drie maanden vrij dankzij bemiddeling van zijn vroegere vriend Nico de Haas, inmiddels ss'er en een tijd hoofdredacteur van het weekblad <span class='italic'>Storm</span>"

textlist = [story1, story2, story3, story4]


months = ['januari', 'februari', 'maart', 'april', 'mei', 'juni',
          'juli', 'augustus', 'september', 'oktober', 'november', 'december']


def valid_year(year):
    if year and year.isdigit():
        if int(year) >= 1900 and int(year) <= 2020:
            return int(year)


def find_date_in_text(txt):
    '''
     Method to find a date with the format {dd month yyyy} in a text
    1. Walk through all the words
    2. tests if the word is a number
    3. tests if the word is a month after that
    4. tests whether the word is a year after that     
    '''
    wordlist = txt.split()
    for i in range(len(wordlist)):

        if(wordlist[i].isdigit()):
            try:
                # find next word . is month?
                index = months.index(wordlist[i+1])
                is_valid_year = valid_year(
                    wordlist[i+2].rstrip('.').rstrip('!').rstrip('?').rstrip(';'))
                if is_valid_year is not None:

                    return datetime.datetime(
                        is_valid_year, index+1, int(wordlist[i]))

            except ValueError:
                pass


story = story4
for text in textlist:
    if find_date_in_text(text):
        print(find_date_in_text(text))

print('klaar')
