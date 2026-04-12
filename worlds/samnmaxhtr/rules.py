from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SamAndMaxWorld

from worlds.generic.Rules import set_rule
from .itemIds import itemIds

def set_all_rules(world: SamAndMaxWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: SamAndMaxWorld) -> None:
    for smItem in itemIds.values():

        req: list[str] | None = None
            
        if smItem.itemReq is not None and smItem.roomReq is not None:
            req = [itemIds[x].name for x in smItem.itemReq]
            req += [itemIds[x].name for x in smItem.roomReq]
        elif smItem.itemReq is not None:
            req = [itemIds[x].name for x in smItem.itemReq]
        elif smItem.roomReq is not None:
            req = [itemIds[x].name for x in smItem.roomReq]

        if req is None:
            continue

        location = world.get_location(smItem.name)

        if req.count == 1:
            set_rule(location, lambda state: state.has(req[0], world.player))
        else:
           set_rule(location, lambda state: state.has_all(req, world.player))
    
def set_completion_condition(world: SamAndMaxWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("End Game Credit", world.player)
