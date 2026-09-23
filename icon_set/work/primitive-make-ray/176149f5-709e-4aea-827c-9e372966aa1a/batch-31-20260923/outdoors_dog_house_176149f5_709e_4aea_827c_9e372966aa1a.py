from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '176149f5-709e-4aea-827c-9e372966aa1a'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg'
AUTHOR = 'gpt-6'
PLAN = 'Side-view dog under a sloping shelter roof. Preserve right-facing muzzle and paired legs.'
CONSTRUCTION_REFERENCES = 'house: long coherent shelter strokes.'
OMISSIONS = 'Rear far leg and minor fur contours omitted to retain a readable silhouette.'

class Drawing(Solo48):
    icon_id = 'outdoors-dog-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('outdoors', 'dog', 'house')

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
        self.add_polyline('shelter',(42,6),(6,16),(6,42),(42,42))
        self.add_polyline('dog',(12,26),(14,22),(26,22),(31,14),(32,20),(38,23),(35,27),(31,27),(29,34),(29,35),(25,35),(25,29),(19,29),(17,35),(13,35),(13,30))

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
