'Compute stack: preserve the front slab and two depth edges with even ten-unit centerline spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fd8996a-d599-4790-9409-7653573d27f2'
SOURCE_PATH = 'pictographic-primitives/programing/elastic compute cloud 1_9fd8996a-d599-4790-9409-7653573d27f2.svg'
AUTHOR = 'gpt-6'

class ElasticComputeCloud1(Solo48):
    icon_id = 'elastic-compute-cloud-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'programing')

    def build(self) -> None:
        self.add_polyline('front',(26,6),(42,14),(42,34),(26,42),closed=True)
        self.add_polyline('middle',(17,8),(16,10),(16,38),(17,40))
        self.add_polyline('back',(7,11),(6,13),(6,35),(7,37))
