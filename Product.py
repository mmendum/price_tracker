from urllib.parse import urlparse
import scraping
import utils
import time

class Product:
    """
    Class to represent a product information from a URL
    
    Attributes
    ----------
    URL : str
        URL of the product
    domain : str
        domain of the URL"""
    
    def __init__(self, URL:str):
        """
        Parameters
        ----------
        URL : str
            URL of the product"""
        self.URL = URL

    @property
    def URL(self):
        """
        URL of the product"""

        return self._URL
    
    @URL.setter
    def URL(self, URL:str):
        """
        URL of the product"""

        self._URL = utils.validate_URL(URL)
            
    @property
    def domain(self):
        """
        domain of the URL"""
        return urlparse(self.URL).netloc
    
    @property
    def price(self):
        """
        Current price of the product"""
        return scraping.get_price(self.URL, self.domain)

    @property
    def name(self):
        """
        Name of the product"""
        return scraping.get_name(self.URL, self.domain)
    
    def update(self):
        """
        Return the latest price, with corresponding date and time"""
        return [time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"), self.price]