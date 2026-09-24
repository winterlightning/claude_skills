"""circle-skull-1: Enlarge dome; rebalance jaw. Eye strokes reduced to dots, or omitted when crowded; skull dome and three jaw prongs preserved.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape CIRCLE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='0275d46c-9a52-48fb-9993-9a0c2a0a4b89'
SOURCE_PATH='pictographic-primitives/other/circle skull 1_0275d46c-9a52-48fb-9993-9a0c2a0a4b89.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-skull-1'
    keyshape=Keyshape.CIRCLE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('circle-skull-1',)
    def build(self):
        self.circle('ring',24,24,20)
        self.add_arc('dome',(13,24),(35,24),radius_x=11)
        self.add_line('right-cheek',(35,24),(32,29))
        self.add_line('right-jaw',(32,29),(32,32))
        self.add_line('left-jaw',(16,32),(16,29))
        self.add_line('left-cheek',(16,29),(13,24))
        self.add_contour('skull','left-jaw','left-cheek','dome','right-cheek','right-jaw')
        self.add_line('mouth',(24,31),(24,34))

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
