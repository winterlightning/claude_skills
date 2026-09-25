"""Cryengine logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7da1e055-283b-4344-8cbf-9e4f26589f09'
SOURCE_PATH = 'pictographic-primitives/logos/cryengine logo_7da1e055-283b-4344-8cbf-9e4f26589f09.svg'
AUTHOR = 'gpt-6'

class CryengineLogo(Solo48):
    icon_id = 'cryengine-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('cryengine', 'logo', 'logos')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (19, 24), (29, 24), radius_x=5, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (29, 24), (19, 24), radius_x=5, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e1-1', (18, 8), (4, 24), radius_x=29, radius_y=29, large_arc=False, sweep=False)
        self.add_arc('e1-2', (4, 24), (16, 38), radius_x=28, radius_y=28, large_arc=False, sweep=False)
        self.add_arc('e2-1', (30, 8), (44, 24), radius_x=30, radius_y=30, large_arc=False, sweep=True)
        self.add_arc('e2-2', (44, 24), (29, 40), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_contour('c0', *('e1-1', 'e1-2'), closed=False)
        self.add_contour('c1', *('e2-1', 'e2-2'), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
