"""Twin Towers with Connecting Bridge.

Symbol plan: Two mirrored pointed towers joined by a broad bridge. Drop narrow upper tiers and facade ticks.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide building-2: sparse facades and shared building attachments; reference supplies paired spires.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49935e36-084e-59cc-8f7a-3108d62113bc'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture twin building_49935e36-084e-59cc-8f7a-3108d62113bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-towers-with-connecting-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        for j,x in enumerate((6,30)):
            path('tower-'+str(j),(x,42),(x,16),(x+6,6),(x+12,16),(x+12,26),(x+12,34),(x+12,42),(x,42),closed=True)
        # Split the inner left wall of the right tower at both bridge nodes.
        self.contours.pop()
        self.primitives=[p for p in self.primitives if not p.element_id.startswith('tower-1-')]
        path('tower-1',(30,42),(30,34),(30,26),(30,16),(36,6),(42,16),(42,42),(30,42),closed=True)
        for j,y in enumerate((26,34)):
            line('bridge-'+str(j),(18,y),(30,y))
            connect('bridge-'+str(j),'tower-0');connect('bridge-'+str(j),'tower-1')
