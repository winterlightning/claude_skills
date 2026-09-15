'Pole vaulter: preserve the bent pole and curled action pose, with a round head and exact four-unit head-to-body clearance.'
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

    def build(self) -> None:
        self.add_arc('head-top', (8,12), (16,12), radius_x=4, radius_y=4)
        self.add_arc('head-bottom', (16,12), (8,12), radius_x=4, radius_y=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        # full_body_ref.png: head bottom y=16 and shoulders y=24 give an exact 4-unit ink gap.
        self.add_bezier('pole',(24,4),((26,4),(28,6),(30,10)),((37,18),(40,34),(40,44)))
        self.add_polyline('body',(10,24),(16,24),(24,28),(18,33))
        self.add_polyline('arms',(16,24),(24,24),(30,10));self.relate('connect','arms','body');self.relate('connect','arms','pole')
        self.add_line('back-leg',(18,33),(14,44));self.relate('connect','back-leg','body')
        self.add_polyline('front-leg',(18,33),(28,32),(32,39));self.relate('connect','front-leg','body');self.relate('connect','front-leg','back-leg')
