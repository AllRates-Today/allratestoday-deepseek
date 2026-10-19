"""Plug real-time currency exchange rates into DeepSeek via tool calling."""

from .agent import DeepSeekCurrencyAgent
from .client import AllRatesTodayClient, AllRatesTodayError
from .tools import TOOLS, dispatch_tool

__all__ = [
    "AllRatesTodayClient",
    "AllRatesTodayError",
    "TOOLS",
    "dispatch_tool",
    "DeepSeekCurrencyAgent",
]
__version__ = "0.2.5"
