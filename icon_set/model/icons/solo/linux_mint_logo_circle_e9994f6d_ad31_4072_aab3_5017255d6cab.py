# Repair: Retain the LM monogram, with the L sharing the left stem and baseline. Equal 8-unit m arches fit the enclosing brand shape.
"""A large circle holds a lowercase m whose left stem rises tall and rounds into the letter base, forming the letters lm.

Symbol plan: Circular enclosure around l and two repeated m arches; radial centerline radius20.
Review notes: Lucide circle supplies enclosure construction. lm monogram is retained; repeated arches share radius and baseline. Tight internal holes must remain visible in validation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9994f6d-ad31-4072-aab3-5017255d6cab'
SOURCE_PATH = 'pictographic-primitives/logos/linux mint logo 1_e9994f6d-ad31-4072-aab3-5017255d6cab.svg'
AUTHOR = 'gpt-6'

class LinuxMintLogoCircle(Solo48):
    icon_id = 'linux-mint-logo-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('linux-mint', 'linux', 'operating-system', 'lm', 'logo', 'brand', 'circle')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts
        ellipse(self,'frame',24,24,20)
        poly(self,'l',(16,16),(16,24),(16,32),(24,32),(32,32))
        path(self,'m',(16,32),('L',(16,24)),('A',4,4,True,(24,24)),('A',4,4,True,(32,24)),('L',(32,32)))
        line(self,'middle',(24,24),(24,32))
        contacts(self)
