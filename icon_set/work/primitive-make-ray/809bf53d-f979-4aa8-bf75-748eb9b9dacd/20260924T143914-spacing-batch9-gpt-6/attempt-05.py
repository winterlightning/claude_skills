"""circle-bluetooth: Enlarge Bluetooth triangular openings and rebalance inside circular enclosure; genuine shared central rune junction.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape CIRCLE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='809bf53d-f979-4aa8-bf75-748eb9b9dacd'
SOURCE_PATH='pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-bluetooth'
    keyshape=Keyshape.CIRCLE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('circle-bluetooth',)
    def build(self):
        self.circle('ring',24,24,20)
        self.add_polyline('rune',(16,17),(24,24),(16,31))
        self.add_polyline('upper',(24,24),(20,11),(34,18),(24,24))
        self.add_polyline('lower',(24,24),(34,30),(20,37),(24,24))
        self.relate('connect','rune','upper')
        self.relate('connect','rune','lower')
        self.relate('connect','upper','lower')

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
