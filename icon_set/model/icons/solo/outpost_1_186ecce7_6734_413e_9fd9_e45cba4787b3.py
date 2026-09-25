from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '186ecce7-6734-413e-9fd9-e45cba4787b3'
SOURCE_PATH = 'icon_set/work/todo-references/outpost 1_186ecce7-6734-413e-9fd9-e45cba4787b3.svg'
AUTHOR = 'gpt-6'
PLAN = 'Roofed outpost with a central foreground rectangular device. Roof mirrors about x=24.'
CONSTRUCTION_REFERENCES = 'house: gable and side walls; monitor: rounded front object.'
OMISSIONS = 'Short device indicator omitted; screen division retained.'

class Drawing(Solo48):
    icon_id = 'outpost-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('outpost', '1')

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
        self.add_polyline('building',(16,34),(6,34),(6,20),(24,6),(42,20),(42,34),(32,34))
        self.box('device',16,24,16,18,3)
        self.relate('connect','building','device')
        self.add_line('screen-rule',(16,33),(32,33));self.relate('connect','device','screen-rule')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
