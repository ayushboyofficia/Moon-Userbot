# modules/help.py
"""
Moon UserBot Help Module
Handles command help functionality and integrates with the main help system
"""

from pyrogram.types import Message
from utils.misc import modules_help, prefix
from utils.scripts import format_module_help

def add_command_help(module_name: str, commands_list: list):
    """
    Adds command help to the global modules_help dictionary
    
    Args:
        module_name: Name of the module
        commands_list: List of tuples with (command, description)
    
    Example:
        add_command_help("example", [
            ("cmd1", "description1"),
            ("cmd2 args", "description2")
        ])
    """
    if module_name not in modules_help:
        modules_help[module_name] = {}
    
    for cmd, desc in commands_list:
        modules_help[module_name][f"{cmd}"] = desc

def get_module_help(module_name: str) -> str:
    """
    Gets formatted help for a specific module
    
    Args:
        module_name: Name of the module to get help for
    
    Returns:
        Formatted help string
    """
    return format_module_help(module_name, prefix)

def generate_full_help() -> dict:
    """
    Returns the complete modules_help dictionary
    
    Returns:
        The global modules_help dictionary
    """
    return modules_help

# Example usage that would work with your existing code
add_command_help("help", [
    ("help [module/command]", "Get help for modules or commands"),
    ("pn", "Next help page"),
    ("pp", "Previous help page"),
    ("pq", "Quit help")
])
