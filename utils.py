from urllib.parse import urlparse

def validate_URL(URL:str):
    """
    Validate a URL

    Parameters
    ----------
    URL : str
        URL to be validated

    Returns
    -------
    str
        Validated URL
    """

    parsed_url = urlparse(URL)
    if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
        return URL
    else:
        parsed_url = urlparse('https://www.' + URL)
        if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
            return parsed_url.geturl()
        else:
            raise ValueError("Invalid URL")