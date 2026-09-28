'Squirrel: smooth full tail and rounded head/haunch retain the sitting pose without the overlapping crown wedge.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4582abe5-3297-4fa0-961e-cfe5747d887e'
SOURCE_PATH = 'pictographic-primitives/animals/squirrel_4582abe5-3297-4fa0-961e-cfe5747d887e.svg'
AUTHOR = 'gpt-6'


class Squirrel(Solo48):
    icon_id = 'squirrel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('squirrel', 'tail', 'bushy', 'rodent', 'nut', 'tree', 'animal', 'wildlife')

    def build(self) -> None:
        # Broad tail and rounded haunch; a smooth head avoids the old small overlapping ear wedge.
        self.add_bezier('tail-top',(6,16),((6,10),(8,6),(14,6)),((20,6),(22,10),(22,16)),((22,21),(20,24),(18,28)))
        self.add_bezier('tail-return',(18,28),((16,33),(20,38),(24,42)))
        self.add_line('base',(24,42),(36,42))
        self.add_bezier('haunch',(36,42),((40,42),(42,39),(42,35)),((42,31),(40,27),(36,26)))
        self.add_bezier('back',(6,16),((6,20),(9,22),(9,26)),((9,30),(6,30),(6,34)),((6,39),(10,42),(16,42)))
        self.add_line('rear-base',(16,42),(24,42))
        self.add_contour('tail','tail-top','tail-return','base','haunch')
        self.add_contour('back-outline','back','rear-base')
        self.relate('connect','tail','back-outline')
        self.add_polyline('neck',(18,28),(30,18),(30,10))
        self.add_arc('ear',(30,10),(38,10),radius_x=4)
        self.add_line('head-top',(38,10),(42,12))
        self.add_bezier('muzzle',(42,12),((42,17),(39,22),(36,26)))
        self.add_contour('head','ear','head-top','muzzle')
        self.relate('connect','head','neck')
        self.relate('connect','tail','head')
        self.relate('connect','tail','neck')
