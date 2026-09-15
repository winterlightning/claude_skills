"""Keypad door lever lock: portrait plate, control slot, projecting handle. Lucide smartphone rounded plate; tiny hub rings and band divisions omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20902ef7-ce54-4369-a83e-5e2e7192fa55'
SOURCE_PATH = 'pictographic-primitives/technology/door password lock_20902ef7-ce54-4369-a83e-5e2e7192fa55.svg'
AUTHOR = 'gpt-6'

class DoorLeverKeypadLock(Solo48):
    icon_id = 'door-lever-keypad-lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('door-lock', 'lever', 'handle', 'keypad', 'password', 'security', 'door', 'smart-lock')

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
        box('plate',8,4,26,44,6)
        line('keypad',(17,14),(17,20))
        line('lever',(17,32),(40,32))
        connect('lever','plate')
