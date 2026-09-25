"""Wilting Drooping Flower.
Symbol plan: Bent stem supports a drooping bell, with two pointed leaves at unequal heights.
Reference construction: flower-2 and sprout.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9796dff7-75cb-5d84-8c49-749d9f71c50a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/global warming dead plant_9796dff7-75cb-5d84-8c49-749d9f71c50a.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'wilting-bell-flower-with-two-drooping-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    aliases = ()
    keywords = ('flower', 'wilting', 'drooping', 'stem', 'leaves', 'plant', 'nature', 'ecology')
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
        arc('stem-bend',(16,14),(34,14),9,8)
        poly('stem',(16,14),(16,22),(16,32),(16,42))
        arc('bell-top-left',(26,18),(34,14),8,4)
        arc('bell-top-right',(34,14),(42,18),8,4)
        poly('bell',(26,18),(28,26),(40,26),(42,18))
        arc('leaf-left-a',(16,22),(6,36),10,14,sweep=False)
        arc('leaf-left-b',(6,36),(16,22),10,14,sweep=False)
        contour('left-leaf','leaf-left-a','leaf-left-b',closed=True)
        arc('leaf-right-a',(16,32),(32,42),16,10)
        arc('leaf-right-b',(32,42),(16,32),16,10)
        contour('right-leaf','leaf-right-a','leaf-right-b',closed=True)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
