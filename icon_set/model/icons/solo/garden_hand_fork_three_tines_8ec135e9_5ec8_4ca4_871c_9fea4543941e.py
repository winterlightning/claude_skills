"""Gardening Hand Fork.
Plan: Diagonal garden fork with three equal parallel tines and an angular shoulder. Extrema (6,6)-(42,42).
Reference: Lucide shovel: diagonal handle and shaped working end.
Reduction: Grip reduced to one stroke; three tines and angular spreading shoulder retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ec135e9-5ec8-4ca4-871c-9fea4543941e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/digging fork_8ec135e9-5ec8-4ca4-871c-9fea4543941e.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'garden-hand-fork-three-tines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('gardening', 'hand', 'fork')

    def build(self):

        self.add_line('shaft',(6,6),(24,24))
        self.add_polyline('shoulder',(18,30),(24,24),(30,18))
        self.relate('connect','shoulder','shaft');self.relate('connect','shoulder','middle')
        self.add_polyline('middle',(24,24),(36,36));self.relate('connect','shaft','middle')
        self.add_line('left-tine',(18,30),(30,42))
        self.add_line('right-tine',(30,18),(42,30))
        self.relate('connect','left-tine','shoulder');self.relate('connect','right-tine','shoulder')
