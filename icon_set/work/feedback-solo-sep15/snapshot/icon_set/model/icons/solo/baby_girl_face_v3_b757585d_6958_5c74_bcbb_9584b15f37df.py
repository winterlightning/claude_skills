"""Remove the bow knot completely and raise both lower bow edges to open the forehead; preserve paired eyes and the round cheeks. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b757585d-6958-5c74-bcbb-9584b15f37df'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_b757585d-6958-5c74-bcbb-9584b15f37df.svg'
AUTHOR = 'gpt-6'

class BabyGirlFaceVariant3(Solo48):
    icon_id = 'baby-girl-face-v3'
    variant_of = 'baby-girl-face'
    variant_label = 'Remove the bow knot completely and raise both lower bow edges to open the forehead; preserve paired eyes and the round cheeks.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'girl', 'face', 'infant', 'nursery')

    def build(self) -> None:
        """Symbol plan: Remove the bow knot completely and raise both lower bow edges to open the forehead; preserve paired eyes and the round cheeks. Reference: Lucide baby: paired dot eyes and one broad cheek contour; shared human reference."""
        self.add_bezier('temple-left', (10, 18), ((9, 21), (8, 23), (8, 24)))
        self.add_bezier('ear-left', (8, 24), ((6, 24), (6, 25), (6, 27)), ((6, 29), (6, 30), (8, 30)))
        self.add_bezier('chin', (8, 30), ((10, 38), (16, 42), (24, 42)), ((32, 42), (38, 38), (40, 30)))
        self.add_bezier('ear-right', (40, 30), ((42, 30), (42, 29), (42, 27)), ((42, 25), (42, 24), (40, 24)))
        self.add_bezier('temple-right', (40, 24), ((40, 23), (39, 21), (38, 18)))
        self.add_contour('face', 'temple-left', 'ear-left', 'chin', 'ear-right', 'temple-right')
        self.add_polyline('bow-left', (24, 12), (10, 6), (10, 18), closed=True)
        self.add_polyline('bow-right', (24, 12), (38, 6), (38, 18), closed=True)
        self.relate('connect', 'bow-left', 'bow-right')
        self.relate('connect', 'bow-left', 'face')
        self.relate('connect', 'bow-right', 'face')
        self.add_dot('eye-left', (17, 26))
        self.add_dot('eye-right', (31, 26))
        self.add_arc('smile', (21, 33), (27, 33), radius_x=4, radius_y=2, sweep=False)
