"""Rib Cage Diagram: A central upright line joins two wide shallow curved ribs and ends at a short horizontal base. Generate this component alone; exclude Rounded Square Frame.

Construction: Two shallow curved ribs cross one upright, ending at the source short horizontal foot.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '58c80690-dc34-4d48-a622-ec4aa12c8598'
SOURCE_PATH = 'pictographic-primitives/state/radiology xray_58c80690-dc34-4d48-a622-ec4aa12c8598.svg'
AUTHOR = 'gpt-6'


class RibCageDiagram(Sub32):
    icon_id = 'rib-cage-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('rib', 'cage', 'diagram', 'central', 'upright', 'line', 'joins', 'wide')

    def build(self):
        self.add_line('stem',(16,2),(16,30))
        for name,y in (('upper',6),('lower',18)):
            self.add_arc(name,(2,y),(30,y),radius_x=14,radius_y=4)
            self.relate('connect','stem',name)
        self.add_line('foot',(10,30),(22,30))
        self.relate('connect','stem','foot')
