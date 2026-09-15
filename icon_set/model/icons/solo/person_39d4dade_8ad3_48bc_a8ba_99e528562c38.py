'person: independent smooth-curve repair.\n\nConstruction: Person with detached circular head and lifted curved arms. Head lower edge 18, shoulder/torso node 26 gives exactly four units of ink gap.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/human_ref/user.svg (human proportions).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'pictographic-primitives/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'
AUTHOR = 'gpt-6'


class Person(Solo48):
    icon_id = 'person'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('person', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        ellipse(self,'head',24,11,7)
        path(self,'left-arm',(24,26),('C',(18,26),(12,32),(8,32)))
        path(self,'right-arm',(24,26),('C',(30,26),(36,32),(40,32)))
        line(self,'torso',(24,26),(24,44))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        contacts(self)
