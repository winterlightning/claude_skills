"""A rectangular goal mouth recedes inward along sloping side and top edges. A square mesh spans the back, with lower net strands hanging toward the open ground edge.

Kept receding top and side edges; mesh reduced to four large openings with three hanging strands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2c7fa679-ceb1-4be0-97bd-8bb2a090844f'
SOURCE_PATH = 'pictographic-primitives/sports/goal net_2c7fa679-ceb1-4be0-97bd-8bb2a090844f.svg'
AUTHOR = 'gpt-6'

class GoalNetPerspective(Solo48):
    icon_id = 'goal-net-perspective'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('goal', 'net', 'football', 'soccer', 'equipment', 'sport')

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
        branches=[('outer-top',[(6,6),(42,6)]),('left-post',[(6,6),(6,42)]),('right-post',[(42,6),(42,42)]),('left-top',[(6,6),(14,14)]),('right-top',[(42,6),(34,14)]),('left-bottom',[(6,42),(14,34)]),('right-bottom',[(42,42),(34,34)])]
        for y in [14,24,34]:branches.append((f'row-{y}',[(14,y),(24,y),(34,y)]))
        for x in [14,24,34]:branches.append((f'column-{x}',[(x,14),(x,24),(x,34),(x,38)]))
        self.skeleton(branches)
