from urllib.parse import urlparse

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

        parsed_url = urlparse(URL)
        if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
            self._URL = URL
        else:
            parsed_url = urlparse('https://' + URL)
            if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
                self.URL = parsed_url.geturl()
            else:
                raise ValueError("Invalid URL")
            
    @property
    def domain(self):
        """
        domain of the URL"""
        return urlparse(self.URL).netloc