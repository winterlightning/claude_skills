"""The letters GO in bold outlined rounded capitals set close together.

Plan: Open G and narrow O with matching capsule curves and baseline.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected at-sign: open letter curve and internal terminal.
Simplification: Double outline reduces to monoline GO.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98cd94a5-917a-45d8-92f2-e9f1197eecf0'
SOURCE_PATH = 'pictographic-primitives/logos/indiegogo logo_98cd94a5-917a-45d8-92f2-e9f1197eecf0.svg'
AUTHOR = 'gpt-6'


class IndiegogoLogo(Solo48):
    icon_id = 'indiegogo-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('indiegogo', 'crowdfunding', 'go', 'wordmark', 'logo', 'brand', 'campaign')

    def build(self):
        self.add_bezier('g',(18,12),((14,8),(4,8),(4,20)))
        self.add_line('gv',(4,20),(4,28))
        self.add_bezier('gb',(4,28),((4,40),(18,44),(18,32)))
        self.add_line('gh1',(18,32),(18,25))
        self.add_line('gh2',(18,25),(12,25))
        self.add_contour('G','g','gv','gb','gh1','gh2')
        self.add_line('ol',(28,16),(28,32))
        self.add_arc('ob',(28,32),(44,32),radius_x=8,sweep=False)
        self.add_line('or',(44,32),(44,16))
        self.add_arc('ot',(44,16),(28,16),radius_x=8,sweep=False)
        self.add_contour('O','ol','ob','or','ot',closed=True)
