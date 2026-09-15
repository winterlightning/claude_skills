"""A triangular flag rises from an oval golf hole on the left. A long leaning club stands to the right, with its curved head beside a small ball near the bottom.

Flag, cup and leaning hooked club retained. The separate tiny ball is omitted to leave clearance between cup and club.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00bfd2ee-e892-43ad-9371-22aec3515ffe'
SOURCE_PATH = 'pictographic-primitives/sports/golf hole aim_00bfd2ee-e892-43ad-9371-22aec3515ffe.svg'
AUTHOR = 'gpt-6'

class GolfClubFlaggedHole(Solo48):
    icon_id = 'golf-club-flagged-hole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('golf', 'club', 'ball', 'hole', 'flag', 'putting')

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
        self.add_arc('hole-right',(12,30),(12,42),radius_x=6)
        self.add_arc('hole-left',(12,42),(12,30),radius_x=6)
        self.add_contour('hole','hole-right','hole-left',closed=True)
        self.skeleton([('pole',[(12,6),(12,22),(12,30)]),('flag',[(12,6),(28,14),(12,22)]),('shaft',[(42,6),(34,38)])])
        for a in ['hole-left','hole-right']:self.relate('connect','pole-1',a)
        self.add_arc('club-heel',(34,38),(30,42),radius_x=4)
        self.add_line('club-toe',(30,42),(26,42))
        self.add_contour('club-head','club-heel','club-toe')
        self.relate('connect','shaft-0','club-heel')
