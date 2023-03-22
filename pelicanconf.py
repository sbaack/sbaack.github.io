#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Stefan Baack"
SITENAME = "Stefan Baack"
SITEURL = ""

PATH = "content"

THEME = "pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "paper"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Mastodon", "https://mozilla.social/@tootbaack"),
    ("Google Scholar", "https://scholar.google.com/citations?hl=en&user=cphFdLUAAAAJ"),
    ("ORCID", "https://orcid.org/0000-0002-2464-7699"),
    ("LinkedIn", "https://de.linkedin.com/in/stefanbaack"),
    ("GitHub", "https://github.com/sbaack"),
    ("Twitter", "https://twitter.com/tweetbaack"),
    ("RSS", f"{SITEURL}/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 5

# By default, HTML files get processed by the article and page generators before the
# static generator, meaning that they won't be included in the generated output as is.
# These settings make sure HTML files in the 'extra' directory are treated as static.
PAGE_EXCLUDES = ["extra"]
ARTICLE_EXCLUDES = ["extra"]

STATIC_PATHS = [
    "extra/custom.css",
    "extra/CNAME",
    "images",
    "downloads",
    # These files are for redirecting old URLs which are used in some publications
    "extra/mapping-the-civic-hacking-community.html",
    "extra/scraping-the-global-civic-tech-community-on-github-part-2.html",
]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
    # For redirection to work properly, imitate directory structure used by Jekyll
    "extra/mapping-the-civic-hacking-community.html": {
        "path": "2015/11/17/mapping-the-civic-hacking-community.html"
    },
    "extra/scraping-the-global-civic-tech-community-on-github-part-2.html": {
        "path": "2015/11/19/scraping-the-global-civic-tech-community-on-github-part-2.html"
    },
}
CUSTOM_CSS = "static/custom.css"

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARCHIVES_SAVE_AS = "archives.html"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["i18n_subsites"]

# Relative URLs for testing locally
RELATIVE_URLS = True
