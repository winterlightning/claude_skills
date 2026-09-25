"""A tall straight pole rises from a flattened oval golf hole. A triangular pennant projects to the right near the top, while the pole continues into the hole.

Triangular pennant and flattened oval cup retained; the pole enters the cup through a true shared point.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5fe34a32-fdd7-525f-aea1-3b59402ec73d'
SOURCE_PATH = 'pictographic-primitives/sports/golf hole_5fe34a32-fdd7-525f-aea1-3b59402ec73d.svg'
AUTHOR = 'gpt-6'

class FlaggedGolfHole(Solo48):
    icon_id = 'flagged-golf-hole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('golf', 'hole', 'flag', 'course', 'green', 'putting')

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
        self.skeleton([('pole',[(24,6),(24,22),(24,28),(24,32)]),('flag',[(24,6),(42,14),(24,22)])])
        pts=[(24,28),(42,35),(24,42),(6,35)]
        for i in range(4):self.add_arc(f'hole-{i}',pts[i],pts[(i+1)%4],radius_x=18,radius_y=7)
        self.add_contour('hole',*[f'hole-{i}' for i in range(4)],closed=True)
        for a in ['pole-1','pole-2']:
         for b in ['hole-0','hole-3']:self.relate('connect',a,b)
