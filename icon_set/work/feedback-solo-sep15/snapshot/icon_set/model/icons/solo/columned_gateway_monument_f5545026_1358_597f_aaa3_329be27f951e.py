"""Columned gateway monument: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5545026-1358-597f-aaa3-329be27f951e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/brandenburg gate berlin_f5545026-1358-597f-aaa3-329be27f951e.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'columned-gateway-monument'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('gate', 'gateway', 'monument', 'brandenburg', 'berlin', 'landmark', 'arch', 'columns', 'architecture')

    def build(self):
        self.add_polyline('outline', (6, 24), (16, 24), (32, 24), (42, 24), (42, 42), (34, 42), (34, 32), (14, 32), (14, 42), (6, 42), closed=True)
        self.add_polyline('attic', (16, 24), (16, 16), (24, 16), (32, 16), (32, 24))
        self.relate('connect', 'attic', 'outline')
        self.add_polyline('mast', (24, 6), (24, 8), (24, 16))
        self.add_polyline('cross', (20, 8), (24, 8), (28, 8))
        self.relate('connect', 'mast', 'cross')
        self.relate('connect', 'mast', 'attic')
