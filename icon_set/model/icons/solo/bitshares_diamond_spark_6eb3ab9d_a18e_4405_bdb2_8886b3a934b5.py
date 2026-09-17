"""Sparkling Diamond BitShares Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eb3ab9d-a18e-4405-bdb2-8886b3a934b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto bitshares_6eb3ab9d-a18e-4405-bdb2-8886b3a934b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitshares-diamond-spark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/finance'
    aliases = ()
    keywords = ('bitshares', 'diamond', 'spark', 'logo', 'cryptocurrency', 'gem', 'glint')

    def build(self):
        # Plan: Slanted diamond plus six intrinsic glints of the supplied emblem. Deliberately asymmetric. No useful exact Lucide match. Bounds (6,6)-(42,42).
        self.add_polyline('diamond',(6,6),(20,14),(20,26),(6,18),closed=True)
        for i,(a,b) in enumerate([((29,17),(33,13)),((36,25),(42,25)),((36,35),(40,39)),((27,38),(27,42)),((17,37),(13,41)),((8,30),(6,32))]):
            self.add_line(f'glint-{i}',a,b)
