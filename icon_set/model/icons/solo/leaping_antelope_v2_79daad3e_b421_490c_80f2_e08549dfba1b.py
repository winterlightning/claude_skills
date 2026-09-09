# Variant of leaping-antelope; parent file remains unchanged.
'Leaping antelope with a single straight foreleg; retained directional silhouette and horn.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79daad3e-b421-490c-80f2-e08549dfba1b'
SOURCE_PATH = 'pictographic-primitives/animals/deer jump_79daad3e-b421-490c-80f2-e08549dfba1b.svg'
AUTHOR = 'gpt-6'

class LeapingAntelopeVariant2(Solo48):
    icon_id = 'leaping-antelope-v2'
    variant_of = 'leaping-antelope'
    variant_label = 'Single straight right leg'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('antelope', 'deer', 'leap', 'jump', 'running', 'gazelle', 'wildlife', 'motion')

    def build(self) -> None:
        self.add_polyline('silhouette', (2, 46), (6, 34), (12, 30), (12, 23), (30, 14), (34, 8), (40, 8), (46, 14), (38, 16), (38, 24), (18, 36), (10, 40), (6, 46), (2, 46))
        self.add_polyline('horn', (34, 8), (28, 2), (38, 2))
        self.relate('connect', 'silhouette', 'horn')
        self.add_line('right-leg', (38,24), (44,34))
        self.relate('connect', 'silhouette', 'right-leg')
