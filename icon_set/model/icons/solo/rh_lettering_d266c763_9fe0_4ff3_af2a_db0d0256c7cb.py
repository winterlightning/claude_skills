from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd266c763-9fe0-4ff3-af2a-db0d0256c7cb'
SOURCE_PATH = 'icon_set/work/todo-references/Rh_d266c763-9fe0-4ff3-af2a-db0d0256c7cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rh-lettering'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('Rh',)

    def build(self):
        # R uses one semicircular bowl, h one arch. Uprights share baseline 38.
        baseline=38
        self.add_line('r-stem',(4,baseline),(4,10))
        self.add_line('r-top',(4,10),(12,10))
        self.add_arc('r-upper',(12,10),(20,18),radius_x=8)
        self.add_arc('r-lower',(20,18),(12,26),radius_x=8)
        self.add_line('r-return',(12,26),(4,26))
        self.add_contour('r','r-stem','r-top','r-upper','r-lower','r-return')
        self.add_line('r-leg',(12,26),(22,baseline))
        self.relate('connect','r','r-leg')
        self.add_polyline('h-stem',(32,10),(32,28),(32,baseline))
        self.add_arc('h-arch',(32,28),(44,28),radius_x=6)
        self.add_line('h-right',(44,28),(44,baseline))
        self.add_contour('h-shoulder','h-arch','h-right')
        self.relate('connect','h-stem','h-shoulder')
