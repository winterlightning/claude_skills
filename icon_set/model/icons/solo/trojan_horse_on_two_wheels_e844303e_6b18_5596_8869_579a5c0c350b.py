from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e844303e-6b18-5596-8869-579a5c0c350b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/troy horse_e844303e-6b18-5596-8869-579a5c0c350b.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'trojan-horse-on-two-wheels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('horse', 'trojan', 'wheels', 'wooden', 'vehicle', 'toy', 'history', 'animal')

    def build(self):
        # Plan: angular horse profile above two equal wheels; shared axle, right-facing neck.
        # Centerline envelope: (6,6)-(42,42). Reference: Lucide truck: equal outlined wheels; no useful horse match.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('horse',(14,28),(14,18),(24,18),(26,6),(38,6),(36,11),(42,18),(34,18),(34,28))
        self.add_line('belly',(14,28),(34,28));join('horse','belly')
        path('tail',(14,18),(6,26));join('tail','horse')
        for x in (14,34):
            circle('wheel-'+str(x),x,39,3)
            self.add_line('leg-'+str(x),(x,28),(x,36));join('leg-'+str(x),'horse');join('leg-'+str(x),'belly');join('leg-'+str(x),'wheel-'+str(x))
        self.add_line('axle',(17,39),(31,39))
        for x in (14,34):join('axle','wheel-'+str(x))
