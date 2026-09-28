"""A side-view sports helmet faces right with a rounded shell, circular ear opening, and short projecting visor. A recessed face opening curves into a protective lower section at the front.

Rounded shell, ear opening, face recess and chin protection retained. Ear opening enlarged relative to source for native visibility.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02e66252-9801-433c-be43-12ad6c9de1cf'
SOURCE_PATH = 'pictographic-primitives/sports/helmet sports_02e66252-9801-433c-be43-12ad6c9de1cf.svg'
AUTHOR = 'gpt-6'

class SportsHelmet(Solo48):
    icon_id = 'sports-helmet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('helmet', 'sport', 'protection', 'headgear', 'equipment', 'safety')

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
        self.add_arc('shell-tl',(6,24),(24,6),radius_x=18)
        self.add_arc('shell-tr',(24,6),(42,24),radius_x=18)
        self.add_line('front',(42,24),(42,34))
        self.add_arc('chin',(42,34),(34,42),radius_x=8)
        self.add_line('base',(34,42),(24,42))
        self.add_arc('shell-bl',(24,42),(6,24),radius_x=18)
        self.add_contour('shell','shell-tl','shell-tr','front','chin','base','shell-bl',closed=True)
        self.add_arc('face-bottom',(24,42),(28,38),radius_x=4,sweep=False)
        self.add_line('face-wall',(28,38),(28,30))
        self.add_arc('face-top',(28,30),(34,24),radius_x=6)
        self.add_line('visor',(34,24),(42,24))
        self.add_contour('face','face-bottom','face-wall','face-top','visor')
        for a in ['base','shell-bl']:self.relate('connect','face-bottom',a)
        for a in ['shell-tr','front']:self.relate('connect','visor',a)
        self.circle('ear',17,26,2)
