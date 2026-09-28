from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7313c8ec-d635-4b38-acd5-fea39286b43e'
SOURCE_PATH = 'icon_set/work/todo-references/card game dice_7313c8ec-d635-4b38-acd5-fea39286b43e.svg'
AUTHOR = 'gpt-6'

PLAN = 'Two suit cards and foreground die; restore the reference two-pip face and enlarge the die opening.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/7313c8ec-d635-4b38-acd5-fea39286b43e/20260922T222321-2443bd/result.json'

class Drawing(Solo48):
    icon_id = 'card-game-dice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('playing', 'cards', 'and', 'dice')

    def build(self):
        # Diamond card at left, spade card behind, and a two-pip die in foreground. Each closed symbol has its own contents; overlaps use visible interrupted contours. Square extremes (4,4)-(44,44).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        self.add_polyline('left-card',(18,34),(12,42),(6,16),(20,10),(24,24))
        self.add_polyline('back-card',(20,10),(24,6),(42,10),(38,24))
        rounded('die',18,24,42,42,3)
        self.relate('connect','die','left-card')
        self.relate('connect','die','back-card')
        self.relate('connect','left-card','back-card')
        self.add_polyline('diamond',(15,21),(20,25),(16,31),(11,27),closed=True)
        self.add_line('spade-top-1',(28,18),(32,12))
        self.add_line('spade-top-2',(32,12),(36,18))
        self.add_arc('spade-right',(36,18),(32,20),radius_x=3)
        self.add_arc('spade-left',(32,20),(28,18),radius_x=3)
        self.add_contour('spade','spade-top-1','spade-top-2','spade-right','spade-left',closed=True)
        self.add_line('stem',(32,20),(32,23))
        self.relate('connect','stem','spade')
        for j,x in enumerate((26,34)): self.add_dot(f'pip-{j}',(x,33))
