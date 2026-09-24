"""mobile-phone-fingerprint: Widen phone keyshape and reduce fingerprint to arch, two outer tails and center ridge. Remove extra crowded curls; actual arc/tail endpoints are connected.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape SQUARE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='0ef09a66-6578-497b-817b-f821ad82e177'
SOURCE_PATH='pictographic-primitives/other/mobile phone fingerprint_0ef09a66-6578-497b-817b-f821ad82e177.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-fingerprint'
    keyshape=Keyshape.SQUARE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mobile-phone-fingerprint',)
    def build(self):
        self.add_polyline('phone',(6,6),(42,6),(42,36),(42,42),(6,42),(6,36),closed=True)
        self.add_line('separator',(6,36),(42,36))
        self.relate('connect','phone','separator')
        self.add_arc('outer-ridge',(15,24),(33,24),radius_x=9)
        self.add_line('left-tail',(15,28),(15,24))
        self.add_line('right-tail',(33,24),(33,28))
        self.relate('connect','outer-ridge','left-tail')
        self.relate('connect','outer-ridge','right-tail')
        self.add_line('inner-ridge',(24,24),(24,28))

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
