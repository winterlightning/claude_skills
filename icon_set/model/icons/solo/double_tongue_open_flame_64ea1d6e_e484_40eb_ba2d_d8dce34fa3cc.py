"""Fire Flame Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64ea1d6e-e484-40eb-ba2d-d8dce34fa3cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/matches fire_64ea1d6e-e484-40eb-ba2d-d8dce34fa3cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'double-tongue-open-flame'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('fire', 'flame', 'burning', 'heat', 'tongue', 'blaze', 'symbol')

    def build(self):
        # Plan: Broad flame owns three pointed tongues and an open lower inner curl. Lucide flame: smooth rounded bowl. Bounds (6,6)-(42,42).
        self.add_bezier('flame',(18,6),((23,14),(19,22),(16,23)),((13,23),(12,20),(12,17)),((8,21),(6,27),(6,30)),((6,38),(13,42),(24,42)),((35,42),(42,37),(42,29)),((42,26),(42,24),(41,22)),((39,24),(37,25),(34,25)),((34,17),(27,9),(18,6)))
        self.add_contour('outline','flame',closed=True)
        self.add_bezier('inner',(23,33),((24,31),(26,30),(27,29)))
