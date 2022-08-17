from datetime import datetime

AUTHOR = 'Ali Lasemi'
SITENAME = "Ali Lasemi"
SITETITLE = "Ali Lasemi"
SITESUBTITLE = 'Project Portfolio'
SITEURL = ''

THEME = '../pelican-themes/Flex'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Used to add additional links to the blogroll
#LINKS = (
#    ('wikipedia', 'https://wikipedia.org'),
#)

USE_FOLDER_AS_CATEGORY = False
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (
    ('github', 'https://github.com/alilasemi'),
)

# TODO
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "language": "en_US",
}
COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images',]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
