'microsoft-visual-studio-logo: independent smooth-curve repair.\n\nConstruction: Visual Studio bow-tie silhouette with equal end loops and a shared crossing.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/infinity.svg and atomic-debug/infinity.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f23c1fcf-345a-4ef4-b844-ecdca619586a'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft visual studio logo_f23c1fcf-345a-4ef4-b844-ecdca619586a.svg'
AUTHOR = 'gpt-6'


class MicrosoftVisualStudioLogoVariant2(Solo48):
    icon_id = 'microsoft-visual-studio-logo-v2'
    variant_of = 'microsoft-visual-studio-logo'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'left',(4,12),(10,8),(24,24),(10,40),(4,36),closed=True)
        poly(self,'right',(44,12),(38,8),(24,24),(38,40),(44,36),closed=True)
        contacts(self)
