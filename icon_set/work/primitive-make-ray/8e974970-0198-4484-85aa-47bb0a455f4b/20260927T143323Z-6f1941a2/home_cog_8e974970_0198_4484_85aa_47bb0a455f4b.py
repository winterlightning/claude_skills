"""Revision of the claimed reference after comparing original and rejected drawing."""
"""home-cog: Raise eaves to enlarge opening above smooth cog; omitted tiny hub speck.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape SQUARE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='8e974970-0198-4484-85aa-47bb0a455f4b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__home-cog/20260927T142529Z-thuan-mac-1/reference/home cog_8e974970-0198-4484-85aa-47bb0a455f4b.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='home-cog'
    keyshape=Keyshape.SQUARE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('home-cog',)
    def build(self):
        # Angular teeth make the inset gear read as a cog rather than a flower.
        self.add_polyline('house',(6,42),(6,16),(24,6),(42,16),(42,42),closed=True)
        pts=((22,17),(26,17),(27,20),(30,19),(33,22),(31,25),(33,28),(30,31),(27,30),(26,34),(22,34),(21,30),(18,31),(15,28),(17,25),(15,22),(18,19),(21,20))
        self.add_polyline('cog',*pts,closed=True)

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
