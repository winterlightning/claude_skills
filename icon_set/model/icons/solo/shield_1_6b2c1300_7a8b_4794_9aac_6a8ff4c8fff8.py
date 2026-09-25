from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b2c1300-7a8b-4794-9aac-6a8ff4c8fff8'
SOURCE_PATH = 'icon_set/work/todo-references/shield 1_6b2c1300-7a8b-4794-9aac-6a8ff4c8fff8.svg'
AUTHOR = 'gpt-6'
# Plan: Plain shield with angled upper rim and a softly pointed base.
# Construction references: shield: symmetric tapered sides and coherent base curves.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shield-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('shield', '1')

    def build(self):
        self.add_polyline('upper',(8,22),(8,10),(24,4),(40,10),(40,22))
        self.add_bezier('base',(40,22),((40,33),(33,40),(24,44)),((15,40),(8,33),(8,22)))
        self.relate('connect','upper','base')

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
