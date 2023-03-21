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

STATIC_PATHS = ["extra/custom.css", "extra/CNAME", "images", "downloads"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
}
CUSTOM_CSS = "static/custom.css"

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARCHIVES_SAVE_AS = "archives.html"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["pelican_alias", "i18n_subsites"]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
