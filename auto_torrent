from requests import get
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from sys import argv
from subprocess import call


def get_magnet(search):
    """Gets magnet link from given search term
    
    Makes a request to The Pirate Bay.
    Uses BeautifulSoup to parse the Response and gets the first magnet link
    
    Parameters:
    search term to find
    
    Returns:
    magnet link
    """

    tpb = get('https://piratebay.party/search/'+ search.replace(' ','%20') +'/1/99/0')
    html = bs(tpb.text, 'html.parser')

    # get first link with 'magnet' term
    for link in html.find_all('a'):
        href = link.get('href')
        if 'magnet' in href:
            return href

    return None


if __name__ == '__main__':

    if len(argv) > 2:

        search = ' '.join(argv[1:])
        magnet = get_magnet(search)

        # call for transmission
        if magnet is not None:
            call(["transmission-gtk", magnet])
        else:
            print("No magnets found for", search)

    else:
        print("No input")


for i in range(28,60):
    search = f'MasterChef Australia S14E{i} 1080p HEVC x265-MeGusta'

    magnet = get_magnet(search)

    call(["transmission-gtk", magnet])
