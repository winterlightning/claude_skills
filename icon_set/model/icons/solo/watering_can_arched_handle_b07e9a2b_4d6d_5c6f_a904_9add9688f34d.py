"""Garden Watering Can.
Plan: Tapered can body with upper arch, rear loop and diagonal spout. Extrema (4,8)-(44,40).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: Body seam and sprinkler holes omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b07e9a2b-4d6d-5c6f-a904-9add9688f34d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/watering can_b07e9a2b-4d6d-5c6f-a904-9add9688f34d.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'watering-can-arched-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('garden', 'watering', 'can')

    def build(self):

        self.add_polyline('body',(18,22),(36,22),(36,34),(36,38),(36,40),(18,40),(18,30),(18,22))
        self.add_arc('top-handle',(18,22),(36,22),radius_x=9,radius_y=14)
        self.relate('connect','body','top-handle')
        self.add_arc('rear-handle',(36,22),(36,38),radius_x=8,radius_y=8)
        self.relate('connect','body','rear-handle')
        self.add_line('spout',(18,30),(6,18));self.relate('connect','spout','body')
        self.add_polyline('rose',(4,22),(6,18),(8,14));self.relate('connect','spout','rose')
