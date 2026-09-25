"""Computer CPU Microchip.
Symbol plan: Processor board with square core, three left and bottom pins and two right blocks.
Reference construction: cpu.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5f237f9f-a39c-5e92-9ba3-322f7c30a4e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/mini computer board_5f237f9f-a39c-5e92-9ba3-322f7c30a4e6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rounded-processor-board-with-square-core-and-side-blocks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('processor', 'board', 'chip', 'pins', 'core', 'contacts', 'computer', 'electronics')
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
        line('top',(12,6),(30,6))
        arc('top-right',(30,6),(34,10),4)
        poly('right',(34,10),(34,18),(34,26),(34,34))
        poly('bottom',(34,34),(30,34),(22,34),(14,34),(12,34))
        arc('bottom-left',(12,34),(8,30),4)
        poly('left',(8,30),(8,22),(8,14),(8,10))
        arc('top-left',(8,10),(12,6),4)
        contour('board','top','top-right','right-1','right-2','right-3','bottom-1','bottom-2','bottom-3','bottom-4','bottom-left','left-1','left-2','left-3','top-left',closed=True)
        rect('core',17,15,8,8)
        for i,y in enumerate((14,22,30)):line('pin-left'+str(i),(6,y),(8,y))
        for i,x in enumerate((14,22,30)):line('pin-bottom'+str(i),(x,34),(x,42))
        for i,y in enumerate((10,26)):poly('block'+str(i),(34,y),(42,y),(42,y+8),(34,y+8))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
