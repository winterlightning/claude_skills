# Refinement: Use a smaller lower-left enclosure corner so the LM baseline has full clearance.
# Repair: Retain the LM monogram, with the L sharing the left stem and baseline. Equal 8-unit m arches fit the enclosing brand shape.
"""A rounded leaf-like square with a notch at its upper left holds the letters lm, the l rising from the notch into a lowercase m.

Symbol plan: Leaf-shaped enclosure with upper-left notch and lm monogram. Extremes (6,6)-(42,42).
Review notes: Retains the notched leaf frame and lm lettering, with paired circular m arches. Lucide square informs tangent corner construction. This dense nested candidate may need manual review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '312c3647-68c9-4bd9-afe9-f0a673e18486'
SOURCE_PATH = 'pictographic-primitives/logos/linux mint logo_312c3647-68c9-4bd9-afe9-f0a673e18486.svg'
AUTHOR = 'gpt-6'

class LinuxMintLogo(Solo48):
    icon_id = 'linux-mint-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('linux-mint', 'linux', 'operating-system', 'lm', 'logo', 'brand', 'open-source')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts
        path(self,'frame',(6,6),('L',(24,6)),('A',18,18,True,(42,24)),('L',(42,42)),('L',(24,42)),('L',(14,42)),('A',8,8,True,(6,34)),('L',(6,24)),('L',(6,6)),closed=True)
        poly(self,'l',(16,16),(16,24),(16,32),(24,32),(32,32))
        path(self,'m',(16,32),('L',(16,24)),('A',4,4,True,(24,24)),('A',4,4,True,(32,24)),('L',(32,32)))
        line(self,'middle',(24,24),(24,32))
        contacts(self)
