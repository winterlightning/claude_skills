"""Complete floating interface window with integral ornament toolbar and lower baseline. Lucide smartphone rounded corners; structural UI treated as one solo subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6f72285-8383-5eda-aeb5-2c86f3adb877'
SOURCE_PATH = 'pictographic-primitives/technology/element ornament_b6f72285-8383-5eda-aeb5-2c86f3adb877.svg'
AUTHOR = 'gpt-6'

class WindowWithOrnamentBar(Solo48):
    icon_id = 'window-with-ornament-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('window', 'ornament', 'toolbar', 'display', 'spatial', 'interface', 'screen')

    def build(self):
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
        line('top',(10,8),(38,8));arc('tr',(38,8),(42,14),6)
        line('right',(42,14),(42,20));arc('br',(42,20),(38,26),6)
        line('bottom-r',(38,26),(34,26))
        box('ornament',14,21,34,31,5)
        line('bottom-l',(14,26),(10,26));arc('bl',(10,26),(6,20),6)
        line('left',(6,20),(6,14));arc('tl',(6,14),(10,8),6)
        contour('window','bottom-l','bl','left','tl','top','tr','right','br','bottom-r')
        connect('window','ornament')
        line('base',(19,40),(29,40))
