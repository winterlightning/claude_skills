'Camera glasses: equal rounded lenses and shared bridge, with the camera outline genuinely attached at both outer sides.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31079e61-3ff6-5151-ac76-c4202759aded'
SOURCE_PATH = 'icons-json/photography/camera glasses_31079e61-3ff6-5151-ac76-c4202759aded.json'
AUTHOR = 'gpt-6'

class CameraGlasses(Solo48):
    icon_id = 'camera-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'glasses', 'photography')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 24, 20, 40, 4
        self.add_line('left-lens-top', (left+radius,top), (right-radius,top))
        self.add_arc('left-lens-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('left-lens-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('left-lens-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('left-lens-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('left-lens-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('left-lens-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('left-lens-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('left-lens', *('left-lens-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 28, 24, 44, 40, 4
        self.add_line('right-lens-top', (left+radius,top), (right-radius,top))
        self.add_arc('right-lens-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('right-lens-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('right-lens-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('right-lens-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('right-lens-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('right-lens-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('right-lens-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('right-lens', *('right-lens-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_arc('bridge',(20,28),(28,28),radius_x=6)
        self.relate('connect','bridge','left-lens');self.relate('connect','bridge','right-lens')
        self.add_polyline('camera',(4,28),(4,20),(8,14),(16,14),(20,8),(28,8),(32,14),(40,14),(44,20),(44,28))
        self.relate('connect','camera','left-lens');self.relate('connect','camera','right-lens')
