"""Hand Holding a Document. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a5b8e57-e476-5e0e-a43f-45bc8105f4e5'
SOURCE_PATH = 'pictographic-primitives/websites/digital policies data breach_1a5b8e57-e476-5e0e-a43f-45bc8105f4e5.svg'
AUTHOR = 'gpt-6'

class HandHoldingDocument(Solo48):
    icon_id = 'hand-holding-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    categories = ('websites', 'primitives')
    aliases = ()
    keywords = ('hand', 'document', 'paper', 'grip', 'policy', 'file', 'holding')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('paper', (18, 20), (8, 20), (8, 44), (32, 44), (32, 26))
        self.add_polyline('arm-top', (40, 4), (31, 10), (23, 10), (18, 20))
        self.relate('connect', 'arm-top', 'paper')
        self.add_line('arm-lower-1', (40, 16), (34, 21))
        self.add_line('arm-lower-2', (34, 21), (29, 21))
        self.add_line('arm-lower-3', (29, 21), (24, 26))
        self.add_arc('thumb-tip', (24, 26), (18, 20), radius_x=5, sweep=True)
        self.add_line('thumb-upper', (18, 20), (24, 14))
        self.add_contour('thumb', 'arm-lower-1', 'arm-lower-2', 'arm-lower-3', 'thumb-tip', 'thumb-upper')
        self.relate('connect', 'paper', 'thumb')
        self.relate('connect', 'arm-top', 'thumb')
        self.add_line('text', (17, 35), (23, 35))
