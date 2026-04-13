from .subclasses import SamAndMaxRegionContainer as SmRegionC, SubRegion, SamAndMaxLocationContainer as Loc, SamAndMaxSubLocationContainer as SubLoc

regionIds = {
    1: SmRegionC("Intro", connects=[Loc(7)]),
    7: SmRegionC("Office", connects=[Loc(8)]),
    8: SmRegionC("Office - Corridor", connects=[Loc(9)]),
    9: SmRegionC("Office - Street", connects=[Loc(10)]),
    10: SmRegionC("Map", connects=[Loc(9), SubLoc(12,133,1), SubLoc(12,133,2), SubLoc(12,133,3), Loc(12), Loc(15), Loc(24), Loc(27), Loc(35), Loc(36), Loc(41), Loc(42), Loc(51), Loc(57), Loc(58), Loc(68)]),

    11: SmRegionC("Snuckeys - Inside", subState=[SubRegion("South", 129, 0), SubRegion("North East", 129, 1), SubRegion("West", 129, 2)]),
    12: SmRegionC("Snuckeys", connects=[SubLoc(11,129,0), SubLoc(11,129,1), SubLoc(11,129,2)], subState=[SubRegion("South", 133, 1), SubRegion("North East", 133, 2), SubRegion("West", 133, 3)]),

    15: SmRegionC("Carnival - Entrance", connects=[Loc(16)]),
    16: SmRegionC("Carnival - Bruno Room", itemReq=[95], connects=[Loc(17)]),
    17: SmRegionC("Carnival - Cone of Tragedy", connects=[Loc(18), Loc(20), Loc(21)]),
    18: SmRegionC("Carnival - Waka-Mole"),
    #19: SmRegionC("Carnival - Waka-Mole - Broken"),
    20: SmRegionC("Carnival - Trailer", itemReq=[230]),
    21: SmRegionC("Carnival - Tunnel of Love", connects=[Loc(22)]),
    22: SmRegionC("Carnival - Tunnel of Love - Ride", itemReq=[35], connects=[Loc(23)]),
    23: SmRegionC("Carnival - Tunnel of Love - Doug", itemReq=[63, 221]),

    24: SmRegionC("GatorGolf", itemReq=[210], connects=[Loc(25)]),
    25: SmRegionC("GatorGolf - Gater Golf Sam", connects=[Loc(26)]),
    26: SmRegionC("GatorGolf - Dunk the Beast", itemReq=[322]),

    27: SmRegionC("Twine", locationReq=[Loc(23)], connects=[Loc(28), SubLoc(32,317,1)]),
    28: SmRegionC("Twine - Museum", connects=[Loc(29)]),
    29: SmRegionC("Twine - Museum Walls", itemReq=[152, 176, 242]),
    30: SmRegionC("Twine - Lookout", connects=[Loc(31), Loc(78)]),
    31: SmRegionC("Twine - Lookout - View"),
    32: SmRegionC("Twine - Lookout", connects=[Loc(30)], subState=[SubRegion("Entry", 317, 1), SubRegion("Fishcook", 317, 2)]),
    #33: SmRegionC("Twine - Fishcook Transistion 1", connects=[]),
    #34: SmRegionC("Twine - Fishcook Transistion 2", connects=[]),

    35: SmRegionC("World of Fish", itemReq=[176], connects=[Loc(73)]),

    36: SmRegionC("Mystery Vortex", connects=[Loc(37)], locationReq=[Loc(26)]),
    37: SmRegionC("Mystery Vortex - Doors", connects=[Loc(38), Loc(39), Loc(40)]),
    38: SmRegionC("Mystery Vortex - Magnets"),
    39: SmRegionC("Mystery Vortex - Shuv Hole"),
    40: SmRegionC("Mystery Vortex - Giftshop"),

    41: SmRegionC("Frog Rock", itemReq=[299], locationReq=[Loc(78)]),

    42: SmRegionC("Bumpus Mansion", itemReq=[150, 269, 377, 366], locationReq=[Loc(41)], connects=[Loc(43)]),  
    43: SmRegionC("Bumpus Mansion - Entrance", connects=[Loc(44),Loc(45),Loc(48)]),
    44: SmRegionC("Bumpus Mansion - Animal Gallery", connects=[Loc(47)]),
    45: SmRegionC("Bumpus Mansion - Badroom"),
    47: SmRegionC("Bumpus Mansion - Bumpusville Stage"),
    48: SmRegionC("Bumpus Mansion - Virtual Reality Equipment", connects=[Loc(49)]),
    49: SmRegionC("Bumpus Mansion - Virtual Reality", itemReq=[430]),

    51: SmRegionC("Savage Jungle Inn", itemReq=[459], connects=[Loc(52)]),
    52: SmRegionC("Savage Jungle Inn - Reception", connects=[Loc(53)]),
    53: SmRegionC("Savage Jungle Inn - Stage", itemReq=[35, 587, 431, 209, 572, 127], connects=[Loc(55), Loc(56)]),
    54: SmRegionC("Savage Jungle Inn - Pool", connects=[Loc(90)]),
    55: SmRegionC("Savage Jungle Inn - Statues", connects=[Loc(54)]),
    56: SmRegionC("Savage Jungle Inn - Kitchen"),

    57: SmRegionC("Celebrity Vegetable Museum", itemReq=[485]),

    58: SmRegionC("Dino Bungee", itemReq=[485], connects=[Loc(59), Loc(60)]),
    59: SmRegionC("Dino Bungee - Dinos"),
    60: SmRegionC("Dino Bungee - Tarpit Slide", connects=[Loc(61)]),
    61: SmRegionC("Dino Bungee - Bunjeejumping", connects=[Loc(62)]),
    62: SmRegionC("Dino Bungee - Bunjeejumping to Tarpit"),

    #66: SmRegionC("Car Bomb - minigame", connects=[]),
    #67: SmRegionC("Black void", connects=[]),
    68: SmRegionC("Highway - minigame"),
    #70: SmRegionC("Paperdoll Outfits - Right - minigame", connects=[]),
    #71: SmRegionC("Paperdoll Outfits - Center (Sam and Max) - minigame", connects=[]),

    73: SmRegionC("World of Fish - In Fish - Cutscene", itemReq=[35, 298], connects=[SubLoc(32,317,2)]),
    #76: SmRegionC("Carnival - Bruno Room - Cutscene", connects=[]),
    #77: SmRegionC("Into Credits", connects=[]),
    78: SmRegionC("Twine - Lookout View - With Stone", itemReq=[178]),
    
    #79: SmRegionC("Mystery Vortex - Vortex Machine - Cutscene", connects=[]),
    #83: SmRegionC("Coulds - Cutscene", connects=[]),
    #84: SmRegionC("WaxMe - Cutscene", connects=[]),
    #85: SmRegionC("Dino Bungee - Tooth - Cutscene", connects=[]),
    #86: SmRegionC("Savage Jungle Inn - Trees - Cutscene", connects=[]),
    #87: SmRegionC("Savage Jungle Inn - Trees - Cutscene", connects=[]),
    #88: SmRegionC("Savage Jungle Inn - Trees - Cutscene", connects=[]),
    #89: SmRegionC("Savage Jungle Inn - Trees - Cutscene", connects=[]),

    90: SmRegionC("End Game Credit", itemReq=[272, 496, 530, 428, 57, 548]),

    #91: SmRegionC("Paperdoll Outfits - Left - minigame", connects=[]),
    #92: SmRegionC("Bumpus Mansion - Hairs - Cutscene", connects=[]),
}
