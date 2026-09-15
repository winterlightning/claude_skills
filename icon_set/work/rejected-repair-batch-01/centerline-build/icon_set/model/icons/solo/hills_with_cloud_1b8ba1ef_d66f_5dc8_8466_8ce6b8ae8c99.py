"""A smaller rounded foreground hill and taller rounded peak share a baseline below a small cloud. HRECT extremes (4,8)-(44,40).
Reduction: Removed the small snowcap zigzag to keep the hills and cloud distinct.
Lucide construction: cloud, mountain
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b8ba1ef-d66f-5dc8-8466-8ce6b8ae8c99'
SOURCE_PATH = 'pictographic-primitives/nature/mountain_1b8ba1ef-d66f-5dc8-8466-8ce6b8ae8c99.svg'
AUTHOR = 'gpt-6'


class HillsWithCloud(Solo48):
    icon_id = 'hills-with-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-01"
    aliases = ()
    keywords = ('mountain', 'hills', 'cloud', 'peak', 'landscape', 'outdoors', 'nature', 'snow')

    def build(self) -> None:
        self.add_arc("cloud-top",(8,12),(18,12),radius_x=5,radius_y=4)
        self.add_arc("cloud-right",(18,12),(18,20),radius_x=4)
        self.add_line("cloud-base",(18,20),(8,20))
        self.add_arc("cloud-left",(8,20),(8,12),radius_x=4)
        self.add_contour("cloud","cloud-top","cloud-right","cloud-base","cloud-left",closed=True)
        self.add_arc("hill",(4,40),(24,40),radius_x=10,radius_y=10)
        self.add_polyline("baseline",(4,40),(24,40),(44,40))
        self.add_arc("peak",(24,40),(44,40),radius_x=10,radius_y=20)
        self.relate("connect","hill","baseline-1")
        self.relate("connect","hill","baseline-2")
        self.relate("connect","peak","baseline-1")
        self.relate("connect","peak","baseline-2")
