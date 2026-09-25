"""A front-facing goal has a broad rectangular frame with rounded top corners and two extended posts. A regular grid of square net openings fills the space inside.

Rounded upper corners and extending posts retained; net reduced to twelve generous cells on a shared grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5179a4ad-d664-4226-9a55-1624876c5ab4'
SOURCE_PATH = 'pictographic-primitives/sports/goal net_5179a4ad-d664-4226-9a55-1624876c5ab4.svg'
AUTHOR = 'gpt-6'

class GoalNet(Solo48):
    icon_id = 'goal-net'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
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
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        branches=[('top',[(8,8),(14,8),(24,8),(34,8),(40,8)]),('left',[(4,12),(4,18),(4,28),(4,38),(4,40)]),('right',[(44,12),(44,18),(44,28),(44,38),(44,40)])]
        for y in [18,28,38]:branches.append((f'row-{y}',[(4,y),(14,y),(24,y),(34,y),(44,y)]))
        for x in [14,24,34]:branches.append((f'col-{x}',[(x,8),(x,18),(x,28),(x,38)]))
        self.skeleton(branches)
        for a,b in [('tl','top-0'),('tl','left-0'),('tr','top-3'),('tr','right-0')]:self.relate('connect',a,b)
