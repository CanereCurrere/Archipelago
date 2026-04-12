from .subclasses import SamAndMaxRegionContainer as SmRegionC, SubRegion, Connection as Con, SubConnection as SubCon

regionIds = {
    1: SmRegionC("Intro", connects=[Con(7)]),
    7: SmRegionC("Office", connects=[Con(8)]),
    8: SmRegionC("Office - Corridor", connects=[Con(9)]),
    9: SmRegionC("Office - Street", connects=[Con(10)]),
    10: SmRegionC("Map", connects=[Con(9), SubCon(12,133,1), SubCon(12,133,2), SubCon(12,133,3), Con(12), Con(15), Con(24), Con(27), Con(35), Con(36), Con(41), Con(42), Con(51), Con(57), Con(58), Con(68)]),

    11: SmRegionC("Snuckeys - Inside", subState=[SubRegion("South", 129, 1), SubRegion("North East", 129, 2), SubRegion("West", 129, 3)]),
    12: SmRegionC("Snuckeys", connects=[SubCon(11,129,1), SubCon(11,129,2), SubCon(11,129,3)], subState=[SubRegion("South", 133, 0), SubRegion("North East", 133, 1), SubRegion("West", 133, 2)]),

    15: SmRegionC("Carnival - Entrance", connects=[Con(16)]),
    16: SmRegionC("Carnival - Bruno Room", itemReq=[95], connects=[Con(17)]),
    17: SmRegionC("Carnival - Cone of Tragedy", connects=[Con(18), Con(20), Con(21)]),
    18: SmRegionC("Carnival - Waka-Mole"),
    #19: SmRegionC("Carnival - Waka-Mole - Broken"),
    20: SmRegionC("Carnival - Trailer", itemReq=[230]),
    21: SmRegionC("Carnival - Tunnel of Love", connects=[Con(22)]),
    22: SmRegionC("Carnival - Tunnel of Love - Ride", itemReq=[1], connects=[Con(23)]),
    23: SmRegionC("Carnival - Tunnel of Love - Doug", itemReq=[63, 221]),

    24: SmRegionC("GatorGolf", itemReq=[210], connects=[Con(25)]),
    25: SmRegionC("GatorGolf - Gater Golf Sam", connects=[Con(26)]),
    26: SmRegionC("GatorGolf - Dunk the Beast", itemReq=[322]),

    27: SmRegionC("Twine", roomReq=[23], connects=[Con(28), SubCon(32,317,1)]),
    28: SmRegionC("Twine - Museum", connects=[Con(29)]),
    29: SmRegionC("Twine - Museum Walls", itemReq=[152, 176, 242]),
    30: SmRegionC("Twine - Lookout", connects=[Con(31), Con(78)]),
    31: SmRegionC("Twine - Lookout - View"),
    32: SmRegionC("Twine - Lookout", connects=[Con(30)], subState=[SubRegion("Entry", 317, 1), SubRegion("Fishcook", 317, 2)]),
    #33: SmRegionC("Twine - Fishcook Transistion 1", connects=[]),
    #34: SmRegionC("Twine - Fishcook Transistion 2", connects=[]),

    35: SmRegionC("World of Fish", itemReq=[176], connects=[Con(73)]),

    36: SmRegionC("Mystery Vortex", connects=[37], roomReq=[26]),
    37: SmRegionC("Mystery Vortex - Doors", connects=[38, 39, 40]),
    38: SmRegionC("Mystery Vortex - Magnets"),
    39: SmRegionC("Mystery Vortex - Shuv Hole"),
    40: SmRegionC("Mystery Vortex - Giftshop"),

    41: SmRegionC("Frog Rock", itemReq=[299], roomReq=[78]),

    42: SmRegionC("Bumpus Mansion", itemReq=[150, 269, 377, 366], roomReq=[41], connects=[43]),  
    43: SmRegionC("Bumpus Mansion - Entrance", connects=[44,45,48]),
    44: SmRegionC("Bumpus Mansion - Animal Gallery", connects=[47]),
    45: SmRegionC("Bumpus Mansion - Badroom"),
    47: SmRegionC("Bumpus Mansion - Bumpusville Stage"),
    48: SmRegionC("Bumpus Mansion - Virtual Reality Equipment", connects=[49]),
    49: SmRegionC("Bumpus Mansion - Virtual Reality", itemReq=[430]),

    51: SmRegionC("Savage Jungle Inn", itemReq=[459], connects=[52]),
    52: SmRegionC("Savage Jungle Inn - Reception", connects=[53]),
    53: SmRegionC("Savage Jungle Inn - Stage", itemReq=[1, 587, 431, 209, 572, 127], connects=[55, 56]),
    54: SmRegionC("Savage Jungle Inn - Pool", connects=[90]),
    55: SmRegionC("Savage Jungle Inn - Statues", connects=[54]),
    56: SmRegionC("Savage Jungle Inn - Kitchen"),

    57: SmRegionC("Celebrity Vegetable Museum", itemReq=[485]),

    58: SmRegionC("Dino Bungee", itemReq=[485], connects=[59, 60]),
    59: SmRegionC("Dino Bungee - Dinos"),
    60: SmRegionC("Dino Bungee - Tarpit Slide", connects=[61]),
    61: SmRegionC("Dino Bungee - Bunjeejumping", connects=[62]),
    62: SmRegionC("Dino Bungee - Bunjeejumping to Tarpit"),

    #66: SmRegionC("Car Bomb - minigame", connects=[]),
    #67: SmRegionC("Black void", connects=[]),
    #68: SmRegionC("Highway - minigame"),
    #70: SmRegionC("Paperdoll Outfits - Right - minigame", connects=[]),
    #71: SmRegionC("Paperdoll Outfits - Center (Sam and Max) - minigame", connects=[]),

    73: SmRegionC("World of Fish - In Fish - Cutscene", itemReq=[1, 298], connects=[SubCon(32,317,2)]),
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
