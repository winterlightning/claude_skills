'open-eyes: independent smooth-curve repair.\n\nConstruction: Eye with two coherent symmetrical lid curves and a true circular pupil.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/eye.svg and atomic-debug/eye.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '47a44264-9c90-4733-bd24-6bfdf39290df'
SOURCE_PATH = 'pictographic-primitives/interface-essential/open eyes_47a44264-9c90-4733-bd24-6bfdf39290df.svg'
AUTHOR = 'gpt-6'


class OpenEyesVariant2(Solo48):
    icon_id = 'open-eyes-v2'
    variant_of = 'open-eyes'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'eyes', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'eye',(4,24),('C',(10,15),(16,8),(24,8)),('C',(32,8),(38,15),(44,24)),('C',(38,33),(32,40),(24,40)),('C',(16,40),(10,33),(4,24)),closed=True)
        ellipse(self,'pupil',24,24,5)
        contacts(self)
