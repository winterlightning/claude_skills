"""Libreoffice logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e87f7a66-b64b-4041-99da-df2c20f4910f'
SOURCE_PATH = 'pictographic-primitives/logos/libreoffice logo_e87f7a66-b64b-4041-99da-df2c20f4910f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LibreofficeLogo(Solo48):
    icon_id = 'libreoffice-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('libreoffice', 'logo', 'logos')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (30, 4), (40, 15))
        self.add_line('e1', (30, 4), (30, 15))
        self.add_line('e2', (30, 15), (40, 15))
        self.add_line('e3', (30, 4), (8, 4))
        self.add_line('e4', (8, 4), (8, 44))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_line('e6', (40, 44), (40, 15))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', closed=False)
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e6', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
