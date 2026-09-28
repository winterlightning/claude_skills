"""Two people form a stacked bridge pose, with both heads at the left.

Kept both heads and the two bridge silhouettes; reduced closed limb outlines to strokes.
Source establishes the two-person pose; Lucide person-standing informs the detached circular heads.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e90b7491-c523-516a-bb5e-3f47ddbb4cab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-stacked-bridge/20260927T145855Z-thuan-mac-1/reference/acro yoga pose_e90b7491-c523-516a-bb5e-3f47ddbb4cab.svg'
AUTHOR = 'gpt-6'

class AcroYogaStackedBridge(Solo48):
    icon_id = 'acro-yoga-stacked-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('acro', 'yoga', 'stacked', 'bridge')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self):
        # Two people form a stacked bridge pose, with both heads at the left.
        for label,y in [('upper',13),('lower',31)]:self.circle(label+'-head',12,y,3)
        self.add_arc('upper-bridge',(22,20),(42,20),radius_x=10,radius_y=14)
        self.add_polyline('lower-bridge',(21,42),(21,30),(42,30),(42,42))
        self.add_line('upper-foot',(42,20),(42,30))
        self.add_contour('upper-pose','upper-bridge','upper-foot')
        self.relate('connect','upper-foot','lower-bridge-2')
        self.relate('connect','upper-foot','lower-bridge-3')
