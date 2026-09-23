from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b569bafc-f80a-44b7-a43f-233891818936'
SOURCE_PATH = 'icon_set/work/todo-references/passport hand_b569bafc-f80a-44b7-a43f-233891818936.svg'
AUTHOR = 'gpt-6'
PLAN = 'Passport cover with an exposed binding above and a centered globe. The source has no visible hand.'
CONSTRUCTION_REFERENCES = 'globe: equal hemispheres and central meridian; monitor: rounded enclosure.'
OMISSIONS = 'Latitude pair reduced to a central equator; one meridian retained. Source has no visible hand.'

class Drawing(Solo48):
    icon_id = 'passport-hand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('passport', 'hand')

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
        self.box('cover',8,12,32,32,3)
        self.add_line('binding',(8,15),(8,7))
        self.add_arc('binding-corner',(8,7),(11,4),radius_x=3)
        self.add_line('binding-top',(11,4),(35,4))
        self.add_arc('binding-right',(35,4),(38,7),radius_x=3)
        self.add_line('binding-end',(38,7),(38,12))
        self.add_contour('binding-outline','binding','binding-corner','binding-top','binding-right','binding-end')
        self.relate('connect','binding-outline','cover')
        self.circle('globe',24,28,7)
        self.add_polyline('equator',(17,28),(24,28),(31,28));self.relate('connect','globe','equator')
        self.add_polyline('meridian',(24,21),(24,28),(24,35));self.relate('connect','globe','meridian');self.relate('connect','equator','meridian')

KEYSHAPE_INK_BOUNDS = (6, 2, 42, 46)
KEYSHAPE_REASON = 'The upright passport uses the 32×40 centerline envelope.'
