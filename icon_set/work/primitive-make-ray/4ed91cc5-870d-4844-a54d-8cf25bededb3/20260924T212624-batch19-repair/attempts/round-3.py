from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4ed91cc5-870d-4844-a54d-8cf25bededb3'
SOURCE_PATH = 'pictographic-primitives/sports/shooting rifle aim_4ed91cc5-870d-4844-a54d-8cf25bededb3.svg'
AUTHOR = "gpt-6"
# Plan: Rifle silhouette crosses a concentric target with vertical sight marks.
# Construction references: No useful exact local Lucide rifle match; concentric circles and straight sight axes.
# Reduction: Reduced target to two rings; retained stock, barrel, trigger and crosshair.

class AuthoredIcon(Solo48):
    icon_id = 'shooting-rifle-aim'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shooting', 'rifle', 'aim')

    def build(self):
        # Rifle interrupts the lower-left target ring instead of crossing it.
        self.add_arc('target-ul',(10,24),(26,8),radius_x=16)
        self.add_arc('target-ur',(26,8),(42,24),radius_x=16)
        self.add_contour('target-upper','target-ul','target-ur')
        self.add_arc('target-lower',(42,24),(26,40),radius_x=16)
        self.add_polyline('rifle',(4,24),(10,24),(26,24),(42,24),(44,24))
        self.add_polyline('stock',(4,24),(4,34),(16,34),(26,24))
        self.relate('connect','rifle','stock')
        self.relate('connect','rifle','target-upper');self.relate('connect','rifle','target-lower')
        self.add_line('sight-top',(26,8),(26,15))
        self.relate('connect','sight-top','target-upper')


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
