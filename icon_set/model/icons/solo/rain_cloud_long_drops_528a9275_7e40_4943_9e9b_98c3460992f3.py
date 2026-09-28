"""Puffy cloud above three parallel rain strokes. Lucide cloud-rain: coherent cloud silhouette and a repeated drop series; drop angle and length retain the source distinction.

SOLO48 SQUARE, live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '528a9275-7e40-4943-9e9b-98c3460992f3'
SOURCE_PATH = 'pictographic-primitives/symbol/rain_528a9275-7e40-4943-9e9b-98c3460992f3.svg'
AUTHOR = 'gpt-6'


class RainCloudLongDrops(Solo48):
    icon_id = 'rain-cloud-long-drops'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('rain', 'cloud', 'weather', 'heavy-rain', 'shower', 'storm', 'forecast', 'downpour')

    def build(self) -> None:

        cloud_shoulder = 14
        cloud_middle = 18
        cloud_base = 22
        self.add_arc('crown',(14,cloud_shoulder),(34,cloud_shoulder),radius_x=10,radius_y=cloud_shoulder-6)
        self.add_arc('right-upper',(34,cloud_shoulder),(42,cloud_middle),radius_x=8,radius_y=cloud_middle-cloud_shoulder)
        self.add_arc('right-lower',(42,cloud_middle),(34,cloud_base),radius_x=8,radius_y=cloud_base-cloud_middle)
        self.add_line('base',(34,cloud_base),(14,cloud_base))
        self.add_arc('left-lower',(14,cloud_base),(6,cloud_middle),radius_x=8,radius_y=cloud_base-cloud_middle)
        self.add_arc('left-upper',(6,cloud_middle),(14,cloud_shoulder),radius_x=8,radius_y=cloud_middle-cloud_shoulder)
        self.add_contour('cloud','crown','right-upper','right-lower','base','left-lower','left-upper',closed=True)
        for index in range(3):
            x = 14 + index*12
            self.add_line('rain-'+str(index),(x,31),(x-2,42))
