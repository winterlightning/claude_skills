from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '936d0079-3089-4c8c-bc22-422921c13e69'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg'
AUTHOR = 'gpt-6'
# Plan: Charging bull silhouette with a curved horn and upward trend arrow behind its back.
# Reference: No useful exact local Lucide bull match; supplied reference controls asymmetric animal pose.
# Reduction: Omitted minor rear-leg crease; retained horn, head, body, legs, tail and trend.

class AuthoredIcon(Solo48):
    icon_id = 'saving-bull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('saving', 'bull')

    def build(self):
        # Broad charging-bull body, two open leg strokes, curved horn and rising arrow.
        self.add_bezier('back-front',(8,28),((14,24),(16,22),(22,22)))
        self.add_bezier('back-rear',(22,22),((28,22),(30,26),(36,26)))
        self.add_arc('rump-top',(36,26),(40,30),radius_x=4)
        self.add_arc('rump-bottom',(40,30),(36,34),radius_x=4)
        self.add_line('belly-right',(36,34),(28,34))
        self.add_line('belly-left',(28,34),(20,34))
        self.add_bezier('chin',(20,34),((16,34),(12,40),(8,36)))
        self.add_line('muzzle',(8,36),(8,28))
        self.add_contour('animal','back-front','back-rear','rump-top','rump-bottom','belly-right','belly-left','chin','muzzle',closed=True)
        self.add_bezier('horn',(8,28),((4,28),(4,22),(4,18)))
        self.relate('connect','horn','animal')
        for name,x in [('front',28),('rear',36)]:
            self.add_line(name+'-leg',(x,34),(x,40));self.relate('connect','animal',name+'-leg')
        self.add_polyline('tail',(40,30),(44,34),(44,40));self.relate('connect','tail','animal')
        self.add_line('trend',(36,16),(44,8))
        self.add_polyline('arrow',(36,8),(44,8),(44,16));self.relate('connect','trend','arrow')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
