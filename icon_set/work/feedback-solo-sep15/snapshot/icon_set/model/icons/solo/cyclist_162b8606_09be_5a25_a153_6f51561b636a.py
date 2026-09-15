"""A rider bends forward above two circular bicycle wheels, with a bent arm reaching a short handlebar. A sloping front fork joins the handlebar to the right wheel.

Equal wheels, bent rider, handlebar and fork retained; wheel hubs and hidden frame omitted.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '162b8606-09be-5a25-a153-6f51561b636a'
SOURCE_PATH = 'pictographic-primitives/sports/fitness bicycle_162b8606-09be-5a25-a153-6f51561b636a.svg'
AUTHOR = "gpt-6"

class Cyclist(Solo48):
    icon_id = 'cyclist'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('bicycle', 'cyclist', 'cycling', 'rider', 'sport', 'pedal')

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
        for name,x in [('rear',9),('front',39)]:
         self.add_arc(name+'-right',(x,30),(x,40),radius_x=5)
         self.add_arc(name+'-left',(x,40),(x,30),radius_x=5)
         self.add_contour(name,name+'-right',name+'-left',closed=True)

        self.circle('head',28,11,3)
        self.skeleton([('body',[(24,23),(18,25),(24,30),(24,36)]),('arms',[(24,23),(32,22),(37,22),(42,22)]),('fork',[(37,22),(39,30)])])
        for part in ['front-left','front-right']:self.relate('connect','fork-0',part)
