from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '59f997a9-32d8-436a-ae34-06535681b16e'
SOURCE_PATH = 'icon_set/work/todo-references/shipment approve smartphone_59f997a9-32d8-436a-ae34-06535681b16e.svg'
AUTHOR = 'gpt-6'
# Plan: Parcel cube behind a smartphone with an approval tick and bottom home mark.
# Construction references: package: three visible faces with a shared center seam; rounded phone contour.
# Reduction: Omitted box seam hidden behind phone; retained tick and home mark.

class AuthoredIcon(Solo48):
    icon_id = 'shipment-approve-smartphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shipment', 'approve', 'smartphone')

    def build(self):
        self.add_polyline('box-top',(6,12),(18,6),(30,12),(18,19),closed=True)
        self.add_polyline('box-left',(6,12),(6,27),(18,34),(18,19))
        self.relate('connect','box-top','box-left')
        self.add_line('box-edge',(30,12),(30,16));self.relate('connect','box-top','box-edge')
        self.box('phone',26,21,42,42,3)
        self.add_polyline('check',(30,29),(33,32),(38,27))
        self.add_line('home',(32,37),(36,37))

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
