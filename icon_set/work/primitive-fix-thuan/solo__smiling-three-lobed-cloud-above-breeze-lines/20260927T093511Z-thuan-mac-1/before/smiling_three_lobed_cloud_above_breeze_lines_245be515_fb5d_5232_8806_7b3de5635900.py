"""Smiling Cloud with Breeze.
Symbol plan: Three-lobed cloud with simple smile above one broad breeze stroke.
Reference construction: cloud.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '245be515-fb5d-5232-8806-7b3de5635900'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/air quality_245be515-fb5d-5232-8806-7b3de5635900.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'smiling-three-lobed-cloud-above-breeze-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('cloud', 'smile', 'breeze', 'air', 'weather', 'face', 'wind', 'ecology')
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
        arc('top-left',(14,16),(24,6),10)
        arc('top-right',(24,6),(34,16),10)
        arc('right',(34,16),(34,32),8,8)
        line('base',(34,32),(14,32))
        arc('left',(14,32),(14,16),8,8)
        contour('cloud','top-left','top-right','right','base','left',closed=True)
        arc('smile',(20,22),(28,22),4,1,sweep=False)
        arc('air',(12,42),(36,42),12,1)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
