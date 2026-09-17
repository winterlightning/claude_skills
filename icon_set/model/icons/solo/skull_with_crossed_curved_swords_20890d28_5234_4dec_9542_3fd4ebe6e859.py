from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20890d28-5234-4dec-9542-3fd4ebe6e859'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy_20890d28-5234-4dec-9542-3fd4ebe6e859.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'skull-with-crossed-curved-swords'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('skull', 'swords', 'pirate', 'piracy', 'emblem', 'blade', 'crossed', 'bones')

    def build(self):
        # Plan: mirrored skull with two dots; crossed sword segments emerge behind it.
        # Centerline envelope: (6,6)-(42,42). Reference: Lucide skull and swords: circular crown, eye dots, paired guards.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        self.add_arc('crown',(11,19),(37,19),radius_x=13)
        path('jaw',(37,19),(37,23),(29,27),(29,31),(19,31),(19,27),(11,23),(11,19))
        self.add_contour('skull','crown',*[f'jaw-{i}' for i in range(1,8)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='jaw']
        for x in (20,28):self.add_dot('eye-'+str(x),(x,18))
        for side in (-1,1):
            def p(x,y):return(24+side*x,y)
            self.add_line('blade-'+str(side),p(18,6),p(13,19));join('blade-'+str(side),'skull')
            self.add_line('handle-'+str(side),p(5,31),p(16,42));join('handle-'+str(side),'skull')
            self.add_line('guard-'+str(side),p(7,42),p(16,33));join('guard-'+str(side),'handle-'+str(side))
