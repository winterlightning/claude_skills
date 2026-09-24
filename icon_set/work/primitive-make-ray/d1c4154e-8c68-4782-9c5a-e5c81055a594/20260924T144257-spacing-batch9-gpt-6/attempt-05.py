"""file-with-shield-plus: Reduce clipped corner, rebalance shield height and plus placement; keep all defining components.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape SQUARE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='d1c4154e-8c68-4782-9c5a-e5c81055a594'
SOURCE_PATH='pictographic-primitives/other/file with shield plus_d1c4154e-8c68-4782-9c5a-e5c81055a594.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='file-with-shield-plus'
    keyshape=Keyshape.SQUARE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('file-with-shield-plus',)
    def build(self):
        self.add_polyline('page',(6,42),(6,6),(40,6),(42,10),(42,42),closed=True)
        self.add_line('shield-top',(15,15),(33,15))
        self.add_bezier('shield-right',(33,15),((33,27),(33,30),(24,33)))
        self.add_bezier('shield-left',(24,33),((15,30),(15,27),(15,15)))
        self.add_contour('shield','shield-top','shield-right','shield-left',closed=True)
        self.add_polyline('plus-h',(23,24),(24,24),(25,24))
        self.add_polyline('plus-v',(24,23),(24,24),(24,25))
        self.relate('connect','plus-h','plus-v')

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
