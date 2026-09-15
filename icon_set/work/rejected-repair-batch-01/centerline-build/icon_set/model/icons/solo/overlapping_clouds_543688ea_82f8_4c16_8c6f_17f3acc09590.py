'Overlapping clouds: smooth rear cloud reaches the upper and right bounds; front lobe reaches the left and bottom.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '543688ea-82f8-4c16-8c6f-17f3acc09590'
SOURCE_PATH = 'pictographic-primitives/weather/weather clouds_543688ea-82f8-4c16-8c6f-17f3acc09590.svg'
AUTHOR = 'gpt-6'

class OverlappingClouds(Solo48):
    icon_id = 'overlapping-clouds'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('cloud', 'overcast', 'sky', 'weather', 'cloudy', 'atmosphere')

    def build(self) -> None:
        # Broad cloud lobes retain their natural overlap and tangent curve flow.
        self.add_arc('left',(12,40),(12,28),radius_x=8,radius_y=6)
        self.add_arc('crown',(12,28),(28,28),radius_x=8,radius_y=6)
        self.add_arc('right',(28,28),(28,40),radius_x=8,radius_y=6)
        self.add_line('base',(28,40),(12,40))
        self.add_contour('front','left','crown','right','base',closed=True)
        self.add_bezier('back',(12,28),((12,17),(16,8),(28,8)),((37,8),(44,15),(44,24)),((44,33),(37,40),(28,40)))
        self.relate('connect','front','back')
