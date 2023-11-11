AUTHOR = 'Clément Fontaine'
SITENAME = "Clément's Blog"
SITESUBTITLE = "Articles about hiking, skiing, cooking in the backcountry, thoughts about the outdoor and wilderness."
SITEURL = ''
THEME = 'theme'
STATIC_PATHS = [
    'static/robots.txt',
    'static/favicon.ico',
    'static/apple-touch-icon.png',
    ]
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    }

PATH = 'content'
IMAGE_PROCESS = {
    "article-image": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
