"""Vertical Temperature Measurement Thermometer. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH = 'pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-temperature-measurement-thermometer-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'vertical temperature measurement thermometer')
    def build(self):
        self.add_line('tube-left',(10,27),(10,13))
        self.add_arc('top',(10,13),(28,13),radius_x=9)
        self.add_line('tube-right',(28,13),(28,27))
        self.add_bezier('bulb',(28,27),((36,35),(32,44),(20,44)),((8,44),(8,40),(8,36)),((8,32),(9,29),(10,27)))
        self.add_contour('outline','tube-left','top','tube-right','bulb',closed=True)
        self.add_line('mercury',(19,24),(19,35))
        self.add_line('scale',(38,17),(40,17))
