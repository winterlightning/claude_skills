"""A camera equipment bag with an arched handle, flap and central square clasp. Square envelope makes room for the handle and fastening. Lucide briefcase-business informs the rounded body and handle. The flap remains horizontal as in the source; the clasp is enlarged for a readable opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '878f75ee-f692-5e74-bed8-420c0b6b91ad'
SOURCE_PATH = 'pictographic-primitives/photography/photography equipment bag_878f75ee-f692-5e74-bed8-420c0b6b91ad.svg'
AUTHOR = 'gpt-6'

class CameraEquipmentBag(Solo48):
    icon_id = 'camera-equipment-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('bag', 'camera bag', 'equipment', 'case', 'briefcase', 'photography', 'travel', 'gear')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
            for j,p in enumerate(pts):arc(n+'-'+str(j),p,pts[(j+1)%4],r)
            contour(n,*[n+'-'+str(j) for j in range(4)],closed=True)

        segments('top',(10,16),(16,16),(32,16),(38,16))
        arc('tr',(38,16),(42,20),4)
        segments('right',(42,20),(42,25),(42,38));arc('br',(42,38),(38,42),4)
        line('bottom',(38,42),(10,42));arc('bl',(10,42),(6,38),4)
        segments('left',(6,38),(6,25),(6,20));arc('tl',(6,20),(10,16),4)
        contour('body','top-1','top-2','top-3','tr','right-1','right-2','br','bottom','bl','left-1','left-2','tl',closed=True)
        arc('handle',(16,16),(32,16),8,10);connect('handle','body')
        poly('clasp',(20,25),(28,25),(28,33),(20,33),closed=True)
        line('flap-left',(6,25),(20,25));line('flap-right',(28,25),(42,25))
        for n in ('flap-left','flap-right'):connect(n,'body');connect(n,'clasp')
