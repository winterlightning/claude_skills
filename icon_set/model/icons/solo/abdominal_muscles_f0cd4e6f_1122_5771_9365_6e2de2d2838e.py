"""A cropped torso narrows at the waist above a curved waistband. Two opposing columns of rounded muscle segments mark the abdomen, leaving a narrow vertical gap between them.

Tapered waist and curved waistband retained; six small muscle outlines reduced to three paired marks around the center line.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f0cd4e6f-1122-5771-9365-6e2de2d2838e'
SOURCE_PATH = 'pictographic-primitives/sports/fitness six pack_f0cd4e6f-1122-5771-9365-6e2de2d2838e.svg'
AUTHOR = "gpt-6"

class AbdominalMuscles(Solo48):
    icon_id = 'abdominal-muscles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('abdomen', 'muscle', 'fitness', 'torso', 'strength', 'core')

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
        self.add_arc('left-side',(10,6),(10,30),radius_x=40)
        self.add_arc('right-side',(38,6),(38,30),radius_x=40,sweep=False)
        self.skeleton([('left-lower',[(10,30),(8,36),(6,42)]),('right-lower',[(38,30),(40,36),(42,42)]),('center',[(24,9),(24,18),(24,27)]),('upper',[(20,9),(24,9),(28,9)]),('middle',[(20,18),(24,18),(28,18)]),('lower',[(20,27),(24,27),(28,27)])])
        self.relate('connect','left-side','left-lower-0');self.relate('connect','right-side','right-lower-0')
        self.add_arc('waistband',(8,36),(40,36),radius_x=16,radius_y=4,sweep=False)
        for a in ['left-lower-0','left-lower-1','right-lower-0','right-lower-1']:self.relate('connect','waistband',a)
