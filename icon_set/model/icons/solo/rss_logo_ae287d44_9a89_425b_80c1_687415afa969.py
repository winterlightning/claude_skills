"""rss-logo: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae287d44-9a89-425b-80c1-687415afa969'
SOURCE_PATH = 'pictographic-primitives/logos/rss logo_ae287d44-9a89-425b-80c1-687415afa969.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class RssLogo(Solo48):
    icon_id = 'rss-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('rss', 'logo', 'logos')

    def build(self):
        # Plan: SQUARE; three concentric quarter circles with shared origin and uniform spacing.
        # Reference: Geometric concentric arcs.
        for name,r in [('outer',36),('middle',23),('inner',10)]:
            self.add_arc(name,(6,42-r),(6+r,42),radius_x=r)
