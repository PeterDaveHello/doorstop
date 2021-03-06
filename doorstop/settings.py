"""Settings for the Doorstop package."""

import logging

# Logging settings
DEFAULT_LOGGING_FORMAT = "%(message)s"
LEVELED_LOGGING_FORMAT = "%(levelname)s: %(message)s"
VERBOSE_LOGGING_FORMAT = "[%(levelname)-8s] %(message)s"
VERBOSE2_LOGGING_FORMAT = "[%(levelname)-8s] (%(name)s @%(lineno)4d) %(message)s"  # pylint: disable=C0301
QUIET_LOGGING_LEVEL = logging.WARNING
DEFAULT_LOGGING_LEVEL = logging.WARNING
VERBOSE_LOGGING_LEVEL = logging.INFO
VERBOSE2_LOGGING_LEVEL = logging.DEBUG
VERBOSE3_LOGGING_LEVEL = logging.DEBUG - 1

# Value constants
SEP_CHARS = "-_."  # valid prefix/number separators
SKIP_EXTS = ['.yml', '.csv', '.tsv']  # extensions skipped in reference search
RESERVED_WORDS = 'all',  # keywords that cannot be used for prefixes

# Formatting settings
MAX_LINE_LENGTH = 79  # line length to trigger multiline on extended attributes

# Validation settings
REFORMAT = True  # reformat item files during validation
REORDER = False  # reorder document levels during validation
CHECK_LEVELS = True  # validate document levels during validation
CHECK_REF = True  # validate external file references
CHECK_CHILD_LINKS = True  # validate reverse links
CHECK_SUSPECT_LINKS = True  # check stamps on links
CHECK_REVIEW_STATUS = True  # check stamps on items

# Publishing settings
PUBLISH_CHILD_LINKS = True  # include child links when publishing
PUBLISH_BODY_LEVELS = True  # include levels on non-header items

# Caching settings
CACHE_ITEMS = True
CACHE_DOCUMENTS = True

# Server settings
SERVER_HOST = None  # '' = server not specified, None = no server in use
SERVER_PORT = 7867
