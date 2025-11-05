---
title: "Tools"
---

Not included here is project-related code or other things not meant for general use. See my [Github profile](https://github.com/sbaack) for more of my coding and writing.

### [archive-md-urls](https://github.com/sbaack/archive-md-urls)

A tool to convert URLs in Markdown files into snapshots from archive.org. The primary use case are blogs written with static site generators like [Hugo](https://gohugo.io/) or [Jekyll](https://jekyllrb.com/) that rely on Markdown. The tool will try to use archive.org snapshots close to the time stamp of blog posts and recognizes "stable" URLs that won't be changed, like intra-site links or  URLs that contain stable identifiers.

### [pymac](https://github.com/sbaack/pymac)

A command line tool for installing and managing Python versions from [Python.org's](https://www.python.org/) Mac installers. Allows you to download, install and manage Python.org versions entirely from the command line.
 
### [github-scraper](https://github.com/sbaack/github-scraper)
 
This tool focuses on scraping information from [organizational Github accounts](https://developer.github.com/v3/orgs/), which means that it only takes a list of organizations as input, not normal user accounts. It generates CSV spreadsheets or [GEXF](https://gexf.net/) files to be used in network analysis software like [Gephi](https://gephi.org/). See [this blogpost]({{< ref "posts/2015-11-19-scraping-the-global-civic-tech-community-on-github-part-2" >}}) for an example for an example of an analysis conducted with this tool.
