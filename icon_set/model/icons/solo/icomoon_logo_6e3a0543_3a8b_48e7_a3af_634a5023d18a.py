"""A large circle holds a smaller upright oval shifted slightly left, with a tiny ring at its centre, like an eye.

Plan: Outer circle and slightly left-offset upright oval, concentric eye dot.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected at-sign: nested circular forms.
Simplification: Tiny innermost ring becomes a dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e3a0543-3a8b-48e7-a3af-634a5023d18a'
SOURCE_PATH = 'pictographic-primitives/logos/icomoon logo_6e3a0543-3a8b-48e7-a3af-634a5023d18a.svg'
AUTHOR = 'gpt-6'


class IcomoonLogo(Solo48):
    icon_id = 'icomoon-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('icomoon', 'icons', 'eye', 'logo', 'brand', 'icon-font', 'design')

    def build(self):
        for name,cx,rx,ry in [('outer',24,20,20),('eye',23,9,11)]:
         self.add_arc(name+'a',(cx+rx,24),(cx-rx,24),radius_x=rx,radius_y=ry)
         self.add_arc(name+'b',(cx-rx,24),(cx+rx,24),radius_x=rx,radius_y=ry)
         self.add_contour(name,name+'a',name+'b',closed=True)
        self.add_dot('pupil',(23,24))
