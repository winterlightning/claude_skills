"""Computer Microchip Processor.
Symbol plan: Rounded square chip with eight pins derived from one symmetric edge definition.
Reference construction: cpu.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '91baab07-2434-44bf-b597-92da30445815'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/safety helmet mine_91baab07-2434-44bf-b597-92da30445815.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rounded-square-microchip-with-eight-pins'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('microchip', 'processor', 'pins', 'circuit', 'chip', 'computer', 'hardware', 'electronics')
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
        for i in range(4):
         def turn(p):
          x,y=p[0]-24,p[1]-24
          for _ in range(i):x,y=-y,x
          return (24+x,24+y)
         pts=[turn(p) for p in ((16,12),(20,12),(28,12),(32,12))]
         poly('side'+str(i),*pts)
         arc('corner'+str(i),pts[-1],turn((36,16)),4)
         for j,x in enumerate((20,28)):line('pin'+str(i)+str(j),turn((x,6)),turn((x,12)))
        contour('chip',*(n for i in range(4) for n in ('side'+str(i)+'-1','side'+str(i)+'-2','side'+str(i)+'-3','corner'+str(i))),closed=True)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
