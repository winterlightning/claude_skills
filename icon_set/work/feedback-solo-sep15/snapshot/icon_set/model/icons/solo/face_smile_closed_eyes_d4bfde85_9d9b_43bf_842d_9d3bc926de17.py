"""A round relaxed face has closed eyes and a U-shaped smile. CIRCLE centerline radius20 about (24,24) fits the circular face. Lucide face-slightly-smiling informs the centered mouth and shared eye dimensions; horizontal closed eyes preserve the supplied expression. No identity-bearing features omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4bfde85-9d9b-43bf-842d-9d3bc926de17'
SOURCE_PATH = 'pictographic-primitives/symbol/face smile_d4bfde85-9d9b-43bf-842d-9d3bc926de17.svg'
AUTHOR = 'gpt-6'


class FaceSmileClosedEyes(Solo48):
    icon_id = 'face-smile-closed-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('smile', 'face', 'happy', 'emoji', 'content', 'relaxed', 'satisfied', 'emotion')

    def build(self) -> None:
        cx, cy, radius = 24, 24, 20
        self.add_arc('face-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('face-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
        axis_x = 24
        for name, x in (('left', 15), ('right', 2*axis_x-18)):
            self.add_line('eye-'+name, (x,19), (x+3,19))
        self.add_arc('smile', (15,29), (33,29), radius_x=9, radius_y=6, sweep=False)
