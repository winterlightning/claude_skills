# Review candidate; original preserved.
"""Cologne Cathedral with a single vertical doorway mark. SQUARE preserves the landmark silhouette; rectangular doorway removed per feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07f608bf-07ea-53df-b369-c2c46c926459'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/cologne cathedral_07f608bf-07ea-53df-b369-c2c46c926459.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'cologne-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('cologne', 'cathedral', 'germany', 'church', 'spire', 'gothic', 'landmark', 'religion')

    def build(self):
        """Opening repair: Lowered the tower crossbeam to enlarge the spire opening; preserved the outer silhouette."""
        self.add_polyline('outline', (6, 42), (6, 27), (6, 23), (9, 14), (16, 23), (16, 27), (16, 31), (27, 23), (36, 31), (36, 35), (42, 39), (42, 42), (28, 42), closed=True)
        self.add_polyline('cross-stem', (9, 6), (9, 6), (9, 14), closed=False)
        self.add_polyline('cross-bar', (6, 6), (9, 6), (13, 6), closed=False)
        self.relate('connect', 'cross-stem', 'cross-bar')
        self.relate('connect', 'cross-stem', 'outline')
        self.add_polyline('tower', (6, 27), (16, 27), (16, 42), closed=False)
        self.relate('connect', 'tower', 'outline')
        self.add_line('door', (28, 42), (28, 38))
        self.relate('connect', 'door', 'outline')
