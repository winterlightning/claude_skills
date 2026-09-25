"""Coiled Garden Water Hose.
Plan: Single smooth hose coil unwinds to a horizontal nozzle. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Nozzle reduced to a straight upper outlet; connector seam and narrow tapered outline omitted. Broad continuous coil retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cf30456-605b-444e-b6dd-fe7af25447e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/watering pipe_0cf30456-605b-444e-b6dd-fe7af25447e4.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'coiled-hose-straight-nozzle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('coiled', 'garden', 'water', 'hose')

    def build(self):

        self.add_bezier('hose',(26,28),((14,32),(11,20),(24,20)),((36,20),(36,40),(24,40)),((12,40),(4,40),(4,26)),((4,12),(12,8),(24,8)))
        self.add_polyline('nozzle',(24,8),(44,8))
        self.relate('connect','hose','nozzle')
