"""A tilted umbrella reflector linked to a round lamp head on a pole and horizontal foot. Vertical envelope fits the lighting stand. Lucide umbrella informs the smooth canopy arc; camera circle construction informs the lamp. Fine canopy ribs are omitted; diagonal shaft and horizontal foot retain the equipment identity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb34016b-5118-528f-b9e3-14ec7d2307ad'
SOURCE_PATH = 'pictographic-primitives/photography/photography equipment light umbrella_eb34016b-5118-528f-b9e3-14ec7d2307ad.svg'
AUTHOR = 'gpt-6'

class UmbrellaLampStand(Solo48):
    icon_id = 'umbrella-lamp-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('umbrella light', 'lamp', 'studio', 'lighting', 'stand', 'reflector', 'photography', 'equipment')

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

        arc('canopy-left',(12,36),(16,8),20)
        arc('canopy-top',(16,8),(40,8),20)
        contour('canopy','canopy-left','canopy-top')
        poly('canopy-edge',(40,8),(28,20),(12,36));connect('canopy-edge','canopy')
        poly('shaft',(16,8),(28,20),(36,28));connect('shaft','canopy');connect('shaft','canopy-edge')
        circle('lamp',36,32,4);connect('shaft','lamp')
        line('pole',(36,36),(36,44));connect('pole','lamp')
        poly('foot',(26,44),(36,44),(40,44));connect('foot','pole')
