"""A round kettlebell has a short squared handle rising from its upper shoulders. A small rectangular opening separates the grip from the body, and a curved highlight follows the lower-left surface.

Rounded weight and squared arched handle retained. Decorative surface highlight omitted; shoulders and handle mirror around x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01dca19c-2ee1-4c4c-b084-cdd5d4c10ae5'
SOURCE_PATH = 'pictographic-primitives/sports/grip weights_01dca19c-2ee1-4c4c-b084-cdd5d4c10ae5.svg'
AUTHOR = 'gpt-6'

class Kettlebell(Solo48):
    icon_id = 'kettlebell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('kettlebell', 'weight', 'grip', 'strength', 'fitness', 'equipment')

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
        self.add_arc('body-left',(6,24),(14,16),radius_x=8)
        self.add_line('body-top',(14,16),(34,16))
        self.add_arc('body-right',(34,16),(42,24),radius_x=8)
        self.add_arc('body-bottom',(42,24),(6,24),radius_x=18)
        self.add_contour('body','body-left','body-top','body-right','body-bottom',closed=True)
        self.add_line('handle-left',(14,16),(14,10))
        self.add_arc('handle-tl',(14,10),(18,6),radius_x=4)
        self.add_line('handle-top',(18,6),(30,6))
        self.add_arc('handle-tr',(30,6),(34,10),radius_x=4)
        self.add_line('handle-right',(34,10),(34,16))
        self.add_contour('handle','handle-left','handle-tl','handle-top','handle-tr','handle-right')
        for a in ['body-left','body-top']:self.relate('connect','handle-left',a)
        for a in ['body-right','body-top']:self.relate('connect','handle-right',a)
