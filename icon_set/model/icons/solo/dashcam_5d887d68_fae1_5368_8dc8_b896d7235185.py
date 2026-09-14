"""Dashcam, rebuilt from the supplied reference on SOLO48."""
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
        # HRECT_L: current contract centerline extremes (6, 8)-(42, 40).
        self.add_polyline('mount-top',(16,8),(24,8),(32,8))
        self.add_line('mount-stem',(24,8),(24,16))
        self.relate('connect','mount-top','mount-stem')
        self.add_line('top-left',(8,16),(24,16))
        self.add_line('top-right',(24,16),(40,16))
        self.add_arc('corner-tr',(40,16),(42,20),radius_x=4)
        self.add_line('right',(42,20),(42,36))
        self.add_arc('corner-br',(42,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('corner-bl',(8,40),(6,36),radius_x=4)
        self.add_line('left',(6,36),(6,20))
        self.add_arc('corner-tl',(6,20),(8,16),radius_x=4)
        self.add_contour('body','top-left','top-right','corner-tr','right','corner-br','bottom','corner-bl','left','corner-tl',closed=True)
        self.relate('connect','mount-stem','body')
        self.add_arc('lens-a',(16,25),(16,31),radius_x=3)
        self.add_arc('lens-b',(16,31),(16,25),radius_x=3)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('indicator',(32,28),(35,28))
