'High-speed train: preserve the aerodynamic rounded nose and a clear window above the separate rail.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '149a83e6-5647-53e7-9abb-0cbcc041df3b'
SOURCE_PATH = 'pictographic-primitives/transportation/high speed train_149a83e6-5647-53e7-9abb-0cbcc041df3b.svg'
AUTHOR = 'gpt-6'

class HighSpeedTrain(Solo48):
    icon_id = 'high-speed-train'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('high speed train', 'bullet train', 'shinkansen', 'train', 'railway', 'rail', 'fast', 'transport')

    def build(self) -> None:
        self.add_line('roof',(4,8),(24,8))
        self.add_bezier('nose',(24,8),((35,8),(44,18),(44,26)),((44,29),(42,30),(40,30)))
        self.add_polyline('base',(40,30),(4,30),(4,8))
        self.relate('connect','roof','nose');self.relate('connect','nose','base');self.relate('connect','base','roof')
        self.add_line('window',(13,19),(23,19))
        self.add_line('rail',(4,40),(44,40))
