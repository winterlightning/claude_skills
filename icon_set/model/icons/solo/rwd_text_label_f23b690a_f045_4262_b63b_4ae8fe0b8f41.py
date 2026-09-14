from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f23b690a-f045-4262-b63b-4ae8fe0b8f41'
SOURCE_PATH = 'pictographic-primitives/transportation/rear wheel drive_f23b690a-f045-4262-b63b-4ae8fe0b8f41.svg'
AUTHOR = 'gpt-6'

class RwdTextLabel(Solo48):
    icon_id = 'rwd-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('rwd', 'rear wheel drive', 'drivetrain', 'car', 'dashboard', 'text', 'label', 'transmission')

    def build(self):
        self.add_polyline('r-stem',(4,40),(4,24),(4,8),(8,8))
        self.add_arc('r-bowl',(8,8),(8,24),radius_x=4,radius_y=8,sweep=True)
        self.add_line('r-middle',(8,24),(4,24))
        self.add_line('r-leg',(4,24),(12,40))
        self.relate('connect','r-stem','r-bowl')
        self.relate('connect','r-stem','r-middle')
        self.relate('connect','r-bowl','r-middle')
        self.relate('connect','r-stem','r-leg')
        self.relate('connect','r-middle','r-leg')
        self.add_polyline('w',(20,8),(21,40),(24,24),(27,40),(28,8))
        self.add_line('d-stem',(37,40),(37,8))
        self.add_arc('d-bowl',(37,8),(37,40),radius_x=7,radius_y=16,sweep=True)
        self.add_contour('d','d-stem','d-bowl',closed=True)
