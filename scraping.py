import requests
from bs4 import BeautifulSoup

def get_price(URL:str, domain:str) -> float:
    """
    Get the price of a product from a URL
    
    Parameters
    ----------
    URL : str
        URL of the product
    domain : str
        domain of the URL
    
    Returns
    -------
    float
        price of the product
    """

    if domain == 'www.amazon.co.uk':
        return amazon_uk_price(URL)
    elif domain == 'www.amazon.com':
        return amazon_com_price(URL)
    else:
        raise Exception(f"Unrecognised domain. Domain {domain} is not supported. URL: {URL}")

def amazon_uk_price(URL) -> float:
    """
    Get the price of a product from an Amazon.co.uk URL
    
    Parameters
    ----------
    URL : str
        URL of the product
        
    Returns
    -------
    float
        price of the product
    """
    soup = get_soup(URL)
    price_int = float(soup.find("span", {"class": "a-price-whole"}).text.strip())
    price_dec = float(soup.find("span", {"class": "a-price-fraction"}).text.strip())
    return price_int + price_dec/100

def amazon_com_price(URL) -> float:
    """
    Get the price of a product from an Amazon.com URL
    
    Parameters
    ----------
    URL : str
        URL of the product
    
    Returns
    -------
    float
        price of the product
    """
    raise Exception(f"Amazon.com is not yet supported. URL: {URL}")

def get_name(URL:str, domain:str) -> str:
    """
    Get the name of a product from a URL
    
    Parameters
    ----------
    URL : str
        URL of the product
    domain : str
        domain of the URL
    
    Returns
    -------
    str
        name of the product
    """

    if domain == 'www.amazon.co.uk':
        return amazon_uk_name(URL)
    elif domain == 'www.amazon.com':
        return amazon_com_name(URL)
    else:
        raise Exception(f"Unrecognised domain. Domain {domain} is not supported. URL: {URL}")
    
def amazon_uk_name(URL) -> str:
    """
    Get the name of a product from an Amazon.co.uk URL

    Parameters
    ----------
    URL : str
        URL of the product

    Returns
    -------
    str
        name of the product
    """
    soup = get_soup(URL)
    return soup.find("span", {"id": "productTitle"}).text.strip()

def amazon_com_name(URL) -> str:
    """
    Get the name of a product from an Amazon.com URL
    
    Parameters
    ----------
    URL : str
        URL of the product
        
    Returns
    -------
    str
        name of the product
    """
    raise Exception(f"Amazon.com is not yet supported. URL: {URL}")

def get_soup(URL):
    """
    Get the soup of a URL
    
    Parameters
    ----------
    URL : str
        URL to get the soup from
    
    Returns
    -------
    BeautifulSoup
        soup of the URL
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup