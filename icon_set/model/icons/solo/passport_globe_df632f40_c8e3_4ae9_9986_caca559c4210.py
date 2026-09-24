from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df632f40-c8e3-4ae9-9986-caca559c4210'
SOURCE_PATH = 'icon_set/work/todo-references/passport globe_df632f40-c8e3-4ae9-9986-caca559c4210.svg'
AUTHOR = 'gpt-6'
PLAN = 'Foreground passport with globe over a larger background world disc. Preserve overlap and continental boundary.'
CONSTRUCTION_REFERENCES = 'globe: meridian and equator construction; monitor: consistent cover corners.'
OMISSIONS = 'Globe meridians reduced to a single central meridian; background continent simplified.'

class Drawing(Solo48):
    icon_id = 'passport-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('passport', 'globe')

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
        self.add_arc('world',(22,32),(32,16),radius_x=13,large_arc=True)
        self.add_polyline('continent',(8,16),(16,16),(16,23),(12,25),(12,31))
        self.box('passport',22,16,20,26,3)
        self.circle('globe',32,29,6)
        self.add_polyline('equator',(26,29),(32,29),(38,29));self.relate('connect','globe','equator')
        self.add_polyline('meridian',(32,23),(32,29),(32,35));self.relate('connect','globe','meridian');self.relate('connect','equator','meridian')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
