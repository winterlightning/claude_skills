'unhappy-smileys: independent smooth-curve repair.\n\nConstruction: Sad face with a true circular border and two smooth drooping eyes; broad downturned mouth.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9487fd87-0dff-5369-a29c-12ab49c0e6f5'
SOURCE_PATH = 'pictographic-primitives/smileys/unhappy_9487fd87-0dff-5369-a29c-12ab49c0e6f5.svg'
AUTHOR = 'gpt-6'


class UnhappySmileysVariant2(Solo48):
    icon_id = 'unhappy-smileys-v2'
    variant_of = 'unhappy-smileys'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        path(self,'left-eye',(18,15),('C',(18,18),(17,19),(15,20)))
        path(self,'right-eye',(30,15),('C',(30,18),(31,19),(33,20)))
        path(self,'mouth',(16,31),('C',(20,25),(28,25),(32,31)))
        contacts(self)
