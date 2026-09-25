"""A front-facing padded headguard has a broad brow band and rounded crown. Deep cheek pads curve inward around a large face opening, joining a rounded protective edge below.

Kept rounded padding and a cheek-shaped face opening; omitted the extra brow seam. Paired geometry mirrors about x=24.
Source padded silhouette and inward cheek pads; rounded-rectangle and circular-arc construction, with no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6baf10a-ceff-5913-8e52-b4e52144f4b0'
SOURCE_PATH = 'pictographic-primitives/sports/boxing head guard_b6baf10a-ceff-5913-8e52-b4e52144f4b0.svg'
AUTHOR = 'gpt-6'

class BoxingHeadguard(Solo48):
    icon_id = 'boxing-headguard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('boxing', 'headguard', 'helmet', 'protection', 'equipment', 'sport')

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
        # One padded crown and paired cheek pads; chin strap closes the face opening.
        self.add_arc('crown',(6,20),(42,20),radius_x=18,radius_y=14)
        self.add_line('outer-right',(42,20),(42,28))
        self.add_arc('right-pad',(42,28),(34,42),radius_x=8,radius_y=14)
        self.add_arc('right-pad-tip',(34,42),(30,38),radius_x=4)
        self.add_line('right-cheek',(30,38),(30,32))
        self.add_arc('right-cheek-upper',(30,32),(33,26),radius_x=7)
        self.add_line('opening-right',(33,26),(33,21))
        self.add_arc('opening-tr',(33,21),(30,18),radius_x=3,sweep=False)
        self.add_line('brow',(30,18),(18,18))
        self.add_arc('opening-tl',(18,18),(15,21),radius_x=3,sweep=False)
        self.add_line('opening-left',(15,21),(15,26))
        self.add_arc('left-cheek-upper',(15,26),(18,32),radius_x=7)
        self.add_line('left-cheek',(18,32),(18,38))
        self.add_arc('left-pad-tip',(18,38),(14,42),radius_x=4)
        self.add_arc('left-pad',(14,42),(6,28),radius_x=8,radius_y=14)
        self.add_line('outer-left',(6,28),(6,20))
        self.add_contour('padding','crown','outer-right','right-pad','right-pad-tip','right-cheek','right-cheek-upper','opening-right','opening-tr','brow','opening-tl','opening-left','left-cheek-upper','left-cheek','left-pad-tip','left-pad','outer-left',closed=True)
        self.add_line('chin-strap',(14,42),(34,42))
        for part in ['left-pad-tip','left-pad','right-pad-tip','right-pad']:self.relate('connect','chin-strap',part)
