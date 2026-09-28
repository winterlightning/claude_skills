"""heart-romance: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '724cec2d-4e21-444d-b8dc-15e8d8bedd82'
SOURCE_PATH = 'pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class HeartRomance(Solo48):
    icon_id = 'heart-romance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('romance', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('heart', 'romance')

    def build(self):
        # Plan: HRECT_L; paired circular lobes and mirrored point; remove conversion kinks.
        # Reference: Lucide heart: rounded lobes flow into deliberate pointed base.
        axis = 24
        self.add_bezier('left-inner',(axis,13),((21,10),(18,8),(14,8)))
        self.add_arc('left-lobe',(14,8),(4,18),radius_x=10,sweep=False)
        self.add_bezier('left-lower',(4,18),((4,23),(6.5,25),(10,28)))
        self.add_line('left-point',(10,28),(axis,40))
        self.add_line('right-point',(axis,40),(38,28))
        self.add_bezier('right-lower',(38,28),((41.5,25),(44,23),(44,18)))
        self.add_arc('right-lobe',(44,18),(34,8),radius_x=10,sweep=False)
        self.add_bezier('right-inner',(34,8),((30,8),(27,10),(axis,13)))
        self.add_contour('outline','left-inner','left-lobe','left-lower','left-point','right-point','right-lower','right-lobe','right-inner',closed=True)
