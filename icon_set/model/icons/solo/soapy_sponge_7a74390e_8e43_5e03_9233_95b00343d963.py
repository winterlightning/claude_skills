'A rectangular sponge is shown in perspective with its top and right side visible. A low cluster of rounded soap suds overlaps its lower front edge and spreads across the base.\n\nConstruction: Rectangular sponge above a three-lobed foam contour; omitted perspective seams for legible foam separation. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a74390e-8e43-5e03-9233-95b00343d963'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleaning sponge soap_7a74390e-8e43-5e03-9233-95b00343d963.svg'
AUTHOR = 'gpt-6'

class SoapySponge(Solo48):
    icon_id = 'soapy-sponge'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('sponge', 'soap', 'suds', 'cleaning', 'washing', 'foam')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('sponge-0', (13, 8), (41, 8))
        self.add_arc('sponge-1', (41, 8), (44, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sponge-2', (44, 11), (44, 17))
        self.add_arc('sponge-3', (44, 17), (41, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sponge-4', (41, 20), (13, 20))
        self.add_arc('sponge-5', (13, 20), (10, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sponge-6', (10, 17), (10, 11))
        self.add_arc('sponge-7', (10, 11), (13, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('foam-left', (4, 35), (8, 31), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('foam-lobe', (8, 31), (20, 31), radius_x=6, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('foam-lobe-2', (20, 31), (32, 31), radius_x=6, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('foam-right', (32, 31), (40, 35), radius_x=8, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('foam-lower-right', (40, 35), (35, 40), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('foam-base', (35, 40), (9, 40))
        self.add_arc('foam-lower-left', (9, 40), (4, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('sponge', 'sponge-0', 'sponge-1', 'sponge-2', 'sponge-3', 'sponge-4', 'sponge-5', 'sponge-6', 'sponge-7', closed=True)
        self.add_contour('foam', 'foam-left', 'foam-lobe', 'foam-lobe-2', 'foam-right', 'foam-lower-right', 'foam-base', 'foam-lower-left', closed=True)
