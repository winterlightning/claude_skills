"""Horizontal data streams converge in four smooth mirrored runs.
Reference preserves converging flow; six trails reduced to four for clearance.
Lucide waves-vertical contributes repeated coherent curves; curves owned by mirrored pairs.
HRECT_L reaches (4,8)-(44,40). Horizontal symmetry around y=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13b62964-c7a2-4a7d-95ca-bf8b24156d5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon kinesis real time analytics_13b62964-c7a2-4a7d-95ca-bf8b24156d5d.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'horizontal-converging-data-stream'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Six Converging Stream Lines', 'Horizontal Converging Data Stream']
    keywords = ['stream', 'flow', 'curves', 'convergence', 'data', 'parallel', 'lines']
    def build(self):
        for side in (1,-1):
            for name,start,end in [('outer',8,11),('inner',18,20)]:
                y=lambda v: 24+side*(v-24)
                self.add_bezier(f'{name}-{side}',(4,y(start)),((12,y(end)),(24,y(end)),(44,y(end))))
