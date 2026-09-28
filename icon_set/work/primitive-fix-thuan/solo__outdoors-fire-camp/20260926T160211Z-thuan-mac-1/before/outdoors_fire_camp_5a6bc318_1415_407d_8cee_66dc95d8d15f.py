from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a6bc318-1415-407d-8cee-66dc95d8d15f'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg'
AUTHOR = 'gpt-6'
PLAN = 'Campfire above a rectangular six-section fuel bed. Grid cells share intersections.'
CONSTRUCTION_REFERENCES = 'flame: asymmetric tongue and rounded lower bowl.'
OMISSIONS = 'All six fuel cells retained; flame reduced to a compact smooth tongue.'

class Drawing(Solo48):
    icon_id = 'outdoors-fire-camp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('outdoors', 'fire', 'camp')

    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self):
        # Clearly asymmetric tongue with left indentation, as in the reference.
        # Bowl and tongue share tangent directions at their smooth junction.
        self.add_bezier('fire-left',(18,12),((19,15),(24,12),(22,6)))
        self.add_bezier('fire-right',(22,6),((27,7),(30,9),(30,12)))
        self.add_arc('fire-bowl',(30,12),(18,12),radius_x=6,radius_y=5)
        self.add_contour('flame','fire-left','fire-right','fire-bowl',closed=True)
        self.box('fuel',6,26,36,16,2)
        self.add_line('fuel-horizontal',(6,34),(42,34));self.relate('connect','fuel','fuel-horizontal')
        for x in (18,30):
         self.add_polyline(f'fuel-divider-{x}',(x,26),(x,34),(x,42))
         self.relate('connect','fuel',f'fuel-divider-{x}');self.relate('connect','fuel-horizontal',f'fuel-divider-{x}')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
