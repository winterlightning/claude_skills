"""Fork Plate and Knife."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28a45b81-4d2d-59c4-aee6-627238431d00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/restaurant eating set_28a45b81-4d2d-59c4-aee6-627238431d00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plate-between-fork-and-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('plate', 'fork', 'knife', 'table setting', 'dining', 'cutlery', 'meal')

    def build(self):
        # Plan: Table setting with small circular plate between upright cutlery. Lucide utensils; fork reduced to two tines to fit the natural three-object group. Envelope (6,6)-(42,42). Narrow knife blade reduced to an open cutting edge.
        self.add_polyline('fork',(6,6),(6,14),(10,18),(14,14),(14,6))
        self.add_line('fork-shaft',(10,18),(10,42));self.relate('connect','fork-shaft','fork')
        self.add_arc('plate-t',(18,29),(30,29),radius_x=6);self.add_arc('plate-b',(30,29),(18,29),radius_x=6)
        self.add_contour('plate','plate-t','plate-b',closed=True)

        self.add_bezier('knife-edge',(42,6),((38,12),(38,20),(38,26)))
        self.add_polyline('knife-handle',(38,26),(42,26),(42,42));self.relate('connect','knife-edge','knife-handle')
