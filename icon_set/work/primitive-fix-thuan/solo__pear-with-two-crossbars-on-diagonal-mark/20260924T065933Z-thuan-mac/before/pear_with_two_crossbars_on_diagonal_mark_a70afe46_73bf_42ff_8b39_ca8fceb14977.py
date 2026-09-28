"""Genetically Modified Pear.
Symbol plan: Pear silhouette with narrowed neck and two diagonal crossbars; meaning of mark left unresolved.
Reference construction: leaf.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a70afe46-73bf-42ff-8b39-ca8fceb14977'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/gmo food pear_a70afe46-73bf-42ff-8b39-ca8fceb14977.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'pear-with-two-crossbars-on-diagonal-mark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('pear', 'fruit', 'leaf', 'stem', 'genetic', 'crossbars', 'mark', 'uncertain')
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
        arc('neck-left',(14,18),(24,8),10)
        arc('neck-right',(24,8),(34,18),10)
        arc('shoulder-right-a',(34,18),(37,25),3,7,sweep=False)
        arc('shoulder-right-b',(37,25),(40,32),3,7)
        arc('base-right',(40,32),(24,44),16,12)
        arc('base-left',(24,44),(8,32),16,12)
        arc('shoulder-left-a',(8,32),(11,25),3,7)
        arc('shoulder-left-b',(11,25),(14,18),3,7,sweep=False)
        contour('pear','neck-left','neck-right','shoulder-right-a','shoulder-right-b','base-right','base-left','shoulder-left-a','shoulder-left-b',closed=True)
        line('stem',(24,8),(24,4))
        poly('mark',(21,26),(22,27),(28,33),(29,34))
        poly('bar-a',(20,29),(22,27),(24,25))
        poly('bar-b',(26,35),(28,33),(30,31))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
