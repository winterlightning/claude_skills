"""A large standing customer faces a smaller attendant behind a horizontal desk line. Both figures have circular heads and rounded shoulders, while the foreground customer's body tapers downward.
Symbol plan: Standing customer faces a bust attendant behind the desk. Both heads use radius 4; customer neck (12,22) and attendant shoulder crown (34,28) yield exactly 4 ink gap. Shared human references supply stick and bust anatomy; omit clothing outlines and attendant chest line.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: human_ref/full_body_ref.png; human_ref/user.svg. Lucide original and atomic-debug renders inspected where named.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6c38d9c8-0e42-5dd8-a256-2b9b12046c18'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__customer-at-information-desk/20260927T032242Z-thuan-mac-1/reference/information desk customer_6c38d9c8-0e42-5dd8-a256-2b9b12046c18.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'customer-at-information-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'companies'
    categories = ('primitives', 'companies')
    aliases = ()
    keywords = ('customer', 'at', 'information', 'desk')

    def build(self) -> None:
        # Larger outlined customer at left, smaller attendant behind a desk.
        for name,x,y,r in (('customer-head',12,10,4),('attendant-head',34,18,4)):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_polyline('customer-body',(8,42),(8,34),(6,34),(6,28),(10,22),(16,22),(20,28),(20,34),(18,34),(18,42))
        self.add_bezier('attendant-shoulder-left',(28,36),((29,32),(32,30),(34,30)))
        self.add_bezier('attendant-shoulder-right',(34,30),((37,30),(40,32),(42,36)))
        self.add_contour('attendant-body','attendant-shoulder-left','attendant-shoulder-right')
        self.add_polyline('desk',(28,36),(42,36),(42,42))
        self.relate('connect','attendant-body','desk')

