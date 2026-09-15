'microsoft-onedrive-logo: independent smooth-curve repair.\n\nConstruction: Three-lobed cloud emblem with crossing inner diagonals; coherent outer bowl and shared lobe junctions.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/cloud.svg and atomic-debug/cloud.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9661d55e-fb7b-4ad4-a213-c9622acb0fc6'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft onedrive logo 1_9661d55e-fb7b-4ad4-a213-c9622acb0fc6.svg'
AUTHOR = 'gpt-6'


class MicrosoftOnedriveLogoVariant2(Solo48):
    icon_id = 'microsoft-onedrive-logo-v2'
    variant_of = 'microsoft-onedrive-logo'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('onedrive', 'microsoft', 'cloud', 'storage', 'logo', 'brand', 'sync')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'cloud',(12,20),('A',12,12,True,(24,8)),('A',12,12,True,(36,20)),('C',(41,20),(44,25),(44,30)),('C',(44,36),(40,40),(34,40)),('L',(14,40)),('C',(8,40),(4,36),(4,30)),('C',(4,25),(7,20),(12,20)),closed=True)
        line(self,'diagonal-a',(12,20),(36,36));line(self,'diagonal-b',(36,20),(12,36))
        contacts(self)
