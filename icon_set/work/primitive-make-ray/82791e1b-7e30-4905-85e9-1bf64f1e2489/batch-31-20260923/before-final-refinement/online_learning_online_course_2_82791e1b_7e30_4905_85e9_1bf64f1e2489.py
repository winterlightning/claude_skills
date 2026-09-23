from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH = 'icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR = 'gpt-6'
PLAN = 'Open book above a course entry field. Mirror the pages about x=24; the field owns its centered rule.'
CONSTRUCTION_REFERENCES = 'book-open: paired pages and center binding; monitor: rounded enclosure.'
OMISSIONS = 'Page curvature simplified; field rule retained.'

class Drawing(Solo48):
    icon_id = 'online-learning-online-course-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('online', 'learning', 'online', 'course', '2')

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
        self.add_polyline('pages',(10,6),(18,6),(24,10),(30,6),(38,6),(38,14),(30,14),(24,18),(18,14),(10,14),closed=True)
        self.add_line('binding',(24,10),(24,18));self.relate('connect','pages','binding')
        self.add_polyline('entry',(6,26),(42,26),(42,42),(6,42),closed=True)
        self.add_line('entry-rule',(16,34),(32,34))
