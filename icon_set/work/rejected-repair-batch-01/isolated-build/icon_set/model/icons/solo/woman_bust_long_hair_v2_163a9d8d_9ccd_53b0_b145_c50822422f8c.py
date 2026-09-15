'woman-bust-long-hair: independent smooth-curve repair.\n\nConstruction: Long-haired portrait on the tall envelope: circular head (24,25), radius 7; smooth shoulder crown y36 is exactly 4 centerline units below the jaw y32. Hair and shoulders share their ends.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/human_ref/user.svg (human proportions).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '163a9d8d-9ccd-53b0-b145-c50822422f8c'
SOURCE_PATH = 'pictographic-primitives/users/woman half_163a9d8d-9ccd-53b0-b145-c50822422f8c.svg'
AUTHOR = 'gpt-6'


class WomanBustLongHairVariant2(Solo48):
    icon_id = 'woman-bust-long-hair-v2'
    variant_of = 'woman-bust-long-hair'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/users'
    aliases = ()
    keywords = ('woman', 'female', 'bust', 'long hair', 'user', 'avatar', 'profile', 'person')
    keyshape = Keyshape.VRECT_L
    human_construction = 'bust'

    def build(self):
        ellipse(self,'head',24,25,7)
        path(self,'hair',(8,44),('L',(8,24)),('A',16,20,True,(24,4)),('A',16,20,True,(40,24)),('L',(40,44)))
        path(self,'shoulders',(8,44),('A',16,8,True,(24,36)),('A',16,8,True,(40,44)))
        self.relate('connect','head','shoulders')
        contacts(self)
