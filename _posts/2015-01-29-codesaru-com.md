---
layout:       post
title:        "codesaru.com"
date:         2015-01-29
date_begin:   2012
date_end:     2018
date_release: 2015-01-29
categories:   projects
priority:     50
slug:         codesaru-com
image_main:   codesaru-jinja.png
---
This site was originally made with Drupal.  That was very nice for a while.  Eventually extensions, data backup and installation processes became a hassle.  To keep surprise maintenance to a minimum, the site was re-written with [Flask][].  Since long-term low-maintenance is the main goal on this rewrite, I've stuck with well-maintained tools and stayed away from fancy things.

Then the hosting service used for the Python/Flask Webserver changed and it went out of date.  Now this site uses [Jekyll][] to create static pages, which are then hosted on [GitHub Pages][].

Disclaimer: I'm not experienced with any of the tools being used here.  So don't take it as best-practice if you're learning, and be nice when judging it.

## Source
This site's main code can be found in [this repo][codesaru.com repo].  To run it locally for development, follow the "how to use" section in its readme.  Feel free to fork and modify, though the stories vs. projects setup is a little wonky (they're ultimately all posts).

## Tools and Languages
[CSS][], [Flask][], [HTML][], [Jekyll][], [Liquid][], [Markdown][], [Python][]

[codesaru.com repo]: https://github.com/Akaito/codesaru.com
[css]: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
[flask]: http://flask.pocoo.org/
[github pages]: https://pages.github.com/
[html]: https://en.wikipedia.org/wiki/HTML
[jekyll]: https://jekyllrb.com/
[liquid]: https://shopify.github.io/liquid/
[markdown]: https://daringfireball.net/projects/markdown/
[python]: https://www.python.org/
