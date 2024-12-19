from .start_handlers import register_handlers as register_start_handlers
from .text_handlers import register_handlers as register_text_handlers

def register_handlers(dp):
    register_start_handlers(dp)
    register_text_handlers(dp)
