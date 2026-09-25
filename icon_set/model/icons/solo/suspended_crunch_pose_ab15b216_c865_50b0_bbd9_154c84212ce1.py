"""A curled figure reclines beneath two sloping suspension lines, with its circular head on the left. The torso and raised bent limbs form a compact upward-facing shape between the straps.

Kept the reclining head, curled body and both suspension lines with real limb contacts. Removed doubled outlines.
Source reclining orientation and suspension; Lucide person-standing supplies the detached circular head and spare body strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab15b216-c865-50b0-bbd9-154c84212ce1'
SOURCE_PATH = 'pictographic-primitives/sports/crunches pose_ab15b216-c865-50b0-bbd9-154c84212ce1.svg'
AUTHOR = 'gpt-6'

class SuspendedCrunchPose(Solo48):
    icon_id = 'suspended-crunch-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('crunch', 'suspension', 'exercise', 'fitness', 'core', 'pose')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self,branches):
        parts=[]
        for name,points in branches:
            members=[]
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}';members.append(key)
                self.add_line(key,a,b);parts.append((key,a,b))
            if len(members)>1:self.add_contour(name,*members)
        for index,(a,p,q) in enumerate(parts):
            for b,r,s in parts[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def rounded(self,name,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%8];key=f'{name}-{index}';members.append(key)
            if index%2:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def weight(self,name,x,y,w,h,r):
        # Expose bar attachment nodes at the midpoint of each vertical wall.
        middle=y+h//2
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,middle),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,middle),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%len(pts)];key=f'{name}-{index}';members.append(key)
            if index in [1,4,6,9]:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.circle('head',9,26,3)
        self.skeleton([
         ('body',[(22,24),(20,32),(28,42),(35,36),(42,30)]),
         ('left-strap',[(28,6),(22,24)]),
         ('right-strap',[(28,6),(35,36)])])
        self.add_line('neck',(12,26),(20,32))
        for part in ['head-top','head-bottom','body-0','body-1']:self.relate('connect','neck',part)
