"""A ceiling-mounted dome camera contains a centered circular lens. Lucide cctv informs hierarchy and minimal lens detail. Remove the extra lens arch and center dot to preserve clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '649db65c-32e2-45a2-9b75-61ac786da97c'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance camera_649db65c-32e2-45a2-9b75-61ac786da97c.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'dome-security-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('dome camera', 'security', 'surveillance', 'cctv', 'ceiling', 'camera', 'monitoring', 'video')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Ceiling flange owns a semicircular dome and centered lens.
        self.add_polyline('plate',(4,8),(44,8),(44,16),(40,16),(8,16),(4,16),closed=True)
        self.add_line('dome-right',(40,16),(40,24))
        self.add_arc('dome-bottom',(40,24),(8,24),radius_x=16)
        self.add_line('dome-left',(8,24),(8,16))
        self.add_contour('dome','dome-right','dome-bottom','dome-left')
        self.relate('connect','dome','plate')
        self.add_arc('lens-top',(21,28),(27,28),radius_x=3)
        self.add_arc('lens-bottom',(27,28),(21,28),radius_x=3)
        self.add_contour('lens','lens-top','lens-bottom',closed=True)
