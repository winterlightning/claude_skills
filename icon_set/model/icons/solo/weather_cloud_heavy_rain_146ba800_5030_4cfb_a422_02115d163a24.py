"""A rounded cloud with a level lower edge spans the upper image. Three long parallel rain strokes fall diagonally toward the lower left beneath the cloud.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '146ba800-5030-4cfb-a422-02115d163a24'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heavy-rain-cloud/20260926T172218Z-thuan-mac-1/reference/weather cloud heavy rain_146ba800-5030-4cfb-a422-02115d163a24.svg'
AUTHOR = "gpt-6"

class HeavyRainCloud(Solo48):
    icon_id = 'heavy-rain-cloud-solo'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('cloud', 'rain', 'downpour', 'precipitation', 'weather', 'storm')

    def build(self) -> None:
        # A three-lobed cloud, with the rain as a mirrored three-stroke series.
        self.add_arc('left-lobe',(4,24),(12,16),radius_x=8,radius_y=8,sweep=True)
        self.add_arc('crown-left',(12,16),(24,8),radius_x=12,radius_y=8,sweep=True)
        self.add_arc('crown-right',(24,8),(36,16),radius_x=12,radius_y=8,sweep=True)
        self.add_arc('right-lobe',(36,16),(44,24),radius_x=8,radius_y=8,sweep=True)
        self.add_line('base',(44,24),(4,24))
        self.add_contour('cloud','left-lobe','crown-left','crown-right','right-lobe','base',closed=True)
        for index,x in enumerate((14,26,38)):
            self.add_line(f'rain-{index}',(x,33),(x-7,40))
