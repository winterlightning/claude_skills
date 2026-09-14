"""Round head above an open shoulder arch. Lucide user-round: circle and semicircular shoulders; no details removed.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3352ce5f-f0e1-4497-86c8-0c433016cab6'
SOURCE_PATH = 'pictographic-primitives/symbol/profile_3352ce5f-f0e1-4497-86c8-0c433016cab6.svg'
AUTHOR = 'gpt-6'

class UserProfile(Solo48):
    icon_id = 'user-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('user', 'profile', 'person', 'account', 'avatar', 'member', 'contact', 'people')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('head-top', (15, 13), (33, 13), radius_x=9)
        self.add_arc('head-bottom', (33, 13), (15, 13), radius_x=9)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (8, 44), (40, 44), radius_x=16, radius_y=14, sweep=True)
