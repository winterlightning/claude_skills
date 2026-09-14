"""Controls rewind (video), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebe0d398-8e66-5e3c-8648-fb9e091f93f2'
SOURCE_PATH = 'icons-json/video/controls rewind_ebe0d398-8e66-5e3c-8648-fb9e091f93f2.json'
AUTHOR = 'json_to_solo'

class ControlsRewindEbe0d398(Solo48):
    icon_id = 'controls-rewind-ebe0d398'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'rewind', 'video')

    def build(self):
        self.add_line('e0', (39, 4), (33, 8))
        self.add_line('e1', (33, 8), (9, 22))
        self.add_line('e2', (10, 27), (33, 40))
        self.add_line('e3', (40, 41), (40, 6))
        self.add_line('e4', (40, 6), (39, 4))
        self.add_bezier('e5', (9, 22), ((8.595, 22.242), (8, 23.126), (8, 23.579)), ((8, 23.586), (8, 23.593), (8, 23.6)), ((8, 25), (8.594, 26.164), (10, 27)))
        self.add_bezier('e6', (33, 40), ((34.474, 40.882), (36.194, 42.064), (37.589, 43.018)), ((37.971, 43.278), (38.774, 44), (39.323, 44)), ((39.331, 44), (39.34, 44), (39.349, 44)), ((39.394, 43.855), (39.44, 43.7), (39.486, 43.555)), ((39.669, 42.936), (39.977, 42.191), (39.977, 41.545)), ((39.989, 41.455), (39.989, 41.091), (40, 41)))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
