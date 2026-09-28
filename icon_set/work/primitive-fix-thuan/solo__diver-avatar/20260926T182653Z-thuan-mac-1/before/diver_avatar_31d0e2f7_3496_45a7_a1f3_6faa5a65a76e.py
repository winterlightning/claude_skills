'diver-avatar: independent smooth-curve repair.\n\nConstruction: Diver bust with circular head, closed paired goggles and symmetric shoulder arch. Head bottom y30, shoulder crown y34: exactly 4 centerline units gives touching ink as required for a bust.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/human_ref/user.svg (human proportions).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '31d0e2f7-3496-45a7-a1f3-6faa5a65a76e'
SOURCE_PATH = 'pictographic-primitives/avatars/diver_31d0e2f7-3496-45a7-a1f3-6faa5a65a76e.svg'
AUTHOR = 'gpt-6'


class DiverAvatar(Solo48):
    icon_id = 'diver-avatar'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('diver', 'portrait', 'bust')
    keyshape = Keyshape.VRECT_L
    human_construction = 'bust'

    def build(self):
        ellipse(self,'head',24,17,13)
        line(self,'mask-top',(11,17),(37,17))
        path(self,'mask-bottom',(11,17),('C',(17,26),(20,26),(24,21)),('C',(28,26),(31,26),(37,17)))
        path(self,'shoulders',(8,44),('A',16,10,True,(24,34)),('A',16,10,True,(40,44)))
        line(self,'zipper',(24,34),(24,44))
        self.relate('connect','head','shoulders')
        contacts(self)
