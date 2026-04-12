from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SamAndMaxWorld

from .subclasses import SamAndMaxRegion, SubConnection as SubCon
from .regionIds import regionIds
from .itemIds import itemIds

def create_and_connect_regions(world: SamAndMaxWorld) -> None:
    create_all_regions(world)
    connect_regions(world)
	
def create_all_regions(world: SamAndMaxWorld) -> None:
    regions: list[SamAndMaxRegion] = []

    for item in regionIds.values():
        regions.append(SamAndMaxRegion(item.name, world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: SamAndMaxWorld) -> None:
    for smRegion in regionIds.values():

        regionFromWorld = world.get_region(smRegion.name)

        for connection in smRegion.connects:
            destName: str
            if isinstance(connection, SubCon):
                region = regionIds[smRegion]
                subName = next(x.name for x in region.subState if x.item == connection.item and x.state == connection.state)
                destName = f"{region.name} - {subName}"
            else:
                destName = regionIds[smRegion].name

            destinationRegion = SamAndMaxRegion(destName, world.player, world.multiworld)
            connectionName = f"'{smRegion.name}' to '{destName}'"

            req: list[str] | None = None
            
            if smRegion.itemReq is not None and smRegion.roomReq is not None:
                req = [itemIds[x].name for x in smRegion.itemReq]
                req += [regionIds[x].name for x in smRegion.roomReq]
            elif smRegion.itemReq is not None:
                req = [itemIds[x].name for x in smRegion.itemReq]
            elif smRegion.roomReq is not None:
                req = [regionIds[x].name for x in smRegion.roomReq]

            if req is None:
                regionFromWorld.connect(destinationRegion, connectionName)
            elif req.count == 1:
                regionFromWorld.connect(destinationRegion, connectionName, lambda state: state.has(req[0], world.player))
            else:
                regionFromWorld.connect(destinationRegion, connectionName, lambda state: state.has_all(req, world.player))