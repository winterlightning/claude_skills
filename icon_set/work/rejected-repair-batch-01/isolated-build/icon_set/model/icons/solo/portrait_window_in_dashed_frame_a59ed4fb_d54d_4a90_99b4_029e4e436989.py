"""Portrait window within dashed layout boundary. Square envelope; rounded window and broad corner dashes; small perimeter dashes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a59ed4fb-d54d-4a90-99b4-029e4e436989'
SOURCE_PATH = 'pictographic-primitives/technology/element presentation 1_a59ed4fb-d54d-4a90-99b4-029e4e436989.svg'
AUTHOR = 'gpt-6'

class PortraitWindowInDashedFrame(Solo48):
    icon_id = 'portrait-window-in-dashed-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('window', 'presentation', 'dashed', 'frame', 'spatial', 'interface', 'element')

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
        for n,l,t,r,b in [('tl',6,6,12,12),('tr',36,6,42,12),('bl',6,36,12,42),('br',36,36,42,42)]:
            if n=='tl':arc(n,(l,b),(r,t),6)
            if n=='tr':arc(n,(l,t),(r,b),6)
            if n=='bl':arc(n,(r,b),(l,t),6)
            if n=='br':arc(n,(r,t),(l,b),6)
        box('portrait',17,15,31,33,3)
