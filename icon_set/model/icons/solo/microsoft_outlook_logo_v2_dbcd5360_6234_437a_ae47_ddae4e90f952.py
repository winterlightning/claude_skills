'microsoft-outlook-logo: distinct review variant.\n\nConstruction: Outlook logo reduced to its recognizable O tile in front of an exposed envelope; preserve the intentional left-right asymmetry.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'dbcd5360-6234-437a-ae47-ddae4e90f952'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft outlook logo_dbcd5360-6234-437a-ae47-ddae4e90f952.svg'
AUTHOR = 'gpt-6'


class MicrosoftOutlookLogoVariant2(Solo48):
    icon_id = 'microsoft-outlook-logo-v2'
    variant_of = 'microsoft-outlook-logo'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'outlook', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'tile',4,8,30,40,3,ys=(12,20))
        ellipse(self,'letter-o',17,24,4,7)
        path(self,'mail',(30,12),('L',(40,12)),('A',4,4,True,(44,16)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(30,40)))
        poly(self,'flap',(30,20),(37,27),(44,20))
        contacts(self)
