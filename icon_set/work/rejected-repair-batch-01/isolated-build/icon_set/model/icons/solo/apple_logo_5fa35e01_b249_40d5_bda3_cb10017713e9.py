"""An apple silhouette with a rounded bite taken from its right side and a single leaf tilted above its top.

Plan: Broad bitten fruit with detached tilted leaf stroke.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: apple: rounded shoulders and paired lower lobes.
Simplification: Leaf outline becomes a tilted stroke; deliberate right-side bite retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fa35e01-b249-40d5-bda3-cb10017713e9'
SOURCE_PATH = 'pictographic-primitives/logos/ios logo 2_5fa35e01-b249-40d5-bda3-cb10017713e9.svg'
AUTHOR = 'gpt-6'


class AppleLogo(Solo48):
    icon_id = 'apple-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('apple', 'ios', 'mac', 'fruit', 'logo', 'brand', 'technology')

    def build(self):
        self.add_line('leaf',(24,8),(30,4))
        self.add_bezier('fruit',(40,20),((34,12),(28,20),(24,18)),((16,14),(8,16),(8,26)),((8,36),(14,44),(19,44)),((21,44),(22,42),(24,42)),((26,42),(28,44),(31,44)),((35,44),(39,37),(40,34)))
        self.add_bezier('bite',(40,34),((29,32),(30,24),(40,20)))
        self.add_contour('body','fruit','bite',closed=True)
