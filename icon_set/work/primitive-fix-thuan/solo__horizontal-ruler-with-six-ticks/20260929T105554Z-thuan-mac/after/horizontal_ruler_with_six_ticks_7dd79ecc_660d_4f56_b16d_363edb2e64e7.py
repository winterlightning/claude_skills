"""ruler horizontal.
Symbol plan: HRECT_M (4,10)-(44,38), shallowest allowed envelope. Four ticks spaced8 centerline units replace six crowded source marks; alternating6 and12 lengths.
Lucide ruler original and atomic-debug: edge-attached graduation marks and rounded outer corners. Original horizontal orientation retained.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7dd79ecc-660d-4f56-b16d-363edb2e64e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-ruler-with-six-ticks/20260929T105554Z-thuan-mac/reference/ruler horizontal_7dd79ecc-660d-4f56-b16d-363edb2e64e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-ruler-with-six-ticks'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horizontal', 'ruler', 'with', 'six', 'ticks')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        line('top',(6,10),(42,10));arc('tr',(42,10),(44,12),2)
        line('right',(44,12),(44,36));arc('br',(44,36),(42,38),2)
        xs=(42,36,28,20,12,6)
        for i in range(5):line('bottom-'+str(i+1),(xs[i],38),(xs[i+1],38))
        arc('bl',(6,38),(4,36),2);line('left',(4,36),(4,12));arc('tl',(4,12),(6,10),2)
        contour('frame','top','tr','right','br',*[f'bottom-{i}' for i in range(1,6)],'bl','left','tl',closed=True)
        for i,x in enumerate((12,20,28,36)):
            line('tick-'+str(i),(x,38),(x,26 if i%2==0 else 32));connect('tick-'+str(i),'frame')

