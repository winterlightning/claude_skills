"""Three curved ascending bands reduced to three coherent strokes. A shared vertical series preserves equal spacing and upward-right direction; omit double outlines and alternating-end joins."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25ebf160-9ae7-4917-81fd-3893fb9b74c7'
SOURCE_PATH = 'pictographic-primitives/logos/scala logo_25ebf160-9ae7-4917-81fd-3893fb9b74c7.svg'
AUTHOR = 'gpt-6'

class ScalaLogo(Solo48):
    icon_id = 'scala-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('scala', 'programming', 'language', 'spiral', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: Three curved ascending bands reduced to three coherent strokes. A shared vertical series preserves equal spacing and upward-right direction; omit double outlines and alternating-end joins.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        for j,dy in enumerate((0,12,24)):
            self.add_bezier('band-'+str(j),(8,20+dy),((20,20+dy),(34,10+dy),(40,4+dy)))

