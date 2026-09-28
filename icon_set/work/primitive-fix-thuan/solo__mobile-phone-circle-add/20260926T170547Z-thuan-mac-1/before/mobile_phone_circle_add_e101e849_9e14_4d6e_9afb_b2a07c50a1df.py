"""mobile-phone-circle-add: Omit redundant circle to enlarge plus symbol. Phone separator and plus junctions share actual emitted vertices.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape VRECT_L; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e101e849-9e14-4d6e-9afb-b2a07c50a1df'
SOURCE_PATH='pictographic-primitives/other/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-circle-add'
    keyshape=Keyshape.VRECT_L
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases=()
    keywords=('mobile-phone-circle-add',)
    def build(self):
        self.add_polyline('phone',(8,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')
        self.add_polyline('plus-h',(18,20),(24,20),(30,20))
        self.add_polyline('plus-v',(24,14),(24,20),(24,26))
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
