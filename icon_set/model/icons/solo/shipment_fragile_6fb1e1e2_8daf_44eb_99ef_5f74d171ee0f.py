from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f'
SOURCE_PATH = 'icon_set/work/todo-references/shipment fragile_6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f.svg'
AUTHOR = 'gpt-6'
# Plan: Fragile parcel with top packing ribbon, wine-glass handling symbol and upward arrow.
# Construction references: package and wine: clear folded tape and bowl/stem construction.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shipment-fragile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shipment', 'fragile')

    def build(self):
        self.box('box',6,6,42,42,3)
        self.add_polyline('tape',(18,6),(18,17),(24,13),(30,17),(30,6));self.relate('connect','tape','box')
        self.add_line('glass-rim-1',(15,24),(23,24))
        self.add_line('glass-rim-2',(23,24),(23,29))
        self.add_arc('glass-bowl',(23,29),(15,29),radius_x=4)
        self.add_line('glass-left',(15,29),(15,24))
        self.add_contour('glass','glass-rim-1','glass-rim-2','glass-bowl','glass-left',closed=True)
        self.add_line('stem',(19,33),(19,37));self.relate('connect','stem','glass')
        self.add_line('foot',(16,37),(22,37));self.relate('connect','stem','foot')
        self.add_line('arrow-shaft',(33,36),(33,24));self.add_polyline('arrow-head',(29,28),(33,24),(37,28));self.relate('connect','arrow-shaft','arrow-head')

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
