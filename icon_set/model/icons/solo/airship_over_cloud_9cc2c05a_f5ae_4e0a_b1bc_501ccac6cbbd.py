"""Airship over Cloud, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd'
SOURCE_PATH = 'pictographic-primitives/transportation/hotair balloon_9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd.svg'
AUTHOR = 'gpt-6'

class AirshipOverCloud(Solo48):
    icon_id = 'airship-over-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('airship', 'blimp', 'zeppelin', 'dirigible', 'cloud', 'sky', 'flight', 'aviation')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('envelope-top',(10,8),(38,8))
        self.add_arc('envelope-right',(38,8),(38,20),radius_x=6)
        self.add_line('envelope-bottom-1',(38,20),(24,20))
        self.add_line('envelope-bottom-2',(24,20),(10,20))
        self.add_arc('envelope-left-bottom',(10,20),(6,14),radius_x=6)
        self.add_arc('envelope-left-top',(6,14),(10,8),radius_x=6)
        self.add_contour('envelope','envelope-top','envelope-right','envelope-bottom-1','envelope-bottom-2','envelope-left-bottom','envelope-left-top',closed=True)
        self.add_line('gondola',(24,20),(24,23))
        self.relate('connect','gondola','envelope')
        self.add_arc('cloud-left',(12,40),(20,32),radius_x=8)
        self.add_arc('cloud-crown',(20,32),(26,34),radius_x=6)
        self.add_arc('cloud-right',(26,34),(32,40),radius_x=6)
        self.add_line('cloud-bottom',(32,40),(12,40))
        self.add_contour('cloud','cloud-left','cloud-crown','cloud-right','cloud-bottom',closed=True)
        self.add_polyline('tail-fin',(6,8),(6,14),(6,20))
        self.relate('connect','tail-fin','envelope')
