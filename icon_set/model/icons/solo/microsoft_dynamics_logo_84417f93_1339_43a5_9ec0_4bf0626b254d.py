# Repair: Preserve the Dynamics folded ribbon; shorten its internal diagonal before it creates a narrow triangular pinch at the lower corner.
"""A right-pointing triangle outline made of angled planes, with a shorter inner stroke folding back from its upper left edge.

Symbol plan: Two right-pointing planes with a folded upper-left stroke and a shared lower-left/right junction. Extremes (8,4)-(40,44).
Review notes: Keeps the folded triangle and lower perspective plane. The left opening is enlarged for clearance. No useful Lucide brand match; angular direction and asymmetry carry the logo identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84417f93-1339-43a5-9ec0-4bf0626b254d'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft dynamics logo_84417f93-1339-43a5-9ec0-4bf0626b254d.svg'
AUTHOR = 'gpt-6'

class MicrosoftDynamicsLogo(Solo48):
    icon_id = 'microsoft-dynamics-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('microsoft-dynamics', 'dynamics', 'microsoft', 'crm', 'logo', 'brand', 'business')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        poly(self,'main',(8,24),(8,44),(40,28),(40,18),(8,4),(8,14),(22,22))
        line(self,'fold',(40,18),(24,26))
        contacts(self)
