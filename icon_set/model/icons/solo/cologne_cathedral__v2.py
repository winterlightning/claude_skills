# Variant of cologne-cathedral; parent file remains unchanged.
"""Cologne Cathedral. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07f608bf-07ea-53df-b369-c2c46c926459'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/cologne cathedral_07f608bf-07ea-53df-b369-c2c46c926459.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'cologne-cathedral-v2'
    variant_of = 'cologne-cathedral'
    variant_label = 'Line door'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('cologne', 'cathedral', 'germany', 'church', 'spire', 'gothic', 'landmark', 'religion')

    def build(self):
        self.add_polyline('outline', (2, 46), (2, 23), (9, 14), (16, 23), (16, 31), (27, 23), (36, 31), (36, 35), (46, 39), (46, 46), (32, 46), (28, 46), (24, 46), closed=True)
        self.add_polyline('cross-stem', (9, 2), (9, 6), (9, 14), closed=False)
        self.add_polyline('cross-bar', (5, 6), (9, 6), (13, 6), closed=False)
        self.relate('connect', 'cross-stem', 'cross-bar')
        self.relate('connect', 'cross-stem', 'outline')
        self.add_polyline('tower', (2, 23), (16, 23), (16, 46), closed=False)
        self.relate('connect', 'tower', 'outline')
        self.add_line('door', (28, 46), (28, 38))
        self.relate('connect', 'door', 'outline')
