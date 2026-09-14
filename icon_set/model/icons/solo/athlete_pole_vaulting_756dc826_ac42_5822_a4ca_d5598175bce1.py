"""A pole vaulter curls beside a strongly bent pole.

Kept the bent pole, raised hand contact and curled legs; omitted doubled body outlines.
Lucide person-standing informs spare limbs; source fixes the pose and bent-pole relationship.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '756dc826-ac42-5822-a4ca-d5598175bce1'
SOURCE_PATH = 'pictographic-primitives/sports/athletics pole vault_756dc826-ac42-5822-a4ca-d5598175bce1.svg'
AUTHOR = 'gpt-6'

class AthletePoleVaulting(Solo48):
    icon_id = 'athlete-pole-vaulting'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('athlete', 'pole', 'vaulting')

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
        # A pole vaulter curls beside a strongly bent pole.
        self.add_arc('pole-upper',(10,6),(28,12),radius_x=30,radius_y=40)
        self.add_arc('pole-lower',(28,12),(40,42),radius_x=30,radius_y=40)
        self.add_contour('pole','pole-upper','pole-lower')
        self.circle('head',11,16,3)
        self.skeleton([('body',[(22,24),(14,28),(22,35)]),('arms',[(22,24),(28,12)]),('back-leg',[(22,35),(18,42)]),('front-leg',[(22,35),(28,32),(29,39)])])
        for part in ['pole-upper','pole-lower']:self.relate('connect','arms-0',part)
