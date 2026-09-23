from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd9177fba-2a20-515e-81aa-43f5ec22aeda'
SOURCE_PATH = 'pictographic-primitives/work/task list to do_d9177fba-2a20-515e-81aa-43f5ec22aeda.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'to-do-list-with-checkmarks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('tasks', 'checklist')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rounded_rect(self, name, x0, y0, x1, y1, r):
        pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}'
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(eid,a,b,radius_x=r)
            else: self.add_line(eid,a,b)
            ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: rounded page enclosing two repeated checks, one open task circle and three text rules.
        # VRECT_L centerline extremes (8,4)-(40,44). Preserve all rows; dense source remains a review candidate.
        self.rounded_rect('page',8,4,40,44,4)
        for i,y in enumerate((14,25)):
            self.add_polyline(f'check-{i}',(16,y),(19,y+3),(24,y-3))
            self.add_line(f'text-{i}',(31,y),(32,y))
        self.circle('unchecked',19,36,3)
        self.add_line('text-2',(30,36),(32,36))
