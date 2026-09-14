"""AWD drivetrain label; narrow letters preserve the single-line reading. HRECT_L ink (6,6)-(42,42). Lucide type informs monoline lettering; D uses small left corners and larger right corners; the W right stem leans to provide curve clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '971034e0-d3cc-5cee-b6c3-07b486f7f0d4'
SOURCE_PATH = 'pictographic-primitives/transportation/all wheel drive_971034e0-d3cc-5cee-b6c3-07b486f7f0d4.svg'
AUTHOR = 'gpt-6'

class AwdTextLabel(Solo48):
    icon_id = 'awd-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('awd', 'all wheel drive', 'drivetrain', 'car', 'dashboard', 'text', 'label', '4x4')

    def build(self) -> None:
        self.add_polyline('a-outline',(6,40),(6,12),(8,8),(12,12),(12,40))
        self.add_line('a-bar',(6,25),(12,25))
        self.relate('connect','a-outline','a-bar')
        self.add_polyline('w',(20,8),(20,40),(24,29),(27,40),(28,8))
        self.add_line('d-left',(36,38),(36,10))
        self.add_arc('d-tl',(36,10),(38,8),radius_x=2)
        self.add_arc('d-tr',(38,8),(42,14),radius_x=6)
        self.add_line('d-right',(42,14),(42,34))
        self.add_arc('d-br',(42,34),(38,40),radius_x=6)
        self.add_arc('d-bl',(38,40),(36,38),radius_x=2)
        self.add_contour('d','d-left','d-tl','d-tr','d-right','d-br','d-bl',closed=True)
