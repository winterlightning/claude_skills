"""Wave both direction large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a762eac9-ddd8-4577-b896-c37fcc59842c'
SOURCE_PATH = 'icons-json/arrows/wave both direction large head_a762eac9-ddd8-4577-b896-c37fcc59842c.json'
AUTHOR = 'json_to_solo'

class WaveBothDirectionLargeHeadArrows(Solo48):
    icon_id = 'wave-both-direction-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'both', 'direction', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (35, 6), (42, 12))
        self.add_line('e1', (13, 31), (6, 36))
        self.add_line('e2', (13, 42), (6, 36))
        self.add_line('e3', (36, 17), (42, 12))
        self.add_line('e4', (42, 12), (21, 12))
        self.add_line('e5', (22, 23), (25, 23))
        self.add_line('e6', (26, 36), (6, 36))
        self.add_bezier('e7', (21, 12), ((20.583, 12), (19.099, 12.218), (18.682, 12.423)), ((14.198, 14.673), (15.286, 20.858), (19.541, 22.666)), ((20.138, 22.92), (21.337, 23), (22, 23)))
        self.add_bezier('e8', (25, 23), ((28.412, 23), (31.331, 25.874), (31.822, 29.204)), ((32.239, 31.985), (30.545, 34.759), (27.993, 35.855)), ((27.543, 36.044), (26.491, 36), (26, 36)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7', 'e5', 'e8', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
