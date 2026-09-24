from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a1b8b06-db68-40b2-adfe-7ecac75aaa72'
SOURCE_PATH = 'icon_set/work/todo-references/shoemaker_4a1b8b06-db68-40b2-adfe-7ecac75aaa72.svg'
AUTHOR = 'gpt-6'
# Plan: Shoemaker with a circular head, apron and a shoe in the lower right foreground.
# Construction references: human_ref/user.svg and full_body_ref.png: circular head and broad smooth shoulders; no exact shoe match.
# Reduction: Omitted small apron side seam; retained apron, shoulder outline and shoe.

class AuthoredIcon(Solo48):
    icon_id = 'shoemaker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shoemaker',)

    def build(self):
        self.circle('head',20,13,7)
        self.add_bezier('torso',(20,28),((9,28),(6,31),(6,38)))
        self.add_bezier('shoulder-right',(20,28),((31,28),(34,30),(34,34)));self.relate('connect','torso','shoulder-right')
        self.add_line('left-side',(6,38),(6,42));self.relate('connect','torso','left-side')
        self.add_polyline('apron',(14,28),(14,34),(11,42),(22,42))
        self.relate('connect','apron','torso')
        self.add_bezier('shoe',(23,42),((23,35),(23,35),(29,37)),((33,39),(32,33),(36,36)),((38,39),(42,37),(42,42)))
        self.add_line('sole',(42,42),(23,42));self.relate('connect','sole','shoe')
        self.mark_human_figure('shoemaker',head='head',torso='torso',torso_junction='start')

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
