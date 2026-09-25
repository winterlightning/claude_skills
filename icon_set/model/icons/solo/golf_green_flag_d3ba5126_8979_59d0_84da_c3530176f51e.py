"""An upright triangular flag marks an irregular rounded golf green. The green broadens into a smaller connected lobe on the right, and its outline opens near the flagpole.

Open irregular green and smaller right lobe retained. Flagpole remains independent of the green outline; natural asymmetry is deliberate.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3ba5126-8979-59d0-84da-c3530176f51e'
SOURCE_PATH = 'pictographic-primitives/sports/golf hole_d3ba5126-8979-59d0-84da-c3530176f51e.svg'
AUTHOR = 'gpt-6'

class GolfGreenFlag(Solo48):
    icon_id = 'golf-green-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('golf', 'green', 'flag', 'course', 'hole', 'putting')

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
        self.skeleton([('pole',[(16,6),(16,22),(16,32)]),('flag',[(16,6),(34,14),(16,22)])])
        self.add_line('green-left',(6,28),(6,34))
        self.add_arc('green-bl',(6,34),(14,42),radius_x=8,sweep=False)
        self.add_line('green-bottom',(14,42),(28,42))
        self.add_arc('green-neck',(28,42),(34,36),radius_x=6,sweep=False)
        self.add_line('lobe-base',(34,36),(36,36))
        self.add_arc('lobe-lower',(36,36),(42,30),radius_x=6,sweep=False)
        self.add_arc('lobe-upper',(42,30),(36,24),radius_x=6,sweep=False)
        self.add_contour('green','green-left','green-bl','green-bottom','green-neck','lobe-base','lobe-lower','lobe-upper')
