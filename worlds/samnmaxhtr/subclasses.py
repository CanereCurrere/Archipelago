from BaseClasses import Region, Location, Item

class Connection:
    id: int

    def __init__(self, id: int):
        self.id = id

class SubConnection(Connection):
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
    roomId: int
    progression: bool
    itemReq: list[int] | None
    roomReq: list[int] | None

    def __init__(self, name: str, roomId: int, itemReq: list[int] | None = None, roomReq: list[int] | None = None, progression: bool = True):
        self.name = name
        self.roomId = roomId
        self.itemReq = itemReq
        self.roomReq = roomReq
        self.progression = progression == True

class SamAndMaxLocation(Location):
    game = "Sam and Max - Hit the Road"

class SamAndMaxRegion(Region):
    id: int

class SamAndMaxRegionContainer:
    name: str
    itemReq: list[int] | None
    roomReq: list[int] | None
    connects: list[Connection] | None
    hasSubState: bool
    subState: list[SubRegion] | None

    def __init__(self, name: str, itemReq: list[int] | None = None, roomReq: list[int] | None = None, connects: list[Connection] | None = None, subState: list[SubRegion] | None = None):
        self.name = name
        self.itemReq = itemReq
        self.roomReq = roomReq
        self.connects = connects
        self.subState = subState
        self.hasSubState = subState is not None 

    