"""Wired gamepad with mirrored rounded grips and cable. Square envelope; Lucide gamepad-2 silhouette; four tiny buttons reduced to a primary button."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c69120b9-fb56-4d39-958a-ffba357a9fbe'
SOURCE_PATH = 'pictographic-primitives/technology/gaming control_c69120b9-fb56-4d39-958a-ffba357a9fbe.svg'
AUTHOR = 'gpt-6'

class WiredGameController(Solo48):
    icon_id = 'wired-game-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('controller', 'gamepad', 'wired', 'cable', 'game', 'gaming', 'console')

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
        line('top',(14,12),(24,12));line('top-right',(24,12),(34,12))
        arc('tr',(34,12),(42,20),8)
        line('right',(42,20),(42,36))
        arc('grip-r',(42,36),(30,36),6)
        arc('notch',(30,36),(18,36),6,3,sweep=False)
        arc('grip-l',(18,36),(6,36),6)
        line('left',(6,36),(6,20))
        arc('tl',(6,20),(14,12),8)
        contour('body','top','top-right','tr','right','grip-r','notch','grip-l','left','tl',closed=True)
        line('cable',(24,12),(24,6));connect('cable','body')
        poly('dpad-h',(15,23),(18,23),(21,23));poly('dpad-v',(18,21),(18,23),(18,25));connect('dpad-h','dpad-v')
        self.add_dot('button',(32,23))

SOURCE_REFERENCES = [('30480c32-ffee-4a42-94da-a19f1a2e9d2f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/joystick_30480c32-ffee-4a42-94da-a19f1a2e9d2f.svg')]
