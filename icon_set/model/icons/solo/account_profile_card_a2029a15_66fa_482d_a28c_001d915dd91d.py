"""Account Profile Card. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide user-round: circular head and symmetric shoulder arch.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2029a15-66fa-482d-a28c-001d915dd91d'
SOURCE_PATH = 'pictographic-primitives/symbol/account page_a2029a15-66fa-482d-a28c-001d915dd91d.svg'
AUTHOR = 'gpt-6'


class AccountProfileCard(Solo48):
    icon_id = 'account-profile-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('account', 'profile', 'user', 'person', 'details', 'card', 'identity', 'page')

    def build(self) -> None:
        # Shared human_ref/user.svg construction: circular head, broad shoulders,
        # and exactly 4 units of visible head/body clearance (8 centerline).
        # HRECT_L centerline extremes: (4,8)-(44,40).
        cx, head_cy, head_radius = 14, 14, 6
        body_top = head_cy + head_radius + 8
        self.add_arc('head-right', (cx, 8), (cx, 20), radius_x=head_radius)
        self.add_arc('head-left', (cx, 20), (cx, 8), radius_x=head_radius)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_arc('shoulder-left', (4, 40), (cx, body_top), radius_x=10, radius_y=12)
        self.add_arc('shoulder-right', (cx, body_top), (24, 40), radius_x=10, radius_y=12)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.add_polyline('detail-box', (34, 10), (44, 10), (44, 22), (34, 22), closed=True)
        self.add_line('detail-line', (34, 34), (44, 34))
