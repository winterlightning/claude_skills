"""Swimming Sperm Cells.

Plan: Three cells share oval-head and S-tail definitions; middle cell is shorter. Bounds (8,4)-(40,44). Intrinsic cell grouping, no modifier. Heads are broad ovals; tail waves alternate arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27aee4c5-ba96-5cb3-b0d5-b5642a6b8a69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pregnancy sperm_27aee4c5-ba96-5cb3-b0d5-b5642a6b8a69.svg'
AUTHOR = 'gpt-6'


class SwimmingSpermCells(Solo48):
    icon_id = 'swimming-sperm-cells'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('swimming', 'sperm', 'cells')

    def build(self):
        for i in range(3):
            y=8+16*i
            cx=34 if i!=1 else 28
            p=f'cell-{i}'
            self.add_arc(p+'-top',(cx-6,y),(cx+6,y),radius_x=6,radius_y=4)
            self.add_arc(p+'-bottom',(cx+6,y),(cx-6,y),radius_x=6,radius_y=4)
            self.add_contour(p+'-head',p+'-top',p+'-bottom',closed=True)
            mid=(8+cx-6)//2
            self.add_arc(p+'-tail-a',(8,y),(mid,y),radius_x=(mid-8)//2,radius_y=2)
            self.add_arc(p+'-tail-b',(mid,y),(cx-6,y),radius_x=(cx-6-mid)//2,radius_y=2,sweep=False)
            self.add_contour(p+'-tail',p+'-tail-a',p+'-tail-b')
            self.relate('connect',p+'-head',p+'-tail')
