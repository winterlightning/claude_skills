"""A thick circular weight plate appears in oblique view as a broad oval disk. A curved interior edge shows its depth, and a horizontal bar projects from both sides.

Kept the oblique oval plate, curved depth edge and projecting bar; omitted no defining parts. Perspective intentionally offsets the plate face.
Source oblique construction; coherent elliptical arcs with exact shared endpoints; no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99ce4ea2-dfe0-4636-870c-35974dcd441b'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell disk weight_99ce4ea2-dfe0-4636-870c-35974dcd441b.svg'
AUTHOR = 'gpt-6'

class WeightPlateOnBar(Solo48):
    icon_id = 'weight-plate-on-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('weight', 'plate', 'bar', 'dumbbell', 'fitness', 'equipment')

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
        self.add_arc('face-upper',(28,8),(36,24),radius_x=8,radius_y=16)
        self.add_arc('face-lower',(36,24),(28,40),radius_x=8,radius_y=16)
        self.add_arc('back-lower',(28,40),(11,24),radius_x=17,radius_y=16)
        self.add_arc('back-upper',(11,24),(28,8),radius_x=17,radius_y=16)
        self.add_contour('plate','face-upper','face-lower','back-lower','back-upper',closed=True)
        self.add_arc('depth-edge',(28,40),(28,8),radius_x=8,radius_y=16)
        for part in ['face-upper','face-lower','back-lower','back-upper']:self.relate('connect','depth-edge',part)
        self.add_line('left-bar',(4,24),(11,24))
        for part in ['back-lower','back-upper']:self.relate('connect','left-bar',part)
        self.add_polyline('right-bar',(29,24),(36,24),(44,24))
        for part in ['face-upper','face-lower']:
            for bar in ['right-bar-1','right-bar-2']:self.relate('connect',bar,part)
