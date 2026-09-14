'Compute instances: three offset square layers with uncluttered partial back outlines and generous diagonal separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c211c96-838c-47b8-8fce-5a2678d829d5'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud instances_6c211c96-838c-47b8-8fce-5a2678d829d5.json'
AUTHOR = 'gpt-6'

class ElasticComputeCloudInstances(Solo48):
    icon_id = 'elastic-compute-cloud-instances'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'instances', 'programing')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 24, 24, 42, 42, 3
        self.add_line('front-top', (left+radius,top), (right-radius,top))
        self.add_arc('front-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('front-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('front-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('front-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('front-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('front-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('front-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('front', *('front-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_polyline('middle',(14,33),(14,14),(33,14))
        self.add_polyline('back',(6,24),(6,6),(24,6))
