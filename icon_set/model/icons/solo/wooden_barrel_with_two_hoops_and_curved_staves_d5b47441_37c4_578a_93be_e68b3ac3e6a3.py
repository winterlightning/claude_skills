"""Wooden Storage Barrel.

Symbol plan: Mirrored barrel silhouette and two hoops; retain one central stave to keep broad openings.
Keyshape VRECT_L: visible ink extremes (6, 2, 42, 46); stroke centerlines inset 2.
Lucide construction reference: barrel.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5b47441-37c4-578a-93be-e68b3ac3e6a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/wine barrel_d5b47441-37c4-578a-93be-e68b3ac3e6a3.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'wooden-barrel-with-two-hoops-and-curved-staves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/drink"
    aliases = ()
    keywords = ('barrel', 'wood', 'storage', 'staves', 'hoops', 'cask', 'container', 'drink')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        poly('top',(12,4),(24,4),(36,4))
        arc('right-top',(36,4),(40,16),20,20)
        line('right-mid',(40,16),(40,32))
        arc('right-bottom',(40,32),(36,44),20,20)
        poly('bottom',(36,44),(24,44),(12,44))
        arc('left-bottom',(12,44),(8,32),20,20)
        line('left-mid',(8,32),(8,16))
        arc('left-top',(8,16),(12,4),20,20)
        contour('body','top-1','top-2','right-top','right-mid','right-bottom','bottom-1','bottom-2','left-bottom','left-mid','left-top',closed=True)
        for y in (16,32): poly('hoop'+str(y),(8,y),(24,y),(40,y))
        poly('stave',(24,4),(24,16),(24,32),(24,44))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)
