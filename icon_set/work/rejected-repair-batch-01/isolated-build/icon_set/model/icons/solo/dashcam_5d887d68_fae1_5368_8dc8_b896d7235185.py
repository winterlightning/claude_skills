'Dashcam: balanced rounded camera body with a centred mount and separated lens and indicator.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d887d68-fae1-5368-8dc8-b896d7235185'
SOURCE_PATH = 'pictographic-primitives/transportation/dashcam_5d887d68-fae1-5368-8dc8-b896d7235185.svg'
AUTHOR = 'gpt-6'

class Dashcam(Solo48):
    icon_id = 'dashcam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('dashcam', 'camera', 'dash camera', 'car', 'recording', 'video', 'driving', 'security')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 16, 44, 40, 4
        self.add_line('body-top', (left+radius,top), (right-radius,top))
        self.add_arc('body-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('body-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('body-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('body-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('body-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('body-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('body-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('body', *('body-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_arc('lens-top', (13,28), (19,28), radius_x=3, radius_y=3)
        self.add_arc('lens-bottom', (19,28), (13,28), radius_x=3, radius_y=3)
        self.add_contour('lens', 'lens-top', 'lens-bottom', closed=True)

        self.add_polyline('mount-top',(16,8),(24,8),(32,8))
        self.add_line('mount',(24,8),(24,16));self.relate('connect','mount-top','mount');self.relate('connect','mount','body')
        self.add_line('indicator',(31,28),(35,28))
