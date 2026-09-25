"""A wall-mounted security camera has a wide hood and left-reaching bracket. Lucide cctv informs the camera/bracket hierarchy. Omit bracket thickness and wall-foot box; preserve the stepped housing and direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d23e8cb-86e9-4a4f-a0b4-e8e399ba9e1f'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance camera_5d23e8cb-86e9-4a4f-a0b4-e8e399ba9e1f.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'wall-mounted-security-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('security camera', 'surveillance', 'camera', 'cctv', 'wall mount', 'monitoring', 'security', 'video')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Broad weather hood, camera underside, and a bracket attached at one node.
        self.add_polyline('hood',(4,8),(44,8),(42,18),(36,18),(24,18),(8,18),closed=True)
        self.add_line('body-left',(8,18),(8,28))
        self.add_line('body-base',(8,28),(24,28))
        self.add_arc('body-corner',(24,28),(36,18),radius_x=12,radius_y=10,sweep=False)
        self.add_contour('body','body-left','body-base','body-corner')
        self.relate('connect','body','hood')
        self.add_polyline('bracket',(24,28),(24,40),(8,40))
        self.relate('connect','bracket','body')
        self.add_line('wall-foot',(8,34),(8,40))
        self.relate('connect','wall-foot','bracket')
