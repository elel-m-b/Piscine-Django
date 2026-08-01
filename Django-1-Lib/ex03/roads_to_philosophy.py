#!/usr/bin/env python3
"""
Exercise 03: HTML Parser
Check the "Getting to Philosophy" phenomenon: starting from a Wikipedia
article, keep following the first valid link in the introduction until
reaching the Philosophy article, a dead end, or an already-visited page.

Authorized modules: sys, requests, BeautifulSoup (bs4)
"""
import sys
import requests
from bs4 import BeautifulSoup

WIKI_SEARCH_URL = "https://en.wikipedia.org/wiki/Special:Search"
WIKI_BASE_URL = "https://en.wikipedia.org"
PHILOSOPHY_TITLE = "Philosophy"


def _get_soup(url, session):
    """Fetch a URL and return a BeautifulSoup object of its HTML content."""
    response = session.get(url, timeout=10, allow_redirects=True)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser"), response.url


def _get_title(soup):
    """Extract the main title of a Wikipedia article page."""
    heading = soup.find(id="firstHeading")
    if heading is None:
        raise ValueError("could not find the page title")
    return heading.get_text(strip=True)


def _is_valid_link(href, title_attr):
    """
    Decide whether a link found in the introduction is a valid link to
    another Wikipedia article (as opposed to help pages, files, external
    links, references, etc.)
    """
    if not href or not href.startswith("/wiki/"):
        return False
    if ":" in href.split("/wiki/", 1)[1]:
        # Namespaces like Help:, File:, Wikipedia:, Special:, Category:, etc.
        return False
    if "#" in href:
        return False
    if title_attr is None:
        return False
    return True


def _first_intro_link(soup):
    """
    Find the first link, in the introductory paragraphs of the article,
    that leads to another valid Wikipedia article. Links inside italics,
    parentheses, or other non-eligible zones are ignored per the rule
    described in the subject; here we simply walk paragraph by paragraph
    and skip invalid targets (help pages, files, etc.).
    """
    content = soup.find(id="mw-content-text")
    if content is None:
        return None

    parser_output = content.find("div", class_="mw-parser-output")
    if parser_output is None:
        parser_output = content

    for paragraph in parser_output.find_all("p", recursive=False):
        # Skip paragraphs that are effectively empty (coordinates, etc.)
        if not paragraph.get_text(strip=True):
            continue
        for link in paragraph.find_all("a", href=True):
            href = link.get("href")
            title_attr = link.get("title")
            if _is_valid_link(href, title_attr):
                return WIKI_BASE_URL + href
        # Only consider the first non-empty paragraph as "the introduction"
        break

    return None


def roads_to_philosophy(search_term):
    """
    Follow the chain of first-links from search_term until Philosophy,
    a dead end, or an infinite loop is reached, then print the result.
    """
    session = requests.Session()
    visited_titles = []
    visited_urls = set()

    try:
        current_url = "{}?search={}&go=Go".format(
            WIKI_SEARCH_URL, requests.utils.quote(search_term)
        )

        while True:
            soup, resolved_url = _get_soup(current_url, session)

            if resolved_url in visited_urls:
                print("It leads to an infinite loop !")
                return

            visited_urls.add(resolved_url)

            title = _get_title(soup)
            visited_titles.append(title)

            if title == PHILOSOPHY_TITLE:
                print("\n".join(visited_titles))
                print(
                    "{} roads from {} to philosophy !".format(
                        len(visited_titles), search_term
                    )
                )
                return

            next_link = _first_intro_link(soup)
            if next_link is None:
                print("It leads to a dead end !")
                return

            current_url = next_link

    except requests.exceptions.RequestException as error:
        print("Error: a network/server problem occurred ({})".format(error))
    except ValueError as error:
        print("Error: {}".format(error))
    except Exception as error:
        print("Error: an unexpected error occurred ({})".format(error))


def main(argv):
    if len(argv) != 2:
        print("Error: usage: python3 roads_to_philosophy.py \"<search term>\"")
        return
    roads_to_philosophy(argv[1])


if __name__ == '__main__':
    main(sys.argv)
