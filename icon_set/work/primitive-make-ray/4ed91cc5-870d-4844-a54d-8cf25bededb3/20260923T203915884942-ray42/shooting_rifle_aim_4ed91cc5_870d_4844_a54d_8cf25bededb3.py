from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4ed91cc5-870d-4844-a54d-8cf25bededb3'
SOURCE_PATH = 'icon_set/work/todo-references/shooting rifle aim_4ed91cc5-870d-4844-a54d-8cf25bededb3.svg'
AUTHOR = 'gpt-6'
# Plan: Rifle silhouette crosses a concentric target with vertical sight marks.
# Construction references: No useful exact local Lucide rifle match; concentric circles and straight sight axes.
# Reduction: Reduced target to two rings; retained stock, barrel, trigger and crosshair.

class AuthoredIcon(Solo48):
    icon_id = 'shooting-rifle-aim'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shooting', 'rifle', 'aim')

    def build(self):
        self.circle('target',24,24,18)
        self.circle('inner',24,24,10)
        self.add_polyline('rifle',(6,24),(24,24),(28,23),(42,23))
        self.add_polyline('stock',(6,24),(6,32),(18,28),(28,28),(30,23))
        self.relate('connect','rifle','stock')
        self.add_arc('trigger',(19,28),(23,28),radius_x=2,sweep=False);self.relate('connect','trigger','stock')
        self.add_line('sight-top',(24,6),(24,16));self.add_line('sight-bottom',(24,33),(24,42))
        self.relate('connect','sight-top','target');self.relate('connect','sight-top','inner');self.relate('connect','sight-bottom','target');self.relate('connect','sight-bottom','inner')

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
