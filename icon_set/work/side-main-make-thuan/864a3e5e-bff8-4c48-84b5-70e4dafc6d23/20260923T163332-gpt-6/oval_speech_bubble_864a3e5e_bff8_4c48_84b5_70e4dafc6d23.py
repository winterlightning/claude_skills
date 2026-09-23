from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '864a3e5e-bff8-4c48-84b5-70e4dafc6d23'
SOURCE_PATH = 'pictographic-primitives/container/message bubble circle_864a3e5e-bff8-4c48-84b5-70e4dafc6d23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """An empty oval speech bubble with a lower-left pointed tail.

    Plan: One closed ellipse-derived contour, center24,23 rx20 ry15. Exact 3-4-5 ellipse points bound the lower-left tail interruption. Oval symmetric apart from the source tail.
    References: Source oval and lower-left tail; Lucide message-circle original and atomic-debug informed single connected outline with deliberate tail corners.
    """
    icon_id = 'oval-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/other'
    aliases = ()
    keywords = ()

    def build(self):
        cx, cy, rx, ry = 24, 23, 20, 15
        self.add_arc("upper", (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc("lower-right", (cx+rx,cy), (cx,cy+ry), radius_x=rx, radius_y=ry)
        self.add_arc("lower", (cx,cy+ry), (12,35), radius_x=rx, radius_y=ry)
        self.add_line("tail-bottom", (12,35), (6,40))
        self.add_line("tail-left", (6,40), (8,32))
        self.add_arc("lower-left", (8,32), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour("bubble", "upper", "lower-right", "lower", "tail-bottom", "tail-left", "lower-left", closed=True)
