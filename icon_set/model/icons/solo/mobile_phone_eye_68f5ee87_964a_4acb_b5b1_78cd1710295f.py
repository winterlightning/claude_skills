"""mobile-phone-eye: Visual repair: flatten mirrored lids to source almond proportions; no pupil because source eye is empty.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape VRECT_L; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='68f5ee87-964a-4acb-b5b1-78cd1710295f'
SOURCE_PATH='pictographic-primitives/other/mobile phone eye_68f5ee87-964a-4acb-b5b1-78cd1710295f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-eye'
    keyshape=Keyshape.VRECT_L
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('mobile-phone-eye',)
    def build(self):
        self.add_polyline('phone',(8,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')
        self.add_bezier('eye',(17,20),((21,14),(27,14),(31,20)),((27,26),(21,26),(17,20)))
        self.add_contour('eye-outline','eye',closed=True)

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
