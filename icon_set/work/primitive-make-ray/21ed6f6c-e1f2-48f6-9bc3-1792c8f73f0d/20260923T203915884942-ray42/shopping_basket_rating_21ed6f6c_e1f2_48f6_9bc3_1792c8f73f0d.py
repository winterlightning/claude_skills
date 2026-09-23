from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '21ed6f6c-e1f2-48f6-9bc3-1792c8f73f0d'
SOURCE_PATH = 'icon_set/work/todo-references/shopping basket rating_21ed6f6c-e1f2-48f6-9bc3-1792c8f73f0d.svg'
AUTHOR = 'gpt-6'
# Plan: Shopping basket beneath three rating stars, with the middle star raised.
# Construction references: No exact useful Lucide rating match; shared star definition and mirrored basket sides.
# Reduction: Reduced basket ribs to two; retained three stars and both handles.

class AuthoredIcon(Solo48):
    icon_id = 'shopping-basket-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shopping', 'basket', 'rating')

    def build(self):
        for n,x,y in [('left',11,16),('center',24,11),('right',37,16)]:
            self.add_polyline(n,(x,y-5),(x+2,y-1),(x+5,y-1),(x+3,y+2),(x+4,y+5),(x,y+3),(x-4,y+5),(x-3,y+2),(x-5,y-1),(x-2,y-1),closed=True)
        self.add_line('rim',(8,29),(40,29))
        self.add_polyline('basket',(10,29),(14,42),(34,42),(38,29));self.relate('connect','basket','rim')
        for n,a,b in [('left',(15,29),(19,23)),('right',(33,29),(29,23))]:self.add_line(n+'-handle',a,b);self.relate('connect',n+'-handle','rim')
        for x in (20,28):self.add_line('rib-'+str(x),(x,34),(x,38))

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
