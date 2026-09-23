from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '090386bc-ec29-43fe-9dba-5fd9ed1f0f5e'
SOURCE_PATH = 'icon_set/work/todo-references/scooter parking shade roof_090386bc-ec29-43fe-9dba-5fd9ed1f0f5e.svg'
AUTHOR = 'gpt-6'
# Plan: Scooter under a pitched shelter roof; two wheels, seat, body and steering column.
# Reference: bike: shared wheel radii and baseline; no useful scooter shelter match.
# Reduction: Omitted tiny seat seam; preserved shelter, seat, scooter body, handle and both wheels.

class AuthoredIcon(Solo48):
    icon_id = 'scooter-parking-shade-roof'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('scooter', 'parking', 'shade', 'roof')

    def build(self):
        self.add_polyline('roof',(4,18),(24,8),(44,18))
        for n,x in [('rear-wheel',13),('front-wheel',36)]:self.circle(n,x,36,4)
        self.add_line('deck',(8,32),(40,32))
        self.add_bezier('body',(8,32),((8,24),(21,24),(21,32)))
        self.relate('connect','body','deck')
        self.add_polyline('seat',(10,25),(9,22),(20,22),(21,25))
        self.add_polyline('steering',(29,22),(33,22),(36,32));self.relate('connect','steering','deck')
        self.add_arc('front-fender',(29,32),(43,32),radius_x=7)
        self.relate('connect','front-fender','deck')
        for n in ('rear-wheel','front-wheel'):self.relate('connect',n,'deck')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
