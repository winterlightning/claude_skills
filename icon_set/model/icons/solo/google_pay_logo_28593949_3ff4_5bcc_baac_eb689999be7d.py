"""The wordmark G Pay in bold rounded letters, a capital G followed by P, a small a and a descending y.

Plan: G above Pay; all four letters rebuilt with shared nodes and legal row spacing.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide wordmark match.
Simplification: Four-letter wordmark reflowed onto two rows; no letters omitted; lowercase a uses the existing small-circle exception.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28593949-3ff4-5bcc-baac-eb689999be7d'
SOURCE_PATH = 'pictographic-primitives/logos/google pay_28593949-3ff4-5bcc-baac-eb689999be7d.svg'
AUTHOR = 'gpt-6'


class GooglePayLogo(Solo48):
    icon_id = 'google-pay-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-pay', 'google', 'payment', 'wallet', 'logo', 'brand', 'wordmark')

    def build(self):
        # Reflow the complete wordmark: G above Pay, without removing letters.
        self.add_arc('g-left',(24,8),(24,22),radius_x=8,radius_y=7,sweep=False)
        self.add_arc('g-bottom',(24,22),(32,15),radius_x=8,radius_y=7,sweep=False)
        self.add_line('g-bar',(32,15),(27,15))
        self.add_contour('g','g-left','g-bottom','g-bar')
        self.add_polyline('p-loop',(4,38),(4,30),(12,30),(12,38),closed=True)
        self.add_line('p-stem',(4,38),(4,40))
        self.relate('connect','p-loop','p-stem')
        self.add_arc('a-top',(21,35),(27,35),radius_x=3)
        self.add_arc('a-bottom',(27,35),(21,35),radius_x=3)
        self.add_contour('a','a-top','a-bottom',closed=True)
        self.add_polyline('a-stem',(27,30),(27,35),(27,38))
        self.relate('connect','a','a-stem')
        self.add_polyline('y-right',(44,30),(40,35),(36,40))
        self.add_line('y-left',(36,30),(40,35))
        self.relate('connect','y-right','y-left')
