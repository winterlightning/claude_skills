"""heart-user: Human reference user.svg; exact head bottom to shoulder apex gap8. Enlarge heart lower opening, rebalance person and try taller keyshape; preserve head and shoulders.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape SQUARE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e7e97355-bccb-465c-ae55-5037fd70d291'
SOURCE_PATH='pictographic-primitives/other/heart user_e7e97355-bccb-465c-ae55-5037fd70d291.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='heart-user'
    keyshape=Keyshape.SQUARE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('heart-user',)
    def build(self):
        self.add_bezier('lobe-li',(24,10),((22,6),(20,6),(15,6)))
        self.add_arc('lobe-lo',(15,6),(6,15),radius_x=9)
        self.add_bezier('flank-l',(6,15),((6,35),(6,35),(24,42)))
        self.add_bezier('flank-r',(24,42),((42,35),(42,35),(42,15)))
        self.add_arc('lobe-ro',(42,15),(33,6),radius_x=9,sweep=False)
        self.add_bezier('lobe-ri',(33,6),((28,6),(26,6),(24,10)))
        self.add_contour('heart','lobe-li','lobe-lo','flank-l','flank-r','lobe-ro','lobe-ri',closed=True)
        self.circle('head',24,21,4)
        self.add_arc('shoulders',(19,38),(29,38),radius_x=5)

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
