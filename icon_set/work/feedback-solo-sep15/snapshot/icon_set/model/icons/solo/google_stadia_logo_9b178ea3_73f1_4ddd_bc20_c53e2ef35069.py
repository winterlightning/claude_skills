"""A ribbon-like swoosh bends back and forth in an S shape, flaring wide at the top right and tapering to a point at the lower left.

Plan: One smooth S ribbon run with broad upper sweep and shortened lower return.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact local Lucide match; tangent-continuous cubic ribbon construction.
Simplification: Ribbon edges merge into one continuous stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b178ea3-73f1-4ddd-bc20-c53e2ef35069'
SOURCE_PATH = 'pictographic-primitives/logos/google stadia logo_9b178ea3-73f1-4ddd-bc20-c53e2ef35069.svg'
AUTHOR = 'gpt-6'


class GoogleStadiaLogo(Solo48):
    icon_id = 'google-stadia-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-stadia', 'stadia', 'gaming', 'google', 'logo', 'brand', 'cloud-gaming')

    def build(self):
        self.add_bezier('swoosh',(44,8),((24,8),(4,8),(4,16)),((4,24),(40,20),(40,28)),((40,34),(20,32),(12,40)))
