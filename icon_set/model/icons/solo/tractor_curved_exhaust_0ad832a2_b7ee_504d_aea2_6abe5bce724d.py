"""Agricultural Farm Tractor.
Plan: Right-facing tractor with large rear wheel, small front wheel and tall cab. Extrema (4,8)-(44,40).
Reference: Lucide tractor: unequal wheel circles and angular cab-to-hood transition.
Reduction: Wheel hubs, ground line and close fender omitted; cab style and exhaust distinguish the variants.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ad832a2-b7ee-504d-aea2-6abe5bce724d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/plow_0ad832a2-b7ee-504d-aea2-6abe5bce724d.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'tractor-curved-exhaust'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('agricultural', 'farm', 'tractor')

    def build(self):

        self.add_arc('rear-a',(4,32),(20,32),radius_x=8)
        self.add_arc('rear-b',(20,32),(4,32),radius_x=8)
        self.add_contour('rear','rear-a','rear-b',closed=True)
        self.add_arc('front-a',(34,35),(44,35),radius_x=5)
        self.add_arc('front-b',(44,35),(34,35),radius_x=5)
        self.add_contour('front','front-a','front-b',closed=True)
        self.add_polyline('body',(6,16),(6,8),(22,8),(26,22),(44,22),(44,35))
        self.relate('connect','body','front')

        self.add_line('exhaust',(36,22),(36,12));self.relate('connect','exhaust','body')
        self.add_arc('exhaust-tip',(36,12),(40,8),radius_x=4);self.relate('connect','exhaust','exhaust-tip')
