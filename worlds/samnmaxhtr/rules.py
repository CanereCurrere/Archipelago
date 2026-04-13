from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import SamAndMaxWorld

from worlds.generic.Rules import set_rule
from .itemIds import itemIds
from .regionIds import regionIds
from .subclasses import SamAndMaxSubLocationContainer as SubLoc

def set_all_rules(world: SamAndMaxWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: SamAndMaxWorld) -> None:
    for itemId, smItem in itemIds.items():

        if itemId == 35 and world.options.start_without_max.value == 0:
            continue

        if itemId == 299 and world.options.include_wires.value == 0:
            continue

        if (itemId == 116 or itemId == 117 or itemId == 128) and world.options.include_minigames.value == 0:
            continue
        
        req: list[str] | None = None
            
        if smItem.itemReq is not None and smItem.locationReq is not None:
            req = [itemIds[x].name for x in smItem.itemReq]
            
            for locReq in smItem.locationReq:
                regionById = regionIds[locReq.id]
                name = regionById.name
                if isinstance(locReq, SubLoc):
                    subName = next(x.name for x in regionById.subState if x.item == locReq.item and x.state == locReq.state)
                    name += f" - {subName}"

                req.append(name)

        elif smItem.itemReq is not None:
            req = [itemIds[x].name for x in smItem.itemReq]
        elif smItem.locationReq is not None:
            req = []
            for locReq in smItem.locationReq:
                regionById = regionIds[locReq.id]
                name = regionById.name
                if isinstance(locReq, SubLoc):
                    subName = next(x.name for x in regionById.subState if x.item == locReq.item and x.state == locReq.state)
                    name += f" - {subName}"

                req.append(name)

        if req is None:
            continue

        location = world.get_location(smItem.name)

        if req.count == 1:
            set_rule(location, lambda state: state.has(req[0], world.player))
        else:
           set_rule(location, lambda state: state.has_all(req, world.player))
    
def set_completion_condition(world: SamAndMaxWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("End Game Credit", world.player)
