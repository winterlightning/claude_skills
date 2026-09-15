"""A rounded square frame holds a lowercase h with a leaf-like accent above its arm and a small right-pointing triangle at the foot of its stem.

Plan: Rounded square frame contains h and a detached rising accent; h owns its arm node.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; equal frame radii and rounded letter shoulder.
Simplification: Leaf accent reduces to one short stroke; tiny stem-foot triangle omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65983977-44fb-4a2c-a8b7-4af262fab497'
SOURCE_PATH = 'pictographic-primitives/logos/heroku logo_65983977-44fb-4a2c-a8b7-4af262fab497.svg'
AUTHOR = 'gpt-6'


class HerokuLogo(Solo48):
    icon_id = 'heroku-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('heroku', 'cloud', 'hosting', 'letter-h', 'logo', 'brand', 'platform')

    def build(self):
        self.add_line('frame-top',(10,6),(38,6))
        self.add_arc('frame-tr',(38,6),(42,10),radius_x=4)
        self.add_line('frame-right',(42,10),(42,38))
        self.add_arc('frame-br',(42,38),(38,42),radius_x=4)
        self.add_line('frame-bottom',(38,42),(10,42))
        self.add_arc('frame-bl',(10,42),(6,38),radius_x=4)
        self.add_line('frame-left',(6,38),(6,10))
        self.add_arc('frame-tl',(6,10),(10,6),radius_x=4)
        self.add_contour('frame',*(f'frame-{s}' for s in ('top','tr','right','br','bottom','bl','left','tl')),closed=True)
        self.add_polyline('h-stem',(16,15),(16,26),(16,33))
        self.add_line('h-arm',(16,26),(28,26))
        self.add_arc('h-shoulder',(28,26),(32,30),radius_x=4)
        self.add_line('h-leg',(32,30),(32,33))
        self.add_contour('h-bend','h-arm','h-shoulder','h-leg')
        self.relate('connect','h-stem','h-bend')
        self.add_line('accent',(28,17),(31,15))
