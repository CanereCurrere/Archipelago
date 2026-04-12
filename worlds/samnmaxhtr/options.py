from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions

class MiniGame(Toggle):
    """Should the Minigames be Part of the Itempool (Junk Items)"""
    display_name = "Include Minigame Items"
    value = True

class Wires(Toggle):
    """Should the Wires from the Twinelookout be an actual Item. This is not normaly the case."""
    display_name = "Include Wire Item"
    value = False

class StartWithoutMax(Toggle):
    """This starts the game in a State, where Max is trapped in the 'Gator Golf - Dunk the Beast' Tank"""
    display_name = "Start without Max"
    value = True

@dataclass
class SamAndMaxOptions(PerGameCommonOptions):
    start_without_max: StartWithoutMax
    include_minigames: MiniGame
    include_wires: Wires
