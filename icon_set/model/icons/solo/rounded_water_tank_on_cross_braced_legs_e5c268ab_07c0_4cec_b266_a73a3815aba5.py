"""Water Tower Structure.
Symbol plan: Rounded water tank above a shared pair of splayed legs and crossed braces.
Reference construction: none.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5c268ab-07c0-4cec-b266-a73a3815aba5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/water protection tower_e5c268ab-07c0-4cec-b266-a73a3815aba5.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rounded-water-tank-on-cross-braced-legs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    aliases = ()
    keywords = ('water', 'tower', 'tank', 'braces', 'storage', 'structure', 'legs', 'utility')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
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
        arc('roof',(12,14),(36,14),12,10)
        poly('tank',(12,14),(12,26),(36,26),(36,14))
        line('top-band',(8,14),(40,14))
        line('lower-band',(8,26),(40,26))
        poly('leg-left',(12,26),(10,35),(8,44))
        poly('leg-right',(36,26),(38,35),(40,44))
        poly('brace-left',(10,35),(24,39),(40,44))
        poly('brace-right',(38,35),(24,39),(8,44))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
