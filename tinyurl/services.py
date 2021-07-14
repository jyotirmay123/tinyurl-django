from typing import List, Optional
import re
from urllib.parse import quote_plus, unquote_plus
import shortuuid

from tinyurl.models import Urls


def is_valid_url(url: str) -> bool:
    """Check if the url is a valid `tier.app` url.

        Args:
            url (string): full tier.app url passed from UI.

        Reurns:
            (boolean): True if valid else False
    """
    # A regex pattern to match for tier.app
    pattern = re.compile(r'(https?://)?(www\.)?(tier\.app/)(\w+)')
    if pattern.match(url):
        return True
    else:
        return False


def push_url(url: str):
    """Push the url to database

        Args:
            url (string): full tier.app url passed from UI.

    """
    # Check if an entry for the url already exist in the db.
    if not Urls.objects.filter(full_url=url).exists():
        # Creating a tinyurl based on url passed and having tier.app as base.
        tiny_url = f"http://tier.app/{shortuuid.uuid(name=url)[:7]}"
        quoted_tiny_url = quote_plus(tiny_url)
        # Pushing the url object to databse.
        Urls(full_url=url, tiny_url=tiny_url,
             quoted_tiny_url=quoted_tiny_url).save()


def get_urls() -> List[Urls]:
    """Get all url entried from db.

        Returns:
            (List(Url Object)): A list containing all urls entry in the db.
    """
    return Urls.objects.all()


def get_url(tiny_url: str) -> Optional[Urls]:
    """Fetch a matched url entry from db by comparing to the argument passed.

        Args:
            tiny_url (string): A tiny url corresponds to an original url in the db.

        Returns:
            (Url Object | None): A matched url object if found else None
    """
    # Check if a match exists
    if Urls.objects.filter(tiny_url=unquote_plus(tiny_url)).exists():
        return Urls.objects.filter(tiny_url=unquote_plus(tiny_url)).get()
    else:
        return None


def increment_hits(url_object: Urls):
    """Incrementing the number of hits corresponding to a particular Url object and updating the db.

        Args:
            url_object (Urls): A Urls Object.
    """
    # Incrementing the hits count.
    url_object.hits += 1
    # Saving the url_object back into db.
    url_object.save()
