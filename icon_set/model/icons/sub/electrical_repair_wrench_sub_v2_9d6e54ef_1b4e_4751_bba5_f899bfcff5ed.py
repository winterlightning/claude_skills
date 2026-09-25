# Variant of electrical-repair-wrench-sub; parent file remains unchanged.
"""Electrical Repair Wrench: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9d6e54ef-1b4e-4751-bba5-f899bfcff5ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/flash wrench_9d6e54ef-1b4e-4751-bba5-f899bfcff5ed.svg'
AUTHOR = 'gpt-6'

class DrawingVariant2(Sub32):
    icon_id = 'electrical-repair-wrench-sub-v2'
    variant_of = 'electrical-repair-wrench-sub'
    variant_label = 'Correct diagonal and open wrench jaw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):
        # Exact 45-degree shaft, jaw lips and lightning legs; retain both breaks.
        # The jaw cavity is a coherent diagonal U, not a pinched zigzag.
        self.add_bezier('heel',(5,25),((3,25),(2,24),(2,23)),((2,22),(3,21),(4,20)))
        self.add_line('shaft-left',(4,20),(14,10))
        self.add_bezier('head-outer',(14,10),((12,5),(15,2),(20,2)))
        self.add_line('top',(20,2),(24,2))
        self.add_line('jaw-upper',(24,2),(20,6))
        self.add_bezier('jaw-inner',(20,6),((20,9),(23,12),(26,12)))
        self.add_line('jaw-lower',(26,12),(30,8))
        self.add_bezier('head-right',(30,8),((30,13),(30,15),(27,18)))
        self.add_contour('wrench','heel','shaft-left','head-outer','top','jaw-upper','jaw-inner','jaw-lower','head-right')
        self.add_polyline('lightning',(19,17),(12,24),(24,24),(18,30))
