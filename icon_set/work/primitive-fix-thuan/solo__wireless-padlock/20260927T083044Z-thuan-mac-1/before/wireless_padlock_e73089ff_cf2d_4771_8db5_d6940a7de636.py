"""Wireless padlock with paired signal waves. Square envelope, centerline extremes 6/6/42/42. Lucide lock-keyhole informs shackle and rounded body; one wave per side replaces two and blank lock face is retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e73089ff-cf2d-4771-8db5-d6940a7de636'
SOURCE_PATH = 'pictographic-primitives/technology/smart lock lock wireless_e73089ff-cf2d-4771-8db5-d6940a7de636.svg'
AUTHOR = 'gpt-6'

class WirelessPadlock(Solo48):
    icon_id = 'wireless-padlock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('padlock', 'lock', 'wireless', 'smart-lock', 'security', 'signal', 'connected')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x+r,y),r)
            arc(n+'b',(x+r,y),(x,y+r),r)
            arc(n+'c',(x,y+r),(x-r,y),r)
            arc(n+'d',(x-r,y),(x,y-r),r)
            contour(n,n+'a',n+'b',n+'c',n+'d',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        chain('body-top',(14,28),(16,28),(32,28),(34,28))
        arc('body-tr',(34,28),(38,32),4);line('body-r',(38,32),(38,38));arc('body-br',(38,38),(34,42),4)
        line('body-b',(34,42),(14,42));arc('body-bl',(14,42),(10,38),4);line('body-l',(10,38),(10,32));arc('body-tl',(10,32),(14,28),4)
        contour('body','body-top-1','body-top-2','body-top-3','body-tr','body-r','body-br','body-b','body-bl','body-l','body-tl',closed=True)
        arc('shackle',(16,28),(32,28),8,12);connect('shackle','body')
        arc('left-top',(14,6),(6,18),8,12,sweep=False)
        arc('right-top',(34,6),(42,18),8,12)
