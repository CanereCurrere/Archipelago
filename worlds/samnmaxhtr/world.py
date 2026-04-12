# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

from subclasses import SamAndMaxItem
from items import create_item_from_name

def create_item(self, item: str) -> SamAndMaxItem:
    return create_item_from_name(self, item)