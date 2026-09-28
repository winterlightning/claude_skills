"""An integrated user silhouette has a plain left half and toothed right half. Lucide cog and settings inform the mechanical outline. Small inner gear arcs are omitted; the central dividing axis and teeth preserve the hybrid identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c401ded5-d2e5-41aa-afc2-b65bf262fa9e'
SOURCE_PATH = 'pictographic-primitives/users/settings user_c401ded5-d2e5-41aa-afc2-b65bf262fa9e.svg'
AUTHOR = 'gpt-6'

class UserWithGear(Solo48):
    icon_id = 'user-with-gear'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('user', 'settings', 'gear', 'account', 'configuration', 'preferences', 'profile', 'admin')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('head-left', (24, 24), (24, 4), radius_x=10)
        self.add_polyline('head-teeth', (24, 4), (32, 4), (32, 8), (36, 10), (40, 10), (40, 18), (36, 18), (32, 20), (32, 24), (24, 24))
        self.relate('connect', 'head-left', 'head-teeth')
        self.add_polyline('axis', (24, 4), (24, 24), (24, 33), (24, 44))
        self.relate('connect', 'head-left', 'axis')
        self.relate('connect', 'head-teeth', 'axis')
        self.add_arc('body-left', (8, 44), (24, 33), radius_x=16, radius_y=11)
        self.add_line('base', (8, 44), (24, 44))
        self.relate('connect', 'body-left', 'base')
        self.relate('connect', 'body-left', 'axis')
        self.relate('connect', 'base', 'axis')
        self.add_polyline('body-teeth', (24, 33), (31, 33), (34, 33), (38, 37), (35, 40), (40, 40), (40, 44))
        self.relate('connect', 'body-teeth', 'axis')
        self.relate('connect', 'body-teeth', 'body-left')
