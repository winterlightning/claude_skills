"""A pong ball above a pair of tapered party cups. HRECT_L gives each cup a readable open interior. Cups mirror across x24 with shared taper2 and height16. Source supplies ball and cups; Lucide cup-soda supplies coherent tapered wall construction. Third repeated cup, elliptical rims and flight trails omitted for minimum gaps.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '33939e2c-79ce-4c17-8024-6849438ef6c0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beer pong_33939e2c-79ce-4c17-8024-6849438ef6c0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'beer-pong-cups-and-ball'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Beer Pong Cups and Ball']
    keywords = ['beer pong', 'cups', 'ball', 'game', 'party', 'throw', 'trajectory']

    def build(self):
        for j,x in enumerate((4,28)):
            self.add_polyline(f"cup-{j}",(x,24),(x+16,24),(x+14,40),(x+2,40),closed=True)
        self.add_arc("ball-top",(20,12),(28,12),radius_x=4)
        self.add_arc("ball-bottom",(28,12),(20,12),radius_x=4)
        self.add_contour("ball","ball-top","ball-bottom",closed=True)
