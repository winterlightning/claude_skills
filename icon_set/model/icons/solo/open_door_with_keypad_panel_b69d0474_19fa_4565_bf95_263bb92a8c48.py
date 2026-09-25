"""Open door leaf, frame and attached keypad panel. Square envelope; Lucide door-open perspective and shared hinge/frame structure. Blank panel retained as in the reference; no cramped keys added."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b69d0474-19fa-4565-bf95-263bb92a8c48'
SOURCE_PATH = 'pictographic-primitives/technology/keycode unlock door_b69d0474-19fa-4565-bf95-263bb92a8c48.svg'
AUTHOR = 'gpt-6'

class OpenDoorWithKeypadPanel(Solo48):
    icon_id = 'open-door-with-keypad-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('door', 'open', 'keypad', 'unlock', 'access', 'entry', 'smart-lock')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
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
        poly('door',(6,6),(20,14),(20,34),(20,42),(6,34),closed=True)
        poly('frame',(6,6),(30,6),(30,23));connect('frame','door')
        line('sill',(20,34),(30,34));connect('sill','door')
        line('panel-top',(33,20),(39,20));arc('panel-tr',(39,20),(42,23),3)
        line('panel-right',(42,23),(42,35));arc('panel-br',(42,35),(39,38),3)
        line('panel-bottom',(39,38),(33,38));arc('panel-bl',(33,38),(30,35),3)
        chain('panel-left',(30,35),(30,34),(30,23));arc('panel-tl',(30,23),(33,20),3)
        contour('keypad','panel-top','panel-tr','panel-right','panel-br','panel-bottom','panel-bl','panel-left-1','panel-left-2','panel-tl',closed=True)
        connect('frame','keypad');connect('sill','keypad')
