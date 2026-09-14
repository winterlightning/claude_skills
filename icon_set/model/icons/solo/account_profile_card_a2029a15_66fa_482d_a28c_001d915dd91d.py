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
    category = "symbols/standalone"
    aliases = ()
    keywords = ('account', 'profile', 'user', 'person', 'details', 'card', 'identity', 'page')

    def build(self) -> None:
        self.add_arc('head-right', (14, 8), (14, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-left', (14, 24), (14, 8), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_arc('shoulder-left', (6, 40), (14, 24), radius_x=10, radius_y=16, sweep=True)
        self.add_arc('shoulder-right', (14, 24), (24, 40), radius_x=10, radius_y=16, sweep=True)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.relate("connect", 'head', 'shoulders')
        self.add_polyline('detail-box', (34, 10), (42, 10), (42, 22), (34, 22), closed=True)
        self.add_line('detail-line', (34, 34), (42, 34))
