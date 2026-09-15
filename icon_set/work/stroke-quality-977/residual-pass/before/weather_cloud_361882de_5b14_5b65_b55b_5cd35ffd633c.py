"""weather-cloud: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '361882de-5b14-5b65-b55b-5cd35ffd633c'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud_361882de-5b14-5b65-b55b-5cd35ffd633c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class WeatherCloud(Solo48):
    icon_id = 'weather-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('weather', 'cloud')

    def build(self):
        # HRECT_L (4,8)-(44,40); preserve cloud silhouette, remove tiny converted segments.
        # Construction reference: Lucide cloud: a few coherent lobes and a flat base
        self.add_line('base',(34,40),(13,40))
        self.add_arc('left-lobe',(13,40),(13,22),radius_x=9)
        self.add_bezier('crown',(13,22),((13,14),(17,8),(24,8)),((31,8),(35,14),(35,20)))
        self.add_bezier('right-lobe',(35,20),((41,20),(44,24),(44,30)),((44,36),(40,40),(34,40)))
        self.add_contour('outline','base','left-lobe','crown','right-lobe',closed=True)
