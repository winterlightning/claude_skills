'Cellar doors: symmetrical semicircular arch, shared center seam, and paired round handles.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c536474-4cfa-4c4a-bf71-7af160b27cb6'
SOURCE_PATH = 'pictographic-primitives/building/cellar_0c536474-4cfa-4c4a-bf71-7af160b27cb6.svg'
AUTHOR = 'gpt-6'

class Cellar(Solo48):
    icon_id = 'cellar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('cellar', 'building')

    def build(self) -> None:
        # Square envelope: two quarter arches share the door seam at x=24.
        self.add_line('left',(6,42),(6,24))
        self.add_arc('arch-left',(6,24),(24,6),radius_x=18)
        self.add_arc('arch-right',(24,6),(42,24),radius_x=18)
        self.add_line('right',(42,24),(42,42))
        self.add_line('base-a',(42,42),(24,42))
        self.add_line('base-b',(24,42),(6,42))
        self.add_contour('doors','left','arch-left','arch-right','right','base-a','base-b',closed=True)
        self.add_line('seam',(24,6),(24,42))
        self.relate('connect','seam','doors')
        for x in (15,33): self.add_dot('handle-'+str(x),(x,28))
