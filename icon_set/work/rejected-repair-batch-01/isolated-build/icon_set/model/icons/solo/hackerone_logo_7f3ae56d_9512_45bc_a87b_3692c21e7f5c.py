"""A tall rounded vertical bar stands beside a numeral 1 with a slanted flag at its top, together reading as h1.

Plan: Tall capsule on the left and a flagged numeral one on the right.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; capsule plus joined typographic stroke.
Simplification: Outlined numeral becomes one stroke; flag and tall left bar retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f3ae56d-9512-45bc-a87b-3692c21e7f5c'
SOURCE_PATH = 'pictographic-primitives/logos/hackerone logo_7f3ae56d-9512-45bc-a87b-3692c21e7f5c.svg'
AUTHOR = 'gpt-6'


class HackeroneLogo(Solo48):
    icon_id = 'hackerone-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('hackerone', 'security', 'bug-bounty', 'h1', 'logo', 'brand', 'hacker')

    def build(self):
        self.add_arc('cap-top',(8,8),(16,8),radius_x=4)
        self.add_line('cap-right',(16,8),(16,40))
        self.add_arc('cap-bottom',(16,40),(8,40),radius_x=4)
        self.add_line('cap-left',(8,40),(8,8))
        self.add_contour('bar','cap-top','cap-right','cap-bottom','cap-left',closed=True)
        self.add_polyline('one',(26,23),(40,15),(40,44))
