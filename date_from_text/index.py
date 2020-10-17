import datetime


def valid_year(year):
    if year and year.isdigit():
        if int(year) >= 1900 and int(year) <= 2020:
            return int(year)


def find_date_in_text(txt, months=['januari', 'februari', 'maart', 'april', 'mei', 'juni',
                                   'juli', 'augustus', 'september', 'oktober', 'november', 'december']):
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
