"""SQUARE (6,6)-(42,42) centerlines. Preserve tall left tower, central gable and low right annex. Remove the small tower-roof division and window marks; doorway becomes a single vertical mark consistent with the existing line-door variants. Deliberate left-to-right descending asymmetry follows the supplied reference.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07f608bf-07ea-53df-b369-c2c46c926459'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/cologne cathedral_07f608bf-07ea-53df-b369-c2c46c926459.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'cologne-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('cologne', 'cathedral', 'germany', 'church', 'spire', 'gothic', 'landmark', 'religion')

    def build(self):
        self.add_polyline('outline',(6,42),(6,24),(12,16),(18,24),(18,30),(28,23),(36,30),(36,33),(42,36),(42,42),(28,42),(18,42),closed=True)
        self.add_polyline('cross-stem',(12,6),(12,9),(12,16))
        self.add_polyline('cross-bar',(8,9),(12,9),(16,9))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','outline')
        self.add_polyline('tower',(18,30),(18,42))
        self.relate('connect','tower','outline')
        self.add_line('door',(28,42),(28,34))
        self.relate('connect','door','outline')
