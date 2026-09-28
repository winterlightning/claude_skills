"""A compact golf cart faces right beneath a long flat canopy with rounded ends. Two wheels sit below an open passenger area, rear seat, and curved front body.

Open passenger area, flat canopy, seat and curved nose retained. Wheels share one diameter; tiny steering detail omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5007ce98-ec8e-4ec8-b398-2a01ebd012d1'
SOURCE_PATH = 'pictographic-primitives/sports/golf cart_5007ce98-ec8e-4ec8-b398-2a01ebd012d1.svg'
AUTHOR = 'gpt-6'

class GolfCart(Solo48):
    icon_id = 'golf-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('golf', 'cart', 'vehicle', 'transport', 'course', 'equipment')

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
        for name,x in [('rear',10),('front',38)]:
         self.add_arc(name+'-r',(x,32),(x,40),radius_x=4)
         self.add_arc(name+'-l',(x,40),(x,32),radius_x=4)
         self.add_contour(name,name+'-r',name+'-l',closed=True)
        self.skeleton([('roof',[(4,8),(10,8),(34,8),(44,8)]),('rear-support',[(10,8),(10,24)]),('front-support',[(34,8),(38,24)]),('chassis',[(4,32),(10,32),(24,32),(38,32),(44,32),(44,30)]),('seat',[(4,32),(4,24),(10,24),(24,24),(24,32)])])
        self.add_arc('nose',(38,24),(44,30),radius_x=6)
        for a in ['front-support-0','chassis-4']:self.relate('connect','nose',a)
        for side,parts in [('rear',['chassis-0','chassis-1']),('front',['chassis-2','chassis-3'])]:
         for a in parts:
          for b in [side+'-r',side+'-l']:self.relate('connect',a,b)
