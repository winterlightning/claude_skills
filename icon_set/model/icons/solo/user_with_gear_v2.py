# Review candidate; original preserved.
"""An integrated user silhouette has a plain left half and toothed right half. Lucide cog and settings inform the mechanical outline. Small inner gear arcs are omitted; the central dividing axis and teeth preserve the hybrid identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c401ded5-d2e5-41aa-afc2-b65bf262fa9e'
SOURCE_PATH = 'pictographic-primitives/users/settings user_c401ded5-d2e5-41aa-afc2-b65bf262fa9e.svg'
AUTHOR = 'gpt-6'

class UserWithGearVariant2(Solo48):
    icon_id = 'user-with-gear-v2'
    variant_of = 'user-with-gear'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/users'
    aliases = ()
    keywords = ('user', 'settings', 'gear', 'account', 'configuration', 'preferences', 'profile', 'admin')

    def build(self) -> None:
        """Opening repair: Made the organic half-head a true semicircle, enlarging its opening beside the centre axis."""
        self.add_arc('head-left', (24, 24), (24, 6), radius_x=9, radius_y=9)
        self.add_polyline('head-teeth', (24, 6), (32, 6), (32, 8), (36, 10), (40, 10), (40, 18), (36, 18), (32, 20), (32, 24), (24, 24))
        self.relate('connect', 'head-left', 'head-teeth')
        self.add_polyline('axis', (24, 6), (24, 24), (24, 33), (24, 42))
        self.relate('connect', 'head-left', 'axis')
        self.relate('connect', 'head-teeth', 'axis')
        self.add_arc('body-left', (8, 42), (24, 33), radius_x=16, radius_y=11)
        self.add_line('base', (8, 42), (24, 42))
        self.relate('connect', 'body-left', 'base')
        self.relate('connect', 'body-left', 'axis')
        self.relate('connect', 'base', 'axis')
        self.add_polyline('body-teeth', (24, 33), (31, 33), (34, 33), (38, 37), (35, 40), (40, 40), (40, 42))
        self.relate('connect', 'body-teeth', 'axis')
        self.relate('connect', 'body-teeth', 'body-left')
