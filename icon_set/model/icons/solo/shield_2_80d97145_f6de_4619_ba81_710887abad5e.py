from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80d97145-f6de-4619-ba81-710887abad5e'
SOURCE_PATH = 'icon_set/work/todo-references/shield 2_80d97145-f6de-4619-ba81-710887abad5e.svg'
AUTHOR = 'gpt-6'
# Plan: Plain shield with gently arched upper rim and rounded pointed base.
# Construction references: shield: equal side curves; crown deliberately softer than shield 1.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shield-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('shield', '2')

    def build(self):
        self.add_bezier('top',(8,8),((13,6),(19,4),(24,4)),((29,4),(35,6),(40,8)))
        self.add_line('right',(40,8),(40,24))
        self.add_bezier('bottom',(40,24),((40,34),(32,40),(24,44)),((16,40),(8,34),(8,24)))
        self.add_line('left',(8,24),(8,8))
        self.add_contour('outline','top','right','bottom','left',closed=True)

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
