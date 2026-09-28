"""Stacked Gardening Pots.
Plan: Two nested pots with broad thick rims and tapered walls. Extrema (8,4)-(40,44).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Corner rounding reduced to short tapered walls; both thick rims retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fda9965-ed09-59ed-8a23-a86ede63c20c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/gardening pots_2fda9965-ed09-59ed-8a23-a86ede63c20c.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'two-stacked-garden-pots'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('stacked', 'gardening', 'pots')

    def build(self):

        self.add_polyline('rim-top',(8,4),(40,4),(40,12),(36,12),(12,12),(8,12),(8,4))
        self.add_polyline('walls-top',(12,12),(14,24));self.relate('connect','walls-top','rim-top')
        self.add_line('wall-right',(36,12),(34,24));self.relate('connect','wall-right','rim-top')
        self.add_polyline('rim-low',(8,24),(14,24),(34,24),(40,24),(40,32),(36,32),(12,32),(8,32),(8,24))
        self.relate('connect','rim-low','walls-top');self.relate('connect','rim-low','wall-right')
        self.add_polyline('base',(12,32),(16,44),(32,44),(36,32));self.relate('connect','base','rim-low')
