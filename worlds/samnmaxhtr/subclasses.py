from BaseClasses import Region, Location, Item

class SamAndMaxLocationContainer:
    id: int

    def __init__(self, id: int):
        self.id = id

class SamAndMaxSubLocationContainer(SamAndMaxLocationContainer):
    item: int
    state: int

    def __init__(self, id: int, item: int, state: int):
        super().__init__(id)
        self.item = item
        self.state = state

class SubRegion:
    item: int
    state: int
    name: str
    def __init__(self, name: str, item: int, state: int):
        self.item = item
        self.state = state
        self.name = name

class SamAndMaxItem(Item):
    game = "Sam and Max - Hit the Road"

class SamAndMaxItemContainer:
    name: str
    location: SamAndMaxLocationContainer
    progression: bool
    itemReq: list[int] | None
    locationReq: list[SamAndMaxLocationContainer] | None

    def __init__(self, name: str, location: SamAndMaxLocationContainer, itemReq: list[int] | None = None, locationReq: list[SamAndMaxLocationContainer] | None = None, progression: bool = True):
        self.name = name
        self.location = location
        self.itemReq = itemReq
        self.locationReq = locationReq
        self.progression = progression == True

class SamAndMaxLocation(Location):
    game = "Sam and Max - Hit the Road"

class SamAndMaxRegion(Region):
    id: int

class SamAndMaxRegionContainer:
    name: str
    itemReq: list[int] | None
    locationReq: list[SamAndMaxLocationContainer] | None
    connects: list[SamAndMaxLocationContainer] | None
    hasSubState: bool
    subState: list[SubRegion] | None

    def __init__(self, name: str, itemReq: list[int] | None = None, locationReq: list[SamAndMaxLocationContainer] | None = None, connects: list[SamAndMaxLocationContainer] | None = None, subState: list[SubRegion] | None = None):
        self.name = name
        self.itemReq = itemReq
        self.locationReq = locationReq
        self.connects = connects
        self.subState = subState
        self.hasSubState = subState is not None 

class SubRegionContainer:
    regionId: int
    regionName: str
    SmRegionC: SamAndMaxRegionContainer

    def __init__(self, regionId: int, regionName: str, SmRegionC: SamAndMaxRegionContainer):
        self.regionId = regionId
        self.regionName = regionName
        self.SmRegionC = SmRegionC
        
    