"""Two concentric circular outlines.
Plan: Inner radius reduced to 10 to maintain certified ink clearance. Both complete rings retained. Source stroke weight replaced by the required 4-unit stroke.
Lucide construction references: circle-dot.
Keyshape CIRCLE: radial ink radius 22 about (24,24).
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'c577e0e4-e7f4-48be-941f-09df216731ed'
SOURCE_PATH = 'icon_set/work/todo-references/concentrics circle 1_c577e0e4-e7f4-48be-941f-09df216731ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'concentrics-circle-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('concentrics', 'circle', '1')

    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Concentric definition owns both radii and the common centre.
        for name,radius in [('outer',20),('inner',10)]:
            self.circle(name,24,24,radius)

