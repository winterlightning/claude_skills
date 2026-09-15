"""Skull over crossed bones. Lucide skull informs a coherent cranium and jaw; only the two source eye dots are retained, without added teeth or nasal details.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd38fbff-cdfa-4f34-a23b-de43ccc998cb'
SOURCE_PATH = 'pictographic-primitives/symbol/skull crossbones_bd38fbff-cdfa-4f34-a23b-de43ccc998cb.svg'
AUTHOR = 'gpt-6'


class SkullCrossbones(Solo48):
    icon_id = 'skull-crossbones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('skull', 'crossbones', 'poison', 'danger', 'toxic', 'pirate', 'death', 'hazard')

    def build(self) -> None:

        self.add_arc('cranium',(10,16),(38,16),radius_x=14,radius_y=10)
        self.add_arc('cheek-right',(38,16),(30,24),radius_x=8)
        for j,(a,b) in enumerate(zip([(30,24),(30,26),(18,26)],[(30,26),(18,26),(18,24)]),1):self.add_line('jaw-'+str(j),a,b)
        self.add_arc('cheek-left',(18,24),(10,16),radius_x=8)
        self.add_contour('skull','cranium','cheek-right','jaw-1','jaw-2','jaw-3','cheek-left',closed=True)
        for x in (19,29):self.add_dot('eye-'+str(x),(x,16))
        self.add_polyline('bone-down',(6,32),(24,37),(42,42))
        self.add_polyline('bone-up',(6,42),(24,37),(42,32))
        self.relate('connect','bone-down','bone-up')
