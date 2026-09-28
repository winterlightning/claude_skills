"""lgbt-heart: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = 'pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LgbtHeart(Solo48):
    icon_id = 'lgbt-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('lgbt', 'heart', 'symbol')

    def build(self):
        # Plan: HRECT_L; mirrored lobes, level bands and exact attachment nodes.
        # Reference: Lucide heart: matched lobe construction; source bands preserved.
        self.add_bezier('left-inner',(24,14),((21,10),(18,8),(14,8)))
        self.add_arc('left-lobe',(14,8),(4,20),radius_x=10,radius_y=12,sweep=False)
        self.add_bezier('left-shoulder',(4,20),((4,23),(7,25),(10,28)))
        self.add_line('left-point',(10,28),(24,40))
        self.add_line('right-point',(24,40),(38,28))
        self.add_bezier('right-shoulder',(38,28),((41,25),(44,23),(44,20)))
        self.add_arc('right-lobe',(44,20),(34,8),radius_x=10,radius_y=12,sweep=False)
        self.add_bezier('right-inner',(34,8),((30,8),(27,10),(24,14)))
        self.add_contour('outline','left-inner','left-lobe','left-shoulder','left-point','right-point','right-shoulder','right-lobe','right-inner',closed=True)
        self.add_line('upper-band',(4,20),(44,20))
        self.add_line('lower-band',(10,28),(38,28))
        self.relate('connect','upper-band','outline')
        self.relate('connect','lower-band','outline')
