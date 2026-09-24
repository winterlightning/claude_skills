"""circle-skull-xmark: Rebalance shorter bone rays toward center; retain skull and xmark, omit eye specks and tooth separator to enlarge interior.
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
        self.add_arc('dome',(16,22),(32,22),radius_x=8)
        self.add_line('cheek-r',(32,22),(32,25))
        self.add_polyline('jaw',(32,25),(29,28),(29,32),(19,32),(19,28),(16,25))
        self.add_line('cheek-l',(16,25),(16,22))
        self.relate('connect','jaw','cheek-r')
        self.relate('connect','jaw','cheek-l')
        self.relate('connect','dome','cheek-l')
        self.relate('connect','dome','cheek-r')
        self.add_line('bone-l',(16,22),(16,16))
        self.add_line('bone-r',(32,22),(32,16))
        self.add_line('bone-bl',(19,28),(16,33))
        self.add_line('bone-br',(29,28),(32,33))
        self.relate('connect','bone-l','dome')
        self.relate('connect','bone-l','cheek-l')
        self.relate('connect','bone-r','dome')
        self.relate('connect','bone-r','cheek-r')
        self.relate('connect','bone-bl','jaw')
        self.relate('connect','bone-br','jaw')

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
