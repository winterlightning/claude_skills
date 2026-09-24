"""mail-card-bug: Merge outer card and envelope silhouette at shared shoulders to remove parallel overlap. Rebalance flap height; omit bug divider, lower legs and envelope seams.
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape SQUARE; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='0b79dbcd-029c-4c05-baad-34d720b23be7'
SOURCE_PATH='pictographic-primitives/other/mail card bug_0b79dbcd-029c-4c05-baad-34d720b23be7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mail-card-bug'
    keyshape=Keyshape.SQUARE
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mail-card-bug',)
    def build(self):
        self.add_polyline('outline',(9,29),(9,6),(39,6),(39,29),(42,29),(42,42),(6,42),(6,29),closed=True)
        self.add_polyline('flap',(9,29),(18,34),(30,34),(39,29))
        self.relate('connect','outline','flap')
        pts=[(21,16),(27,16),(29,20),(27,24),(21,24),(19,20)]
        for j,a in enumerate(pts):self.add_arc('bug-'+str(j),a,pts[(j+1)%6],radius_x=5)
        self.add_contour('bug',*('bug-'+str(j) for j in range(6)),closed=True)
        for j,(a,b) in enumerate([((21,16),(19,14)),((27,16),(29,14)),((19,20),(17,20)),((29,20),(31,20))]):
            self.add_line('leg-'+str(j),a,b)
            self.relate('connect','leg-'+str(j),'bug')

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
