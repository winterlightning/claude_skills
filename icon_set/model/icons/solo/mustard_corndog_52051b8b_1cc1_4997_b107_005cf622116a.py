"""Corndog with Mustard Swirl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52051b8b-1cc1-4997-b107-005cf622116a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/corndog_52051b8b-1cc1-4997-b107-005cf622116a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mustard-corndog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('corndog', 'mustard', 'sausage', 'stick', 'snack', 'fast food', 'coating')

    def build(self):
        # Plan: Broad diagonal corndog capsule with one mustard wave and wooden stick. Fine zigzag simplified for clearance. Lucide capsule curves; envelope (6,6)-(42,42).
        self.add_bezier('coat',(6,16),((6,10),(10,6),(16,6)),((24,6),(36,18),(36,26)),((36,29),(35,31),(33,33)),((31,35),(29,36),(26,36)),((18,36),(6,24),(6,16)))
        self.add_contour('coating','coat',closed=True)
        self.add_line('stick',(33,33),(42,42));self.relate('connect','stick','coating')
        self.add_bezier('mustard',(15,15),((15,24),(26,17),(26,26)))
