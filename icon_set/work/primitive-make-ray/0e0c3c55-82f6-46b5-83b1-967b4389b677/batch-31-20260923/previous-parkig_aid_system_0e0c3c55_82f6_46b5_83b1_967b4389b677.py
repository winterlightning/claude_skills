from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0e0c3c55-82f6-46b5-83b1-967b4389b677'
SOURCE_PATH = 'icon_set/work/todo-references/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg'
AUTHOR = 'gpt-6'
PLAN = 'Parking aid P emits two waves toward a triangular obstacle. Deliberate diagonal arrangement.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; concentric wave arcs share their logical origin.'
OMISSIONS = 'None.'

class Drawing(Solo48):
    icon_id = 'parkig-aid-system'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('parkig', 'aid', 'system')

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
        self.letter_p('p',6,6,14,24)
        self.add_arc('signal-inner',(28,14),(22,25),radius_x=16)
        self.add_arc('signal-outer',(36,17),(26,30),radius_x=22)
        self.add_polyline('obstacle',(30,42),(36,34),(42,42),closed=True)
