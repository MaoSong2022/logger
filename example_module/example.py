import logger
log = logger.get_logger(__name__)

def example_function(a: int, b: int) -> int:
    log.debug(f'a={a}, b={b}, output={a+b}')
    return a + b