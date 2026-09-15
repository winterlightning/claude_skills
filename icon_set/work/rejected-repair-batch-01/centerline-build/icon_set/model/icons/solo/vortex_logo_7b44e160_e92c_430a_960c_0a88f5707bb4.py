"""Tall symmetric V reduced to two joined strokes. Preserve the sharp lower vertex; omit the doubled outline and use the required rounded stroke caps."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b44e160-e92c-430a-960c-0a88f5707bb4'
SOURCE_PATH = 'pictographic-primitives/logos/vortex logo_7b44e160-e92c-430a-960c-0a88f5707bb4.svg'
AUTHOR = 'gpt-6'

class VortexLogo(Solo48):
    icon_id = 'vortex-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('vortex', 'letter-v', 'logo', 'brand', 'v', 'mod-manager', 'gaming')

    def build(self):
        # Plan: Tall symmetric V reduced to two joined strokes. Preserve the sharp lower vertex; omit the doubled outline and use the required rounded stroke caps.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('v',(8,4),(24,44),(40,4))

