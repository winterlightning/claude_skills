"""High-Speed Train, re-authored from its reference on SOLO48."""
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
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('roof',(6,8),(24,8))
        self.add_arc('nose-upper',(24,8),(42,26),radius_x=20,radius_y=18)
        self.add_arc('nose-lower',(42,26),(40,30),radius_x=4)
        self.add_line('lower-body-1',(40,30),(6,30))
        self.add_line('lower-body-2',(6,30),(6,8))
        self.add_contour('body','roof','nose-upper','nose-lower','lower-body-1','lower-body-2')
        self.add_line('window',(13,18),(23,18))
        self.add_line('rail',(6,40),(42,40))
