"""A closed diagonal safety pin with rounded spring and hooked clasp; double coil reduced to one loop."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8f5f092-e7e9-4e0f-ad55-5ae52fcdd2e9'
SOURCE_PATH = 'pictographic-primitives/tools/safety pin_e8f5f092-e7e9-4e0f-ad55-5ae52fcdd2e9.svg'
AUTHOR = 'gpt-6'

class SafetyPin(Solo48):
    icon_id = 'safety-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('safety pin', 'pin', 'clasp', 'sewing', 'fastener', 'clothing', 'attach', 'diaper')

    def build(self) -> None:
        self.add_line('wire-left',(6,30),(30,6))
        self.add_arc('clasp',(30,6),(42,18),radius_x=12)
        self.add_line('wire-right',(42,18),(18,42))
        self.add_arc('spring',(18,42),(6,30),radius_x=12)
        self.add_contour('outline','wire-left','clasp','wire-right','spring',closed=True)
        self.add_polyline('clasp-hook',(30,6),(30,16),(36,16),(36,24))
        self.relate('connect','clasp-hook','outline')
        self.add_arc('coil',(6,30),(18,42),radius_x=12,sweep=True)
        self.relate('connect','coil','outline')
