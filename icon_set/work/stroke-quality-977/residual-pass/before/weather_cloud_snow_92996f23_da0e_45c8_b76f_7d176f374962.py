"""weather-cloud-snow: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92996f23-da0e-45c8-b76f-7d176f374962'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud snow_92996f23-da0e-45c8-b76f-7d176f374962.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class WeatherCloudSnow(Solo48):
    icon_id = 'weather-cloud-snow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('weather', 'cloud', 'snow')

    def build(self):
        # HRECT_L (4,8)-(44,40); preserve cloud silhouette, remove tiny converted segments.
        # Construction reference: Lucide cloud: a few coherent lobes and a flat base
        self.add_line('base',(34,40),(13,40))
        self.add_arc('left-lobe',(13,40),(13,22),radius_x=9)
        self.add_bezier('crown',(13,22),((13,14),(17,8),(24,8)),((31,8),(35,14),(35,20)))
        self.add_bezier('right-lobe',(35,20),((41,20),(44,24),(44,30)),((44,36),(40,40),(34,40)))
        self.add_contour('outline','base','left-lobe','crown','right-lobe',closed=True)
