from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '45f19a3b-198b-4c09-92f8-b3fc6d512c7f'
SOURCE_PATH = 'icon_set/work/todo-references/painting palette 1_45f19a3b-198b-4c09-92f8-b3fc6d512c7f.svg'
AUTHOR = 'gpt-6'
PLAN = 'Round painting palette with three equal circular wells in a triangular arrangement.'
CONSTRUCTION_REFERENCES = 'palette: common outer circle and repeated round paint wells.'
OMISSIONS = 'None; triangular pattern and three circular wells retained.'

class Drawing(Solo48):
    icon_id = 'painting-palette-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('painting', 'palette', '1')

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
        self.circle('palette',24,24,20)
        for i,(x,y) in enumerate(((24,16),(17,29),(31,29))):self.circle(f'well-{i}',x,y,3)

KEYSHAPE_INK_BOUNDS = (2, 2, 46, 46)
KEYSHAPE_REASON = 'A dominant round outline owns the radial envelope centered at (24,24).'
