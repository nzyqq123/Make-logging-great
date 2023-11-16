import logging

from logger import get_logger, init_logger, set_logger


def test(log: logging.Logger = None):
    log.setLevel(logging.DEBUG)
    log.info(f"I am {log.name}")
    log.debug("DEBUG")
    log.info("INFO")
    log.warning("WARNING")
    log.error("ERROR")
    log.critical("CRITICAL")


if __name__ == '__main__':
    log1 = get_logger()
    test(log1)
    log1.handlers.pop()

    # if you have logger already
    log2 = logging.getLogger("mylog2")
    set_logger("mylog2")
    test(log2)
    log2.handlers.pop()

    # or you can do
    log3 = logging.getLogger("mylog3")
    fmt = (
        "%(asctime)s "
        "[%(levelname)s]"
        # "[%(name)s]"
        # "(%(filename)s,%(lineno)s)"
        " | %(message)s"
    )
    init_logger(log3, fmt)
    test(log3)
    log3.handlers.pop()
