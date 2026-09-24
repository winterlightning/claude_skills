"""circle-skull-xmark: Visual review rejected eye-free reduction as headphone-like. Restore identifying eyes; enlarge dome and rebalance cheeks. Preserve readable skull and report spacing blocker rather than approve reduced silhouette.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape CIRCLE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH='pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-skull-xmark'
    keyshape=Keyshape.CIRCLE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('circle-skull-xmark',)
    def build(self):
        self.circle('ring',24,24,20)
        self.add_arc('dome',(13,23),(35,23),radius_x=11)
        self.add_bezier('right-cheek',(35,23),((35,28),(32,28),(32,30)))
        self.add_line('right-jaw',(32,30),(32,32))
        self.add_line('left-jaw',(16,32),(16,30))
        self.add_bezier('left-cheek',(16,30),((16,28),(13,28),(13,23)))
        self.add_contour('skull','left-jaw','left-cheek','dome','right-cheek','right-jaw')
        self.add_line('tooth',(24,31),(24,34))
        self.add_dot('eye-left',(20,23))
        self.add_dot('eye-right',(28,23))
        self.add_line('bone-left',(16,32),(13,35))
        self.add_line('bone-right',(32,32),(35,35))
        self.relate('connect','bone-left','skull')
        self.relate('connect','bone-right','skull')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,l,t,r,b,rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,z,radius_x=rad)
            else:self.add_line(n+str(i),a,z)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def house(self):
        self.add_polyline('house',(6,42),(6,18),(24,6),(42,18),(42,42),closed=True)
    def page(self):
        self.add_polyline('page',(8,44),(8,4),(28,4),(40,16),(40,44),closed=True)
