"""An inverted yoga figure spreads the arms beneath raised legs.

Kept the upside-down head, raised legs and spread arms. Thin secondary sling loops were omitted to keep the inversion readable.
Source inversion orientation and symmetry; Lucide person-standing informs jointed limbs and a circular head.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4cdc728-6ddc-5030-90ee-9fd33c53636a'
SOURCE_PATH = 'pictographic-primitives/sports/aerial yogabasic inversion pose_a4cdc728-6ddc-5030-90ee-9fd33c53636a.svg'
AUTHOR = 'gpt-6'

class AerialYogaInversion(Solo48):
    icon_id = 'aerial-yoga-inversion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('aerial', 'yoga', 'inversion')

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
        # An inverted yoga figure spreads the arms beneath raised legs.
        self.circle('head',24,39,3)
        self.skeleton([('left-leg',[(16,6),(16,18),(24,18)]),('right-leg',[(32,6),(32,18),(24,18)]),('torso',[(24,18),(24,26)]),('left-arm',[(24,26),(6,32)]),('right-arm',[(24,26),(42,32)])])
