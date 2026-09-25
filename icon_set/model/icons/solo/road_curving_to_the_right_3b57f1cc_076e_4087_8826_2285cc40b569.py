'A broad road sweeps from bottom left to upper right with a broken centerline. SQUARE extremes (6,6)-(42,42) preserve the quarter turn. Lucide road contributes separated lane marks within broad road edges; inspected corner-up-right provides the quarter-circle turn principle. Concentric quarter circles share center (42,42), with radii 36 and16. Three separated lane dashes follow the intermediate radius; source many short dashes reduced to three.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '3b57f1cc-076e-4087-8826-2285cc40b569'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/roadway_3b57f1cc-076e-4087-8826-2285cc40b569.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'road-curving-to-the-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Curved Highway Road Path']
    keywords = ['road', 'curving', 'to', 'the', 'right']
    def build(self):
        for name,radius in [('outer-edge',36),('inner-edge',16)]:
            self.add_arc(name,(42-radius,42),(42,42-radius),radius_x=radius)
        self.add_line('lane-bottom',(16,42),(16,38))
        self.add_arc('lane-turn',(22,26),(26,22),radius_x=26)
        self.add_line('lane-top',(38,16),(42,16))
