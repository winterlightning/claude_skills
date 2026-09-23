from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '12af7a01-21fd-509d-9eae-c7bfcfdaedd2'
SOURCE_PATH = 'icon_set/work/todo-references/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg'
AUTHOR = 'gpt-6'
PLAN = 'Oxygen cylinder with valve and connected circular timer. Preserve timer at upper right.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; capsule cylinder and clock constructed from shared centers.'
OMISSIONS = 'Clock minute subdivisions omitted; hands retained.'

class Drawing(Solo48):
    icon_id = 'oxygen-tank-timer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('oxygen', 'tank', 'timer')

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
        self.box('tank',6,20,15,22,6)
        self.add_polyline('valve',(10,20),(10,13),(17,13),(17,20))
        self.relate('connect','tank','valve')
        self.add_polyline('valve-top',(8,6),(14,6),(20,6))
        self.add_line('valve-neck',(14,6),(14,13));self.relate('connect','valve-top','valve-neck');self.relate('connect','valve','valve-neck')
        self.circle('timer',33,16,9)
        self.add_polyline('hands',(33,11),(33,16),(37,16))
        self.add_line('hose',(17,13),(24,13));self.relate('connect','hose','valve')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
