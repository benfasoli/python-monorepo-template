import json
import logging
import sys
import traceback
from types import TracebackType

logger = logging.getLogger(__name__)

_prev_excepthook = sys.excepthook


def _on_unhandled_exception(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_traceback: TracebackType | None,
) -> None:
    exc_info = (exc_type, exc_value, exc_traceback)
    logger.critical("Unhandled exception", exc_info=exc_info)
    _prev_excepthook(exc_type, exc_value, exc_traceback)


sys.excepthook = _on_unhandled_exception


def _format_exception(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_traceback: TracebackType | None,
) -> str:
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    return "".join(lines)


class JsonFormatter(logging.Formatter):
    default_time_format = "%Y-%m-%dT%H:%M:%S"
    default_msec_format = "%s.%03dZ"

    def format(self, record: logging.LogRecord) -> str:
        message = record.getMessage()
        if record.exc_info:
            exc_type, exc_value, exc_traceback = record.exc_info
            if exc_type and exc_value:
                message += "\n"
                message += _format_exception(
                    exc_type=exc_type,
                    exc_value=exc_value,
                    exc_traceback=exc_traceback,
                )
        record_dict = {
            "time": self.formatTime(record),
            "severity": record.levelname,
            "message": message,
            "module": record.name,
            "line": record.lineno,
        }
        return json.dumps(record_dict)


def setup_logging(level: str) -> None:
    formatter = JsonFormatter()

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers = [handler]
    root_logger.setLevel(level)
