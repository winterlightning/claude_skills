"""An almond eye surrounds a round iris, retained as a separate source identity. HRECT_L extremes (6,8)-(42,40). Lucide eye: mirrored arcs and iris; no focus frame is present in this supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6627b62c-9a54-43be-8f20-fccd8ae111e8'
SOURCE_PATH = 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'
AUTHOR = 'gpt-6'


class EyeOutlineFocus(Solo48):
    icon_id = 'eye-outline-focus'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('eye', 'view', 'see', 'visibility', 'watch', 'look', 'vision', 'focus')

    def build(self) -> None:
        self.add_arc('lid-top', (6,24), (42,24), radius_x=25, radius_y=40)
        self.add_arc('lid-bottom', (42,24), (6,24), radius_x=25, radius_y=40)
        self.add_contour('lids', 'lid-top', 'lid-bottom', closed=True)
        cx, cy, radius = 24, 24, 6
        self.add_arc('iris-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('iris-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('iris', 'iris-top', 'iris-bottom', closed=True)
