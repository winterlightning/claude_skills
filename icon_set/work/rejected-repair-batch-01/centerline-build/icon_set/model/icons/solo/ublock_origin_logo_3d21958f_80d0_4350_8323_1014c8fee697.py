"""Joined lowercase u and B monogram. Preserve both identifying letters and omit the enclosing shield to provide legal room for the B counters."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d21958f-80d0-4350-8323-1014c8fee697'
SOURCE_PATH = 'pictographic-primitives/logos/ublock origin logo_3d21958f-80d0-4350-8323-1014c8fee697.svg'
AUTHOR = 'gpt-6'

class UblockOriginLogo(Solo48):
    icon_id = 'ublock-origin-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('ublock-origin', 'ad-blocker', 'shield', 'privacy', 'logo', 'brand', 'browser')

    def build(self):
        # Plan: Joined lowercase u and B monogram. Preserve both identifying letters and omit the enclosing shield to provide legal room for the B counters.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('u-left',(6,6),(6,33));self.add_arc('u-bottom',(6,33),(24,33),radius_x=9,sweep=False)
        self.add_polyline('shared-stem',(24,33),(24,24),(24,6))
        self.add_arc('b-top',(24,6),(24,24),radius_x=18,radius_y=9)
        self.add_arc('b-bottom',(24,24),(24,42),radius_x=18,radius_y=9)
        self.add_line('b-foot',(24,42),(24,33))
        for a,b in [('u-left','u-bottom'),('u-bottom','shared-stem'),('shared-stem','b-top'),('shared-stem','b-bottom'),('shared-stem','b-foot'),('b-top','b-bottom'),('b-bottom','b-foot'),('u-bottom','b-foot')]:self.relate('connect',a,b)

