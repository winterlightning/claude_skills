from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '945b25be-2ad9-4b54-9548-b41ff357244a'
SOURCE_PATH = 'icon_set/work/todo-references/signal slash_945b25be-2ad9-4b54-9548-b41ff357244a.svg'
AUTHOR = 'gpt-6'
# Plan: Circular wireless signal crossed by a diagonal slash, with broadcast arcs and a dot.
# Construction references: signal plus concentric wireless arc principles; source is wireless, not bar signal.
# Reduction: Reduced outer ring to two arcs around slash clearance; two wireless arcs and dot retained.

class AuthoredIcon(Solo48):
    icon_id = 'signal-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('signal', 'slash')

    def build(self):
        self.circle('ring',24,24,18)
        self.add_bezier('wave-top',(14,19),((21,13),(31,15),(36,21)))
        self.add_bezier('wave-bottom',(19,26),((24,21),(29,23),(32,27)))
        self.circle('dot',24,34,3)
        self.add_line('slash',(6,6),(42,42))
        self.relate('connect','slash','ring')
        self.relate('connect','slash','wave-top');self.relate('connect','slash','wave-bottom')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
