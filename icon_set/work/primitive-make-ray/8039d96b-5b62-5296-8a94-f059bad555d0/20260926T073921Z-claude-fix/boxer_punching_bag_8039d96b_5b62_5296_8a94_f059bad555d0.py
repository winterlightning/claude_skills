"""A boxer reaches forward to strike a hanging punching bag.

Reduced the glove to the hand contact and the body to readable limbs. Bag contact is physical, not a modifier.
Lucide person-standing informed the figure; capsule construction defines the bag.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8039d96b-5b62-5296-8a94-f059bad555d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer-punching-bag/20260926T073831Z-thuan-mac/reference/boxing boxer bag_8039d96b-5b62-5296-8a94-f059bad555d0.svg'
AUTHOR = "claude-opus-5-5"

class BoxerPunchingBag(Solo48):
    icon_id = 'boxer-punching-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
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
        # Redraw (no reviewer text; matched to the reference): a boxer throws a straight punch
        # at a hanging bag, with a clear gap between glove and bag. Boxer: r4 head (10, 10) exactly
        # 8 above the neck of a vertical torso (10, 22)-(10, 30); the punching arm runs level from
        # the neck to a round r3 glove at (22, 22); the back leg drops to (6, 42) and the front
        # leg bends through the knee (20, 35) to (20, 42). Bag: a capsule x 34..42 with r4 ends
        # (y 12..38) hanging from a chain (38, 6)-(38, 12); the glove stops 9 short of it.
        # Human reference: icon_set/references/human_ref/full_body_ref.png.
        self.circle('head', 10, 10, 4)
        self.add_line('torso', (10, 22), (10, 30))
        self.add_line('arm', (10, 22), (19, 22))
        self.circle('glove', 22, 22, 3)
        self.add_line('back-leg', (10, 30), (6, 42))
        self.add_polyline('front-leg', (10, 30), (20, 35), (20, 42))
        for part in ('arm', 'back-leg', 'front-leg'):
            self.relate('connect', 'torso', part)
        self.relate('connect', 'back-leg', 'front-leg')
        self.relate('connect', 'arm', 'glove')
        self.mark_human_figure('boxer', head='head', torso='torso', torso_junction='start')
        self.add_arc('bag-top-left', (34, 16), (38, 12), radius_x=4)
        self.add_arc('bag-top-right', (38, 12), (42, 16), radius_x=4)
        self.add_line('bag-right', (42, 16), (42, 34))
        self.add_arc('bag-bottom', (42, 34), (34, 34), radius_x=4)
        self.add_line('bag-left', (34, 34), (34, 16))
        self.add_contour('bag', 'bag-top-left', 'bag-top-right', 'bag-right', 'bag-bottom', 'bag-left', closed=True)
        self.add_line('chain', (38, 6), (38, 12))
        self.relate('connect', 'chain', 'bag')
