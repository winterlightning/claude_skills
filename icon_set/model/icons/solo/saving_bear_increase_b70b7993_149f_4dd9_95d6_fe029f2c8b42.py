from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b70b7993-149f-4dd9-95d6-fe029f2c8b42'
SOURCE_PATH = 'icon_set/work/todo-references/saving bear increase_b70b7993-149f-4dd9-95d6-fe029f2c8b42.svg'
AUTHOR = 'gpt-6'
# Plan: Bear head below a rising financial arrow; ears and muzzle mirror around x=26.
# Reference: No exact local Lucide bear match; smooth lobes and coherent financial arrow.
# Reduction: Omitted tiny muzzle crease while retaining split muzzle and two ears.

class AuthoredIcon(Solo48):
    icon_id = 'saving-bear-increase'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('saving', 'bear', 'increase')

    def build(self):
        self.add_polyline('trend',(6,23),(18,11),(30,13),(42,6))
        self.add_polyline('arrow',(34,6),(42,6),(42,14));self.relate('connect','trend','arrow')
        self.add_bezier('bear',(16,25),((12,18),(20,17),(22,23)),((25,22),(29,22),(32,23)),((35,17),(41,19),(38,26)),((45,37),(38,42),(27,42)),((16,42),(10,37),(16,25)))
        self.add_bezier('muzzle',(22,40),((22,28),(32,28),(32,40)),((29,42),(25,42),(22,40)))
        self.add_polyline('nose',(27,36),(27,39),(24,41));self.relate('connect','nose','muzzle')

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
