"""
# Auto Generate Header Anchor
This script parses Github readme markdowns to automatically generate header anchors for headers. 

This is to aid organising Github readme markdowns to increase readability for the viewers.  

This script skips h1 and looks for h2~h4 headers.
"""


# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    """
    This function connects to the url and saves the HTML content to 
    a BeautifulSoup object.
    Then the BeautifulSoup object is returned.

    Input:
    - url: URL link to the target Github readme markdown
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return(soup)

def find_header(soup):
    """
    This function finds the headers by parsing through the HTML
    elements based on the anchor class.
    The headers are saved in a list in a first-come, first-served order.
    The function then returns the header list.

    Input:
    - soup: BeautifulSoup object 
    """

    headers_order = []
    for element in soup.find_all('a', {'class': 'anchor'}):
        header = element['href']
        headers_order.append(header)
    
    return(headers_order)

def make_anchor(headers_order):
    """
    This function creates markdown anchors for the determined headers.
    This firstly identifies headers again based on the header size and 
    determine its title and href to create markdown anchors.
    Then the anchors are sorted based on the header order given via the input.
    The ordered anchors are returned.

    Input:
    - headers_order: list of headers in a first-come, first-served order
    """
    size_prefix_dict = dict({'h2':'-', 'h3':'  -', 'h4':'    -'})
    size_header_dict = dict()
    anchors = []
    orders = []

    # find headers by header size
    for size in size_prefix_dict.keys():
        header_li = soup.find_all(size, {'dir':'auto'})

        if len(header_li) == 0:
            continue
        else:
            size_header_dict[size] = header_li

    # create markdown anchors
    for size, header_li in size_header_dict.items():
        for header in header_li:
            title = header.text
            href = header.a['href']
            prefix = size_prefix_dict[size]
            anchor = f'{prefix}[{title}]({href})'
            order = headers_order.index(href)

            anchors.append(anchor)
            orders.append(order)

    # sort anchors by header order
    anchors_series = pd.Series(data=anchors, index=orders)
    ordered_anchors = anchors_series.sort_index()

    return(ordered_anchors)

def print_anchors(anchors):
    """
    This function prints out markdown anchors.

    Input:
    - anchors: ordered anchors in string
    """

    for anchor in anchors:
        print(anchor)

def main():
    # create BeautifulSoup object of the Github readme markdown HTML
    url = input('Please type URL for Github ReadMe markdown: ')
    soup = get_html(url)

    # find all headers in order
    headers_order = find_header(soup)

    # create markdown anchors for the headers
    anchors = make_anchor(headers_order)

    # print markdown anchors
    print_anchors(anchors)

    
if __name__ == "__main__":
    main()
