import logging
from rich.logging import RichHandler
from rich.console import Console

console = Console()

def get_logger(name: str) -> logging.Logger:
    """Configures and returns a logger with Rich formatting."""
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, console=console, markup=True)]
    )
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
