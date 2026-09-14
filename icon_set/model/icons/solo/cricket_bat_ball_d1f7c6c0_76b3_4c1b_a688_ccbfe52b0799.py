"""A cricket bat tilts upward to the right with a broad flat blade and a narrower straight handle. A small round ball floats in the open space beside its upper-left side.

Kept a flat broad blade and aligned narrow grip, plus the separate ball. Reduced the handle to one stroke; retained the diagonal source pose.
Source flat cricket blade; circle and parallel diagonal construction. No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1f7c6c0-76b3-4c1b-a688-ccbfe52b0799'
SOURCE_PATH = 'pictographic-primitives/sports/cricket bat ball_d1f7c6c0-76b3-4c1b-a688-ccbfe52b0799.svg'
AUTHOR = 'gpt-6'

class CricketBatBall(Solo48):
    icon_id = 'cricket-bat-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('cricket', 'bat', 'ball', 'equipment', 'sport', 'hitting')

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
        self.circle('ball',11,11,5)
        self.add_polyline('blade',(34,7),(42,13),(27,33),(23,30),(19,27),closed=True)
        self.add_line('handle',(23,30),(14,42))
        self.relate('connect','handle','blade-3')
        self.relate('connect','handle','blade-4')
