from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9b912024-cd41-447a-9b3f-0d8b1e66a4fe'
SOURCE_PATH = 'icon_set/work/todo-references/paragraph right to left_9b912024-cd41-447a-9b3f-0d8b1e66a4fe.svg'
AUTHOR = 'gpt-6'
PLAN = 'Text-direction T above a leftward arrow. A centered stem shares the top-bar midpoint.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; hand-authored directional geometry.'
OMISSIONS = 'None.'

class Drawing(Solo48):
    icon_id = 'paragraph-right-to-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('paragraph', 'right', 'to', 'left')

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
        self.add_polyline('top-bar',(14,6),(26,6),(38,6))
        self.add_line('stem',(26,6),(26,26));self.relate('connect','top-bar','stem')
        self.add_polyline('arrow',(14,26),(6,34),(14,42))
        self.add_line('arrow-shaft',(6,34),(42,34));self.relate('connect','arrow','arrow-shaft')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
