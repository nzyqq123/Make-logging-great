import logging
import sys


class Foreground:
    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    PURPLE = "35"
    CYAN = "36"
    WHITE = "37"

    WARNING = YELLOW
    INFO = GREEN
    DEBUG = BLUE
    CRITICAL = CYAN
    ERROR = RED


class Background:
    BLACK = "40"
    RED = "41"
    GREEN = "42"
    YELLOW = "43"
    BLUE = "44"
    PURPLE = "45"
    CYAN = "46"
    WHITE = "47"

    WARNING = Foreground.YELLOW
    INFO = Foreground.GREEN
    DEBUG = Foreground.BLUE
    CRITICAL = Foreground.CYAN
    ERROR = Foreground.RED


class Mode:
    ORIGIN = "0"
    BOLD = "1"
    BLUR = "2"
    ITALIC = "3"
    UNDERLINE = "4"
    SLOWLY_BLINK = "5"
    BLINK = "6"
    INVERT = "7"

    DEBUG = ORIGIN
    WARNING = ORIGIN
    INFO = ORIGIN
    CRITICAL = ORIGIN
    ERROR = ORIGIN


_fmt = (
    "%(asctime)s "
    "[%(levelname)s]"
    # "[%(name)s]"
    # "(%(filename)s,%(lineno)s)"
    " | %(message)s"
)
_datefmt = "%Y-%m-%d %H:%M:%S"


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt, use_color=True, **kwargs):
        if fmt is None:
            fmt = _fmt
        super().__init__(fmt, **kwargs)
        self.use_color = use_color

    def format(self, record):
        if self.use_color:
            levelname = record.levelname
            prefix = f"\033[{getattr(Mode, levelname)};" \
                     f"{getattr(Foreground, levelname)};" \
                     f"{getattr(Background, levelname)}m"
            suffix = f"\033[0m"
            record.levelname = f"{prefix}{levelname}{suffix}"

            # asctime = record.asctime
            # name = record.name
            # filename = record.filename
            # lineno = record.lineno
            # message = record.message
        return super().format(record)


def init_logger(logger: logging.Logger, fmt: str = None):
    handler = logging.StreamHandler()
    init_handler(handler, fmt)
    logger.addHandler(handler)
    return handler


def init_handler(handler: logging.StreamHandler, fmt: str = None):
    handler.setLevel(logging.DEBUG)
    handler.setStream(sys.stdout)
    formatter = ColoredFormatter(
        fmt=fmt,
        use_color=True,
        datefmt=_datefmt
    )
    handler.setFormatter(formatter)
    return handler


def set_logger(name: str = None):
    init_logger(logging.getLogger(name))


def get_logger(name: str = None):
    logger = logging.getLogger(name)
    init_logger(logger)
    return logger
