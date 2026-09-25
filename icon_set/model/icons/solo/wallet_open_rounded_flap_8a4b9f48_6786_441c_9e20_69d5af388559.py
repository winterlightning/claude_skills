"""Open Snap Wallet.
Plan: A rounded rear wallet panel and forward swinging flap with central snap. Extrema (6,6)-(42,42).
Reference: Lucide wallet: broad rounded panel and sparse clasp detail.
Reduction: Short pocket line removed to retain the large snap and swinging flap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a4b9f48-6786-441c-9e20-69d5af388559'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/money wallet open_8a4b9f48-6786-441c-9e20-69d5af388559.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'wallet-open-rounded-flap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('open', 'snap', 'wallet')

    def build(self):

        self.add_polyline('rear-top',(6,6),(36,6))
        self.add_arc('rear-corner',(36,6),(42,12),radius_x=6)
        self.add_line('rear-side',(42,12),(42,28))
        self.add_arc('rear-bottom',(42,28),(36,34),radius_x=6)
        self.add_line('rear-base',(36,34),(32,34))
        self.add_line('flap-top-1',(6, 6),(26, 14))
        self.add_bezier('flap-right',(26,14),((32,16),(32,18),(32,24)),((32,28),(32,30),(32,34)))
        self.add_line('flap-end',(32,34),(32,38))
        self.add_arc('flap-bottom',(32,38),(28,42),radius_x=4)
        self.add_line('flap-base',(28,42),(10,36))
        self.add_arc('flap-left-bottom',(10,36),(6,32),radius_x=4)
        self.add_line('flap-left',(6,32),(6,6))
        self.add_contour('flap','flap-top-1','flap-right','flap-end','flap-bottom','flap-base','flap-left-bottom','flap-left',closed=True)
        self.relate('connect','rear-top','flap');self.relate('connect','rear-top','rear-corner');self.relate('connect','rear-corner','rear-side');self.relate('connect','rear-side','rear-bottom');self.relate('connect','rear-bottom','rear-base');self.relate('connect','rear-base','flap')

        self.add_arc('snap-a',(20,24),(20,30),radius_x=3)
        self.add_arc('snap-b',(20,30),(20,24),radius_x=3)
        self.add_contour('snap','snap-a','snap-b',closed=True)
