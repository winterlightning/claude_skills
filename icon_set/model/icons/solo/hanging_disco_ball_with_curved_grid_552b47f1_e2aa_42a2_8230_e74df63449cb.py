"""A gridded disco ball hangs from a short cord. VRECT_L 8..40 x4..44 supports sphere radius16 centered24,28 and cord4..12. Source supplies sphere, curved meridians and hanging cord; Lucide globe supplies quarter-circle and meridian construction. Mirror elliptical meridians about x24; split equator at actual surface-grid intersections. Omit two extra horizontal bands to retain open cells."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '552b47f1-e2aa-42a2-8230-e74df63449cb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/disco_552b47f1-e2aa-42a2-8230-e74df63449cb.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'hanging-disco-ball-with-curved-grid'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Hanging Disco Ball with Curved Grid']
    keywords = ['disco', 'ball', 'hanging', 'grid', 'sphere', 'dance', 'mirror']
    def build(self):
        self.add_line('cord',(24,4),(24,12))
        points=[(24,12),(40,28),(24,44),(8,28),(24,12)]
        for j in range(4):
            self.add_arc('sphere-'+str(j),points[j],points[j+1],radius_x=16)
        self.add_contour('sphere',*[f'sphere-{j}' for j in range(4)],closed=True)
        self.relate('connect','cord','sphere')
        for side in (-1,1):
            x=24+side*8;n='meridian-'+str(side)
            self.add_arc(n+'-top',(24,12),(x,28),radius_x=8,radius_y=16,sweep=side>0)
            self.add_arc(n+'-bottom',(x,28),(24,44),radius_x=8,radius_y=16,sweep=side>0)
            self.add_contour(n,n+'-top',n+'-bottom')
            self.relate('connect',n,'sphere','cord')
        self.relate('connect','meridian--1','meridian-1')
        xs=(8,16,32,40)
        for j in range(3):
            self.add_line('equator-'+str(j),(xs[j],28),(xs[j+1],28))
        self.add_contour('equator','equator-0','equator-1','equator-2')
        self.relate('connect','equator','sphere','meridian--1','meridian-1')
