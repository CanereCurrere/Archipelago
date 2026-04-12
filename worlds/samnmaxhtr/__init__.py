from worlds.AutoWorld import World
from . import SamAndMaxOptions, itemIds, regionIds, regions, items, rules, locations


class SamAndMaxWorld(World):
    """Sam & Max Hit the Road is a graphical adventure game, originally developed and released by LucasArts in 1993 for DOS and in 1995 for Macintosh computers, being their ninth game to use the SCUMM adventure game engine. A Windows version of the game was later developed by Aaron Giles and released in 2002. It follows Sam and Max across a kitsch, tourist trap pastiche of America (featuring such locales as the World's Largest Ball of Twine and the Mystery Vortex) in search of an escaped bigfoot."""
    game = "Sam and Max - Hit the Road"

    options_dataclass = SamAndMaxOptions
    options: SamAndMaxOptions
    
     # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = locations.locations_from_regions(regionIds)
    
    item_name_to_id = {item.name: id for id, item in itemIds.values()}

    # Auch wenn 'Save and Quit' nicht wirklich existiert, ist die Karte dennoch der allgemeine Punkt
    origin_region_name = "Map"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        regions.create_all_locations(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
          
    





# from BaseClasses import Region, ItemClassification
# from subclasses import SamAndMaxItem, SamAndMaxLocation, SamAndMaxRegion
# from .items import ITEM_LIST
# from .locations import LOCATION_LIST
# from typing import Dict, Any

    # topology_present = True
    # base_id = 1000

    # # Build mappings
    # item_name_to_id: Dict[str, int] = {it["ingame_name"]: it["id"] for it in ITEM_LIST}
    # location_name_to_id: Dict[str, int] = {loc[1]: loc[0] for loc in LOCATION_LIST}

    # def create_item(self, name: str) -> SamAndMaxItem:
    #     # All items referenced in rules are progression
    #     return SamAndMaxItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    # def create_regions(self) -> None:
    #     # Create one Region per location (room)
    #     for room_id, name, _, _ in LOCATION_LIST:
    #         region = Region(name, self.player, self.multiworld)
    #         # create a Location object and append to region
    #         loc = SamAndMaxLocation(self.player, name, room_id, region)
    #         region.locations.append(loc)
    #         self.multiworld.regions.append(region)

    # def create_items(self) -> None:
    #     # Add all items to the itempool
    #     for it in ITEM_LIST:
    #         item = self.create_item(it["ingame_name"])
    #         self.multiworld.itempool.append(item)

    # def set_rules(self) -> None:
    #     # Helper to find location object by room name
    #     name_to_location = {loc.name: loc for loc in self.multiworld.get_locations(self.player)}
    #     # Map id -> ingame_name for items
    #     id_to_name = {it["id"]: it["ingame_name"] for it in ITEM_LIST}

    #     for room_id, loc_name, item_reqs, room_reqs in LOCATION_LIST:
    #         loc_obj = name_to_location.get(loc_name)
    #         if loc_obj is None:
    #             continue

    #         # Build rule function
    #         def make_rule(item_reqs, room_reqs):
    #             def rule(state):
    #                 # check item requirements
    #                 if item_reqs:
    #                     if isinstance(item_reqs, list):
    #                         for iid in item_reqs:
    #                             iname = id_to_name.get(iid)
    #                             if iname is None or not state.has(iname, self.player):
    #                                 return False
    #                     else:
    #                         iname = id_to_name.get(item_reqs)
    #                         if iname is None or not state.has(iname, self.player):
    #                             return False
    #                 # check room requirements (other regions reachable)
    #                 if room_reqs:
    #                     # room_reqs can be a single int or list
    #                     reqs = room_reqs if isinstance(room_reqs, list) else [room_reqs]
    #                     for rid in reqs:
    #                         # find room name
    #                         rname = next((r[1] for r in LOCATION_LIST if r[0] == rid), None)
    #                         if rname is None:
    #                             return False
    #                         # register indirect condition so generator rechecks when region becomes reachable
    #                         try:
    #                             self.multiworld.register_indirect_condition(rname, loc_obj.name)
    #                         except Exception:
    #                             # register_indirect_condition may require different args in some AP versions;
    #                             # ignore if not available
    #                             pass
    #                         if not state.can_reach_region(rname):
    #                             return False
    #                 return True
    #             return rule

    #         loc_obj.access_rule = make_rule(item_reqs, room_reqs)

    # def generate_output(self, output_directory: str) -> None:
    #     # No game ROM output for now; placeholder to satisfy API
    #     pass

    # def fill_slot_data(self) -> Dict[str, Any]:
    #     # Minimal slot data
    #     return {
    #         "game": self.game,
    #         "item_name_to_id": self.item_name_to_id,
    #         "location_name_to_id": self.location_name_to_id,
    #     }
