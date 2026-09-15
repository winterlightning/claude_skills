"""A domed protective hood surrounds a narrow oval face opening crossed by three horizontal bars. Its lower edge spreads outward into three rounded protective lobes beneath the face.

Domed hood, separate face opening and three rounded hem lobes retained. Three small grille bars reduced to one divider; outer flare rebalanced to the square envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38c7b142-9112-4996-82a7-8d6d958adc9f'
SOURCE_PATH = 'pictographic-primitives/sports/mask helmet_38c7b142-9112-4996-82a7-8d6d958adc9f.svg'
AUTHOR = 'gpt-6'

class ProtectiveHoodGrille(Solo48):
    icon_id = 'protective-hood-grille'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('mask', 'hood', 'helmet', 'grille', 'protection', 'sport')

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
        self.add_arc('dome',(6,24),(42,24),radius_x=18)
        self.add_line('right-side',(42,24),(42,40))
        for i,x in enumerate([42,30,18]):self.add_arc(f'hem-{i}',(x,40),(x-12,40),radius_x=6,radius_y=2)
        self.add_line('left-side',(6,40),(6,24))
        self.add_contour('hood','dome','right-side','hem-0','hem-1','hem-2','left-side',closed=True)
        self.add_arc('face-top',(16,23),(32,23),radius_x=8)
        self.add_arc('face-bottom',(32,23),(16,23),radius_x=8)
        self.add_contour('face','face-top','face-bottom',closed=True)
        self.add_line('bar',(16,23),(32,23))
        for a in ['face-top','face-bottom']:self.relate('connect','bar',a)
