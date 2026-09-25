"""Vector Graphic Pen Tool.

Symbol plan: Symmetric fountain nib with circular shoulders, two open holder arms, a circular breather and integral slit. Lucide pen-tool informs breather/slit topology. Omit short duplicate neck.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '748a2816-d5d6-4c34-8dfa-866767da3284'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors pen_748a2816-d5d6-4c34-8dfa-866767da3284.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-downward-pen-nib-with-open-holder'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vector', 'graphic', 'pen', 'tool')

    def build(self):
        a=24
        self.add_line('top',(16,12),(32,12))
        self.add_arc('shoulder-right',(32,12),(40,20),radius_x=8)
        self.add_line('edge-right',(40,20),(a,44))
        self.add_line('edge-left',(a,44),(8,20))
        self.add_arc('shoulder-left',(8,20),(16,12),radius_x=8)
        self.add_contour('nib','top','shoulder-right','edge-right','edge-left','shoulder-left',closed=True)
        self.add_line('holder-left',(14,4),(16,12));self.add_line('holder-right',(32,12),(34,4))
        for part in ['holder-left','holder-right']:self.relate('connect',part,'nib')
        self.circle('breather',a,24,3)
        self.add_line('slit',(a,27),(a,44))
        self.relate('connect','slit','breather');self.relate('connect','slit','nib')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)
