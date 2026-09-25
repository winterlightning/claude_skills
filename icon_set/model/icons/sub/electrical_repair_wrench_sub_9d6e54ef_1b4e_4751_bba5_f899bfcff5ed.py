"""Electrical Repair Wrench: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9d6e54ef-1b4e-4751-bba5-f899bfcff5ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/flash wrench_9d6e54ef-1b4e-4751-bba5-f899bfcff5ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'electrical-repair-wrench-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):

        # One open wrench and the lightning-shaped continuation of its shaft.
        # Preserve both breaks. Lucide wrench informed the curved open jaw.
        self.add_bezier('heel', (5,24), ((3,25),(2,23),(2,22)),((2,21),(2,21),(3,20)))
        self.add_line('shaft-left', (3,20), (13,10))
        self.add_bezier('head-outer', (13,10), ((10,4),(16,2),(22,2)))
        self.add_line('jaw-upper', (22,2), (17,7))
        self.add_bezier('jaw-inner', (17,7), ((18,10),(21,12),(24,12)))
        self.add_line('jaw-lower', (24,12), (30,6))
        self.add_bezier('head-right', (30,6), ((30,12),(29,14),(25,15)))
        self.add_contour('wrench','heel','shaft-left','head-outer','jaw-upper','jaw-inner','jaw-lower','head-right')
        self.add_polyline('lightning', (19,20),(12,24),(26,24),(20,30))

