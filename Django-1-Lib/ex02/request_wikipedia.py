#!/usr/bin/env python3
"""
Exercise 02: Request an API
Query the Wikipedia API for a given search term, convert the resulting
wikitext to plain text, and write it to a <name_of_the_search>.wiki file.

Authorized modules: requests, json, dewiki, sys
"""
import sys
import json
import requests
import dewiki.dewiki as dewiki

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"


def _build_filename(search_term):
    """Turn the search term into a valid, space-free filename."""
    cleaned = "_".join(search_term.split())
    return "{}.wiki".format(cleaned)


def _search_page_title(search_term, session):
    """
    Use the Wikipedia search endpoint to find the closest matching
    article title for the given (possibly misspelled) search term.
    """
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search_term,
        "format": "json",
        "srlimit": 1,
    }
    response = session.get(WIKI_API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = data.get("query", {}).get("search", [])
    if not results:
        raise ValueError("no result found for '{}'".format(search_term))

    return results[0]["title"]


def _fetch_wikitext(page_title, session):
    """Fetch the raw wikitext content of a given Wikipedia page."""
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "titles": page_title,
        "format": "json",
    }
    response = session.get(WIKI_API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    if not pages:
        raise ValueError("no page content found for '{}'".format(page_title))

    page = next(iter(pages.values()))
    if "missing" in page:
        raise ValueError("page '{}' does not exist".format(page_title))

    try:
        wikitext = page["revisions"][0]["slots"]["main"]["*"]
    except (KeyError, IndexError):
        raise ValueError("could not extract content for '{}'".format(page_title))

    return wikitext


def request_wikipedia(search_term):
    """
    Search Wikipedia for search_term, convert the article's wikitext to
    plain text and write it to a file named after the search term.
    """
    if not search_term or not search_term.strip():
        print("Error: a non-empty search parameter is required.")
        return

    session = requests.Session()

    try:
        page_title = _search_page_title(search_term, session)
        wikitext = _fetch_wikitext(page_title, session)
        plain_text = dewiki.clean(wikitext)

        if not plain_text or not plain_text.strip():
            raise ValueError("empty content after conversion")

        filename = _build_filename(search_term)
        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(plain_text)

    except requests.exceptions.RequestException as error:
        print("Error: a network/server problem occurred ({})".format(error))
    except (ValueError, KeyError) as error:
        print("Error: {}".format(error))
    except json.JSONDecodeError:
        print("Error: invalid response received from the Wikipedia API.")
    except Exception as error:
        print("Error: an unexpected error occurred ({})".format(error))


def main(argv):
    if len(argv) != 2:
        print("Error: usage: python3 request_wikipedia.py \"<search term>\"")
        return
    request_wikipedia(argv[1])


if __name__ == '__main__':
    main(sys.argv)
