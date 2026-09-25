"""A boxer reaches forward to strike a hanging punching bag.

Reduced the glove to the hand contact and the body to readable limbs. Bag contact is physical, not a modifier.
Lucide person-standing informed the figure; capsule construction defines the bag.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8039d96b-5b62-5296-8a94-f059bad555d0'
SOURCE_PATH = 'pictographic-primitives/sports/boxing boxer bag_8039d96b-5b62-5296-8a94-f059bad555d0.svg'
AUTHOR = 'gpt-6'

class BoxerPunchingBag(Solo48):
    icon_id = 'boxer-punching-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('boxer', 'punching', 'bag')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self):
        # A boxer reaches forward to strike a hanging punching bag.
        self.circle('head',14,9,3)
        self.skeleton([('torso',[(14,21),(11,31)]),('arm',[(14,21),(23,21),(32,21)]),('back-leg',[(11,31),(6,42)]),('front-leg',[(11,31),(22,36),(22,42)])])
        self.add_arc('bag-top-left',(32,19),(37,14),radius_x=5)
        self.add_arc('bag-top-right',(37,14),(42,19),radius_x=5)
        self.add_line('bag-right',(42,19),(42,29))
        self.add_arc('bag-bottom',(42,29),(32,29),radius_x=5)
        self.add_line('bag-left-lower',(32,29),(32,21))
        self.add_line('bag-left-upper',(32,21),(32,19))
        self.add_contour('bag','bag-top-left','bag-top-right','bag-right','bag-bottom','bag-left-lower','bag-left-upper',closed=True)
        self.add_line('suspension',(37,6),(37,14))
        for part in ['bag-top-left','bag-top-right']:self.relate('connect','suspension',part)
        for part in ['bag-left-lower','bag-left-upper']:self.relate('connect','arm-1',part)
