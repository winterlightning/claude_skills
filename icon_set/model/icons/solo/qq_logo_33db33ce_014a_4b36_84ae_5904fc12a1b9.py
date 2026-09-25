'qq-logo: independent smooth-curve repair.\n\nConstruction: Penguin silhouette with a round crown, smooth flippers and two small broad feet.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bird.svg and atomic-debug/bird.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '33db33ce-014a-4b36-84ae-5904fc12a1b9'
SOURCE_PATH = 'pictographic-primitives/logos/qq logo_33db33ce-014a-4b36-84ae-5904fc12a1b9.svg'
AUTHOR = 'gpt-6'


class QqLogo(Solo48):
    icon_id = 'qq-logo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('qq', 'logo', 'logos')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bird',(24,4),('C',(15,4),(13,11),(13,17)),('C',(13,24),(8,28),(8,34)),('C',(8,38),(13,36),(15,35)),('L',(13,41)),('C',(13,44),(20,44),(24,44)),('C',(28,44),(35,44),(35,41)),('L',(33,35)),('C',(35,36),(40,38),(40,34)),('C',(40,28),(35,24),(35,17)),('C',(35,11),(33,4),(24,4)),closed=True)
        contacts(self)
