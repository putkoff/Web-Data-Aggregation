import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_
import inspect
import re
from urllib.parse import urlparse, urljoin
from abstract_utilities.class_utils import *
import ssl
import time
import logging
def change_glob\([^)]*\):
    """
    Change the value of a global variable.

    Args:
        name (str): The name of the global variable to be changed.
        var (any): The new value to be assigned to the global variable.

    Returns:
        any: The new value assigned to the global variable.
    """
    globals()[name]=var
    return var
class TLSAdapter(HTTPAdapter):
    def ssl_options\([^)]*\):
        """
        Configure SSL options to disable TLSv1, TLSv1.1, and compression.

        Returns:
            int: Combined SSL options for disabling certain TLS versions and compression.
        """
        return ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_COMPRESSION

    def __init__\([^)]*\):
        """
        Initialize the TLSAdapter.

        Args:
            ssl_options (int, optional): SSL options used to disable certain TLS versions and compression.
            *args: Positional arguments for the superclass HTTPAdapter.
            **kwargs: Keyword arguments for the superclass HTTPAdapter.
        """
        self.ssl_options = ssl_options
        super().__init__(*args, **kwargs)

    def add_string_list(self, ls: (list or str), delim: str = '', string: str = ''):
        if isinstance(ls, str):
            ls = list(ls.split(','))
        if isinstance(ls, list):
            string = ''
            for part in ls:
                string = string + delim + part
        return string

    def get_ciphers\([^)]*\):
        """
        Get the list of cipher suites.

        Returns:
            list: The list of cipher suites.
        """
        return "ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-SHA256,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES128-SHA256,AES256-SHA,AES128-SHA".split(',')

    def create_ciphers_string\([^)]*\):
    """
        Create a string of cipher suites to be used in the TLS context.

        Args:
            ls (list, optional): The list of cipher suites. If not provided, a default list will be used.

        Returns:
            str: The string of cipher suites.
    """
        if ls is None:
            ls = self.get_ciphers()
        cipher_string = self.add_string_list(ls=ls, delim=':')[:-1]
        globals()['CIPHERS'] = cipher_string
        return cipher_string

    def init_poolmanager\([^)]*\):
    """
        Initialize the connection pool manager with the configured TLS context.

        Args:
            *args: Positional arguments for the superclass PoolManager.
            **kwargs: Keyword arguments for the superclass PoolManager.
    """
        context = ssl_.create_urllib3_context(ciphers=self.create_ciphers_string(), cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*args, ssl_context=context, **kwargs)
def create_columns\([^)]*\):
    """
    Split a list into nested lists of specified size.

    Args:
        ls (list): The original list to be split.
        i (int): The current index.
        k (int): The size of each nested list.

    Returns:
        list: The list split into nested lists.
    """
    if float(i) % float(k) == float(0.00) and i != 0:
        lsN = list(ls[:-k])
        lsN.append(list(ls[-k:]))
        ls = lsN
    return ls
def is_valid\([^)]*\):
    """
    Check whether a URL is valid.

    Args:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def format_url\([^)]*\):
    """
    Format a URL to include the 'https://' prefix if missing.

    Args:
        url (str): The URL to be formatted.

    Returns:
        str: The formatted URL.
    """
    # Check if the URL starts with 'http://' or 'https://'
    if not url.startswith(('http://', 'https://')):
        # Add 'https://' prefix if missing
        url = 'https://' + url
    # Check if the URL has a valid format
    if not re.match(r'^https?://\w+', url):
        # Return None if the URL is invalid
        return None
    return url
def try_request(url: str, session: type(requests.Session) = requests):
    try:
        return session.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return False
def desktop_user_agents\([^)]*\):
    """
    Get a list of desktop user agent strings.

    Returns:
        list: The list of desktop user agent strings.
    """
    return ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14']
def get_user_agent(user_agent=desktop_user_agents()[0]):
    return {"user-agent": user_agent}

def get_parser_choices\([^)]*\):
    """
    Get a list of available parser choices for BeautifulSoup.

    Returns:
        list: The list of parser choices.
    """
        return ['html.parser', 'lxml', 'html5lib']
def get_bs4_options\([^)]*\):
    """
    Get a list of BeautifulSoup objects and their descriptions.

    Returns:
        list: A list of tuples containing BeautifulSoup object names and their descriptions.
    """
    bs4_options = [
        'BeautifulSoup',
        'Tag',
        'NavigableString',
        'Comment',
        'ResultSet',
        'SoupStrainer',
        'CData'
    ]
    descriptions = [
        'The main BeautifulSoup class used for parsing HTML.',
        'Represents an HTML tag.',
        'Represents a string within an HTML document.',
        'Represents an HTML comment.',
        'Represents a collection of tags found during a search.',
        'Allows parsing only a specific subset of the HTML document.',
        'Represents a CDATA section within an XML document.'
    ]
    return list(zip(bs4_options, descriptions))
def get_soup(data, selected_option: str = get_parser_choices()[0]):
    try:
        soup = change_glob('last_soup', BeautifulSoup(data, selected_option))
    except:
        soup = None
    return soup
def find_all_soup\([^)]*\):
    """
    Find all occurrences of a tag or string in the last_soup.

    Args:
        string (str): The tag or string to find.

    Returns:
        ResultSet: A collection of tags or strings that match the search criteria.
    """
    return last_soup.find_all(string)
def get_status(url):
    return try_request(url=url).status_code
def all_soup(data, tag, typ, clas, inp):
    print(getattr(last_soup, tag, typ))  # ,string))
    return getattr(last_soup, tag, typ)
def find_all_soup\([^)]*\):
    """
    Find all occurrences of a tag or string in the last_soup.

    Args:
        string (str): The tag or string to find.

    Returns:
        ResultSet: A collection of tags or strings that match the search criteria.
    """
    return last_soup.find_all(string)
def parse_all\([^)]*\):
    """
    Parse the HTML data to get lists of tag types, tag descriptions, tags, and classes.

    Args:
        data (str): The HTML data to be parsed.

    Returns:
        tuple: A tuple containing lists of tag types, tag descriptions, tags, and classes.
    """
    ls_type, ls_tag, ls_class, ls_desc = [], [], [], []
    data = str(data).split('<')
    for k in range(1, len(data)):
        dat = data[k].split('>')[0]
        if dat[0] != '/':
            if dat.split(' ')[0] not in ls_type:
                ls_type.append(dat.split(' ')[0])
        dat = dat[len(dat.split(' ')[0]) + 1:].split('"')
        for c in range(1, len(dat)):
            if len(dat[c]) > 0:
                if '=' == dat[c][-1] and ' ' == dat[c][0] and dat[c] != '/':
                    if dat[c][1:] + '"' + dat[c + 1] + '"' not in ls_desc:
                        ls_desc.append(dat[c][1:] + '"' + dat[c + 1] + '"')
                    if dat[c][1:-1] not in ls_tag:
                        ls_tag.append(dat[c][1:-1])
                    if dat[c + 1] not in ls_class:
                        ls_class.append(dat[c + 1])
    return ls_type, ls_desc, ls_tag, ls_class
def parse_react_source\([^)]*\):
    """
    Parse the HTML data to extract React source code from script tags.

    Args:
        data (str): The HTML data to be parsed.

    Returns:
        list: A list of extracted React source code from script tags.
    """
    soup = BeautifulSoup(data, 'html.parser')
    script_tags = soup.find_all('script', type=lambda t: t and ('javascript' in t or 'jsx' in t))
    react_source_code = []
    for script_tag in script_tags:
        react_source_code.append(script_tag.string)
    return react_source_code
def get_parsed_html(url: str = 'https://www.example.com', user_agent= desktop_user_agents()[0]):
    s = requests.Session()
    s.cookies["cf_clearance"] = "cb4c883efc59d0e990caf7508902591f4569e7bf-1617321078-0-150"
    s.headers.update(get_user_agent(user_agent))
    adapter = TLSAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    s.mount('https://', adapter)
    r = try_request(url=url, session=s)

    if r is False:
        return None
    return r.text
def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = [url]
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(get_parsed_html(url=url), "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            continue
        urls.append(href)
    return urls
def get_elements(url):
    # Step 1: Get the source code from the provided URL.

    source_code = get_parsed_html(url)
    print(source_code)  # Prints the source code

    # Step 2: Get the BeautifulSoup object from the source code
    soup = get_soup(source_code)
    print(soup)  # Prints the BeautifulSoup object

    # Step 3: Get the listed categories from the soup
    listed_categories = parse_all(soup)
    print(listed_categories)  # Prints the listed categories

    # From here, you can use listed_categories to refine your results further according to your needs.
    # For instance:

    # Step 4: Filter elements using the first category
    filtered_elements = [element for element in soup if element.name in listed_categories[0]]
    return filtered_elements  # Prints elements filtered by the first category
