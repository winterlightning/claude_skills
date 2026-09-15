"""A runner leans left with one knee raised and the opposite leg stretched diagonally behind. Three short horizontal motion strokes trail to the right of the bent arms and torso.

Left-facing running posture and three trailing motion marks retained. Speed lines describe the action, rather than a separate status glyph.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f2f572ad-703c-51e8-8b77-597c50b75da0'
SOURCE_PATH = 'pictographic-primitives/sports/jogging fast running_f2f572ad-703c-51e8-8b77-597c50b75da0.svg'
AUTHOR = 'gpt-6'

class FastRunner(Solo48):
    icon_id = 'fast-runner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('running', 'sprint', 'runner', 'speed', 'athlete', 'fitness')

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
        self.circle('head',16,9,3)
        self.skeleton([('body',[(18,21),(22,30)]),('left-arm',[(18,21),(12,25),(6,20)]),('right-arm',[(18,21),(26,21),(28,28)]),('bent-leg',[(22,30),(12,34),(14,42)]),('rear-leg',[(22,30),(32,42)])])
        for i,y in enumerate([12,22,32]):self.add_line(f'motion-{i}',(38,y),(42,y))
