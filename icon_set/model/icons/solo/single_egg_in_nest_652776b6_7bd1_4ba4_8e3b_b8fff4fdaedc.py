"""One egg rising from a deep rounded nest. HRECT_L envelope: egg top8, nest sides4/44 and bottom40. Shared symmetry x24 owns egg and bowl. Lucide egg supplies broad lower egg with narrowing smooth crown; source supplies the natural egg-in-nest arrangement. Omit redundant rim band and opening ellipse."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '652776b6-7bd1-4ba4-8e3b-b8fff4fdaedc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/nestmate_652776b6-7bd1-4ba4-8e3b-b8fff4fdaedc.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'single-egg-in-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = []
    keywords = ['egg', 'nest', 'bird', 'nature', 'nesting', 'wildlife']
    def build(self):
        self.add_bezier('egg',(14,24),((14,16),(19,8),(24,8)),((29,8),(34,16),(34,24)))
        self.add_polyline('rim',(4,24),(14,24),(34,24),(44,24))
        self.add_arc('bowl-left',(4,24),(24,40),radius_x=20,radius_y=16,sweep=False)
        self.add_arc('bowl-right',(24,40),(44,24),radius_x=20,radius_y=16,sweep=False)
        self.add_contour('bowl','bowl-left','bowl-right')
        self.relate('connect','egg','rim')
        self.relate('connect','rim','bowl')
