"""Two people balance with both heads on the right and bent bodies extending left.

Kept the two right-hand heads and curved, stacked bodies; simplified the upper curled limb and thick loops.
Source two-person silhouette; Lucide person-standing informs detached heads, with circular bends for limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5240dbe0-19a2-54d5-b0f7-5cc3089e49e4'
SOURCE_PATH = 'pictographic-primitives/sports/acro yoga pose_5240dbe0-19a2-54d5-b0f7-5cc3089e49e4.svg'
AUTHOR = 'gpt-6'

class AcroYogaSupportedBalance(Solo48):
    icon_id = 'acro-yoga-supported-balance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('acro', 'yoga', 'supported', 'balance')

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
        # Two people balance with both heads on the right and bent bodies extending left.
        self.circle('upper-head',39,17,3)
        self.circle('lower-head',39,39,3)
        self.add_line('upper-body',(6,20),(20,20))
        self.add_arc('upper-bend',(20,20),(24,16),radius_x=4,sweep=False)
        self.add_line('upper-leg',(24,16),(24,12))
        self.add_arc('raised-foot',(24,12),(18,6),radius_x=6,sweep=False)
        self.add_contour('upper-pose','upper-body','upper-bend','upper-leg','raised-foot')
        self.add_line('lower-body',(6,42),(22,42))
        self.add_arc('lower-bend',(22,42),(26,38),radius_x=4,sweep=False)
        self.add_line('lower-leg',(26,38),(20,30))
        self.add_line('support',(20,30),(20,20))
        self.add_contour('lower-pose','lower-body','lower-bend','lower-leg','support')
        self.relate('connect','support','upper-body')
        self.relate('connect','support','upper-bend')
