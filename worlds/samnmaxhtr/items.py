from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SamAndMaxWorld

from BaseClasses import Item, ItemClassification
from .itemIds import itemIds

class SamAndMaxItem(Item):
    game = "Sam and Max - Hit the Road"

def create_item_from_name(world: SamAndMaxWorld, name: str) -> SamAndMaxItem:
    id, item = next((id,x) for id, x in itemIds.items() if x.name == name)
    
    classification = ItemClassification.progression if item.progression else ItemClassification.filler
    
    return SamAndMaxItem(name, classification=classification, code=id, player=world.player)

def create_all_items(world: SamAndMaxWorld) -> None:
    for itemId, smItem in itemIds.items():

        if itemId == 35 and world.options.start_without_max.value == 0:
            continue

        if itemId == 299 and world.options.include_wires.value == 0:
            continue

        if (itemId == 116 or itemId == 117 or itemId == 128) and world.options.include_minigames.value == 0:
            continue
        
        item = world.create_item(smItem.name)
        world.multiworld.itempool += item