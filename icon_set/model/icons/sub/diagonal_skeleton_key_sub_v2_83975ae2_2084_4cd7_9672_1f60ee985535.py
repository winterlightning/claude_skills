# Variant of diagonal-skeleton-key-sub; parent file remains unchanged.
"""Simple Skeleton Key Symbol: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '83975ae2-2084-4cd7-9672-1f60ee985535'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/key 3_83975ae2-2084-4cd7-9672-1f60ee985535.svg'
AUTHOR = 'gpt-6'

class DrawingVariant2(Sub32):
    icon_id = 'diagonal-skeleton-key-sub-v2'
    variant_of = 'diagonal-skeleton-key-sub'
    variant_label = 'Correct 45-degree shaft and larger circular bow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):
        # One true radius-8 bow; shaft and both teeth use exact 45-degree axes.
        # The diagonal shaft enters the painted ring at its lower-left quadrant.
        self.add_arc('bow-top',(14,10),(30,10),radius_x=8)
        self.add_arc('bow-bottom',(30,10),(14,10),radius_x=8)
        self.add_contour('bow','bow-top','bow-bottom',closed=True)
        self.add_line('shaft',(2,30),(16,16))
        self.relate('connect','shaft','bow')
        for name, x, y in [('tip',6,26),('middle',12,20)]:
            self.add_line(name,(x,y),(x+4,y+4))
            self.relate('connect',name,'shaft')
