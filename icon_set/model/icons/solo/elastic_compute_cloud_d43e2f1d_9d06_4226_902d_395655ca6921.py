'Compute stack: regular perspective panels with deliberate 8-unit offsets and straight edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43e2f1d-9d06-4226-902d-395655ca6921'
SOURCE_PATH = 'pictographic-primitives/programing/elastic compute cloud_d43e2f1d-9d06-4226-902d-395655ca6921.svg'
AUTHOR = 'gpt-6'

class ElasticComputeCloud(Solo48):
    icon_id = 'elastic-compute-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'programing')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('front-1', (6, 20), (18, 26))
        self.add_line('front-2', (18, 26), (18, 42))
        self.add_line('front-3', (18, 42), (6, 36))
        self.add_line('front-4', (6, 36), (6, 20))
        self.add_line('middle-1', (14, 12), (28, 19))
        self.add_line('middle-2', (28, 19), (28, 36))
        self.add_line('back-1', (26, 6), (42, 14))
        self.add_line('back-2', (42, 14), (42, 30))
        self.add_contour('front', *('front-1', 'front-2', 'front-3', 'front-4'), closed=False)
        self.add_contour('middle', *('middle-1', 'middle-2'), closed=False)
        self.add_contour('back', *('back-1', 'back-2'), closed=False)
