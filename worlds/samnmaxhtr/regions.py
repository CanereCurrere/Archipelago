from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import SamAndMaxWorld

from .subclasses import SamAndMaxRegion, SamAndMaxSubLocationContainer as SubLoc, SubRegionContainer as SmSubRegionC
from .regionIds import regionIds
from .itemIds import itemIds

def create_and_connect_regions(world: SamAndMaxWorld) -> None:
    create_all_regions(world)
    connect_regions(world)
	
def create_all_regions(world: SamAndMaxWorld) -> None:
    regions: list[SamAndMaxRegion] = []

    for region_id, region in regionIds.items():
        base_name = region.name

        if region.subState is not None:
            for sub in region.subState:
                # zusammengesetzte ID als String zusammenfügen und in int umwandeln
                # Beispiel: region_id=12, sub.item=133, sub.state=0 -> "121330" -> 121330
                composite_id = int(f"{region_id}{sub.item}{sub.state}")
                composed_name = f"{base_name} - {sub.name}"

                regions.append(SamAndMaxRegion(composed_name, world.player, world.multiworld))
        else:
            regions.append(SamAndMaxRegion(base_name, world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: SamAndMaxWorld) -> None:

    regions: list[SmSubRegionC] = []
    
    for smRegionId, smRegion in regionIds.items():
        if smRegion.subState is not None:
            for sub in smRegion.subState:
                composite_id = int(f"{smRegionId}{sub.item}{sub.state}")
                composed_name = f"{smRegion.name} - {sub.name}"

                regions.append(SmSubRegionC(composite_id, composed_name, smRegion))
        else:
            regions.append(SmSubRegionC(smRegionId, smRegion.name, smRegion))

    for subRegionC in regions:

        regionFromWorld = world.get_region(subRegionC.regionName)

        if subRegionC.SmRegionC.connects is None:
            continue

        for connection in subRegionC.SmRegionC.connects:
            destName: str
            if isinstance(connection, SubLoc):
                connectedRegion = regionIds[connection.id]
                subName = next(x.name for x in connectedRegion.subState if x.item == connection.item and x.state == connection.state)
                destName = f"{connectedRegion.name} - {subName}"
            else:
                destName = regionIds[connection.id].name

            destinationRegion = SamAndMaxRegion(destName, world.player, world.multiworld)
            connectionName = f"'{subRegionC.regionName}' to '{destName}'"

            req: list[str] | None = None
            
            # if subRegionC.SmRegionC.itemReq is not None and subRegionC.SmRegionC.locationReq is not None:
            #     req = [itemIds[x].name for x in subRegionC.SmRegionC.itemReq]
            #     req += [regionIds[x.id].name for x in subRegionC.SmRegionC.locationReq]
            # elif subRegionC.SmRegionC.itemReq is not None:
            #     req = [itemIds[x].name for x in subRegionC.SmRegionC.itemReq]
            # elif subRegionC.SmRegionC.locationReq is not None:
            #     req = [regionIds[x.id].name for x in subRegionC.SmRegionC.locationReq]

            
            if subRegionC.SmRegionC.itemReq is not None and subRegionC.SmRegionC.locationReq is not None:
                req = [itemIds[x].name for x in subRegionC.SmRegionC.itemReq]
                
                for locReq in subRegionC.SmRegionC.locationReq:
                    regionById = regionIds[locReq.id]
                    name = regionById.name
                    if isinstance(locReq, SubLoc):
                        subName = next(x.name for x in regionById.subState if x.item == locReq.item and x.state == locReq.state)
                        name += f" - {subName}"

                    req.append(name)

            elif subRegionC.SmRegionC.itemReq is not None:
                req = [itemIds[x].name for x in subRegionC.SmRegionC.itemReq]
            elif subRegionC.SmRegionC.locationReq is not None:
                req = []
                for locReq in subRegionC.SmRegionC.locationReq:
                    regionById = regionIds[locReq.id]
                    name = regionById.name
                    if isinstance(locReq, SubLoc):
                        subName = next(x.name for x in regionById.subState if x.item == locReq.item and x.state == locReq.state)
                        name += f" - {subName}"

                    req.append(name)

            if req is None:
                regionFromWorld.connect(destinationRegion, connectionName)
            elif req.count == 1:
                regionFromWorld.connect(destinationRegion, connectionName, lambda state: state.has(req[0], world.player))
            else:
                regionFromWorld.connect(destinationRegion, connectionName, lambda state: state.has_all(req, world.player))