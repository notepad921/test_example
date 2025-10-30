from config.settings import BASE_URL

def form_page_url_by_language(language: str) -> str:
    """ Form base url by passed language. 'cz' is default. """
    return f"{BASE_URL}{language}/"