"""Arduino Microcontroller Board.
Symbol plan: Notched circuit board with left edge connector and a separate square component.
Reference construction: circuit-board.
HRECT_L visible extremes: (2, 6, 46, 42); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2f61b4f-015b-5959-9ee4-0640251a986e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/arduino circuit_c2f61b4f-015b-5959-9ee4-0640251a986e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'notched-microcontroller-board-with-edge-connector'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/electronics'
    aliases = ()
    keywords = ('microcontroller', 'board', 'circuit', 'connector', 'component', 'arduino', 'hardware', 'electronics')
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
        line('top',(14,8),(36,8))
        arc('corner-tr',(36,8),(40,12),4)
        poly('right',(40,12),(40,16),(44,20),(44,30),(40,34),(40,36))
        arc('corner-br',(40,36),(36,40),4)
        line('bottom',(36,40),(14,40))
        arc('corner-bl',(14,40),(10,36),4)
        line('left-lower',(10,36),(10,28))
        line('left-upper',(10,20),(10,12))
        arc('corner-tl',(10,12),(14,8),4)
        contour('board','left-upper','corner-tl','top','corner-tr','right-1','right-2','right-3','right-4','right-5','corner-br','bottom','corner-bl','left-lower')
        poly('connector',(10,20),(4,20),(4,28),(10,28),(16,28),(16,20),(10,20))
        rect('component',24,18,8,8)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
