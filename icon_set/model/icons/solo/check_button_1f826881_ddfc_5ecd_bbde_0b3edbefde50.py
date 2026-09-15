'Check button: centered check with a longer rising stroke and consistent rounded corners. Lucide circle-check informs the mark.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f826881-ddfc-5ecd-bbde-0b3edbefde50'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check button_1f826881-ddfc-5ecd-bbde-0b3edbefde50.svg'
AUTHOR = 'gpt-6'

class CheckButton(Solo48):
    icon_id = 'check-button'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'button', 'interface-essential')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 8, 44, 40, 4
        self.add_line('outline-top', (left+radius,top), (right-radius,top))
        self.add_arc('outline-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('outline-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('outline-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('outline-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('outline-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('outline-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('outline-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('outline', *('outline-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)
        self.add_polyline('check',(16,24),(22,30),(32,18))
