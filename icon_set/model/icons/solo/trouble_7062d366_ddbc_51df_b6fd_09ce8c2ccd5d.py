'trouble: independent smooth-curve repair.\n\nConstruction: Sad face with a true circular border and two smooth drooping eyes; broad downturned mouth.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7062d366-ddbc-51df-b6fd-09ce8c2ccd5d'
SOURCE_PATH = 'pictographic-primitives/smileys/trouble_7062d366-ddbc-51df-b6fd-09ce8c2ccd5d.svg'
AUTHOR = 'gpt-6'


class Trouble(Solo48):
    icon_id = 'trouble'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('trouble', 'smileys')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        path(self,'left-eye',(18,15),('C',(18,18),(17,19),(15,20)))
        path(self,'right-eye',(30,15),('C',(30,18),(31,19),(33,20)))
        path(self,'mouth',(16,31),('C',(20,25),(28,25),(32,31)))
        contacts(self)
