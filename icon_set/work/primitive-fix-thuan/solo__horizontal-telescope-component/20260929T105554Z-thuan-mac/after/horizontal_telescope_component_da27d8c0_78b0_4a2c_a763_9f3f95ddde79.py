"""distro for opentelemetry preview.
Symbol plan: HRECT_L (4,8)-(44,40). Horizontal stepped optical tube, rim atx36, and signal trace with a shared peak at24,24. Simplify fine waveform oscillations.
Lucide telescope original and atomic-debug: stepped tube and lens rim. Supplied original: horizontal barrel above waveform.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'da27d8c0-78b0-4a2c-a763-9f3f95ddde79'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-telescope-component/20260929T105554Z-thuan-mac/reference/distro for opentelemetry preview_da27d8c0-78b0-4a2c-a763-9f3f95ddde79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-telescope-component'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horizontal', 'telescope', 'component')
    
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


        path('barrel',(4,12),(16,12),(20,8),(36,8),(44,8),(44,24),(36,24),(24,24),(20,24),(16,20),(4,20),closed=True)
        line('rim',(36,8),(36,24));connect('rim','barrel')
        path('signal',(4,36),(14,36),(24,24),(32,40),(38,36),(44,36));connect('signal','barrel')

