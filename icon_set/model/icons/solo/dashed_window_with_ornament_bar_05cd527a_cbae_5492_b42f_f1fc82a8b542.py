"""Dashed interface boundary with attached ornament toolbar. Wide envelope; Lucide rounded corner construction, fewer larger dashes to retain clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '05cd527a-cbae-5492-b42f-f1fc82a8b542'
SOURCE_PATH = 'pictographic-primitives/technology/element ornament_05cd527a-cbae-5492-b42f-f1fc82a8b542.svg'
AUTHOR = 'gpt-6'

class DashedWindowWithOrnamentBar(Solo48):
    icon_id = 'dashed-window-with-ornament-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('window', 'ornament', 'toolbar', 'dashed', 'spatial', 'interface', 'placeholder')

    def build(self):
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        line('tl-top',(10,8),(14,8));arc('tl',(4, 14),(10,8),6)
        line('tl-side',(4, 20),(4, 14));contour('top-left','tl-side','tl','tl-top')
        line('tr-top',(34,8),(38,8));arc('tr',(38,8),(44, 14),6)
        line('tr-side',(44, 14),(44, 20));contour('top-right','tr-top','tr','tr-side')
        self.add_dot('top-dash',(24,8))
        arc('bl',(4, 30),(10,36),6,sweep=False);line('bl-end',(10,36),(14,36));contour('bottom-left','bl','bl-end')
        arc('br',(38,36),(44, 30),6,sweep=False);line('br-start',(34,36),(38,36));contour('bottom-right','br-start','br')
        box('ornament',14,30,34,40,5);connect('ornament','bottom-left');connect('ornament','bottom-right')
