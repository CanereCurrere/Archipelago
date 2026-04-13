from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import SamAndMaxWorld

from typing import Dict
from BaseClasses import Location
from .subclasses import SamAndMaxRegionContainer as SmRegionC, SubRegionContainer as SmSubRegionC, SamAndMaxSubLocationContainer as SubLoc
from .regionIds import regionIds
from .itemIds import itemIds

import logging

def locations_from_regions(regions: Dict[int, SmRegionC]) -> Dict[int, str]:
    name_to_id: Dict[str, int] = {}

    for region_id, region in regions.items():
        base_name = region.name

        # Falls SubRegions vorhanden sind: für jede SubRegion einen Eintrag erzeugen
        if region.subState is not None:
            for sub in region.subState:
                # zusammengesetzte ID als String zusammenfügen und in int umwandeln
                # Beispiel: region_id=12, sub.item=133, sub.state=0 -> "121330" -> 121330
                composite_id = int(f"{region_id}{sub.item}{sub.state}")
                composed_name = f"{base_name} - {sub.name}"

                name_to_id[composed_name] = composite_id
        else:
            # normale Region ohne SubState: Name -> region_id
            name_to_id[base_name] = region_id
            
    return name_to_id

def create_all_locations(world: SamAndMaxWorld) -> None:
    create_regular_locations(world)
    #create_events(world)

def create_regular_locations(world: SamAndMaxWorld) -> None:
    logger = logging.getLogger(__name__)
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    for itemId, smItem in itemIds.items():

        if itemId == 35 and world.options.start_without_max.value == 0:
            continue

        if itemId == 299 and world.options.include_wires.value == 0:
            continue

        if (itemId == 116 or itemId == 117 or itemId == 128) and world.options.include_minigames.value == 0:
            continue

        regionById = regionIds[smItem.location.id]
        regionName = regionById.name

        if isinstance(smItem.location, SubLoc):
            subName = next(x.name for x in regionById.subState if x.item == smItem.location.item and x.state == smItem.location.state)
            regionName += f" - {subName}"
            

        region = world.get_region(regionName)
        
        location = SamAndMaxLocation(world.player, smItem.name, itemId, region)
        logger.info(f"Add Location: {location.name}")
        region.locations.append(location)

class SamAndMaxLocation(Location):
    game = "Sam and Max - Hit the Road"

