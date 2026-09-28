"""Side-view delivery truck with cargo box, angled cab, and two wheels joined to the undercarriage. Local Lucide truck original and atomic debug informed the body and wheel attachment."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shipping-delivery-truck-solo/20260927T172707Z-thuan-mac-1/reference/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'shipping-delivery-truck-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'shipping delivery truck')
    def build(self):
        # Wheels meet the undercarriage at shared centerline points, as in the source.
        nodes=((6,25),(6,6),(26,6),(26,16),(35,16),(42,25),
               (34,25),(14,25),(6,25))
        for j,(a,b) in enumerate(zip(nodes,nodes[1:]),1):
            self.add_line(f'shell-{j}',a,b)
        self.add_contour('shell',*(f'shell-{j}' for j in range(1,len(nodes))),closed=True)
        self.add_line('cab-divider',(26,16),(26,25))
        self.relate('connect','shell','cab-divider')
        for name,x in (('rear',14),('front',34)):
            points=((x,34),(x+4,38),(x,42),(x-4,38),(x,34))
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_arc(f'{name}-wheel-{j}',a,b,radius_x=4)
            self.add_contour(f'{name}-wheel',*(f'{name}-wheel-{j}' for j in range(1,5)),closed=True)
            self.add_line(f'{name}-axle',(x,25),(x,34))
            self.relate('connect','shell',f'{name}-axle')
            self.relate('connect',f'{name}-wheel',f'{name}-axle')
