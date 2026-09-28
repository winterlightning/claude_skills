"""Festive Party Bunting Flags.
Plan: Two offset single-pennant cords and a pair of confetti marks. Centerline extremes (4,8)-(44,40).
Reference: No useful local Lucide bunting match; repeated pennant definition.
Reduction: Five flags reduced to two and confetti reduced to two bends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2809250-1b46-4c46-822c-17af67873899'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party decoration_d2809250-1b46-4c46-822c-17af67873899.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'festive-bunting-confetti'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('festive', 'party', 'bunting', 'flags')

    def build(self):

        self.add_polyline('upper-cord',(4,8),(22,8),(30,8))
        self.add_polyline('upper-flag',(4,8),(13,20),(22,8))
        self.relate('connect','upper-cord','upper-flag')
        self.add_polyline('lower-cord',(18,28),(26,28),(44,28))
        self.add_polyline('lower-flag',(26,28),(35,40),(44,28))
        self.relate('connect','lower-cord','lower-flag')
        self.add_polyline('confetti-left',(4,33),(4,37),(8,37))
        self.add_polyline('confetti-right',(40,8),(40,12),(44,12))
