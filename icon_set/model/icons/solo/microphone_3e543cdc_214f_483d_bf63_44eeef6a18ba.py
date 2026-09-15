'microphone: independent smooth-curve repair.\n\nConstruction: Microphone capsule, smooth U-shaped cradle and a central stand; wide capsule clearance.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/mic.svg and atomic-debug/mic.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3e543cdc-214f-483d-bf63-44eeef6a18ba'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.svg'
AUTHOR = 'gpt-6'


class Microphone(Solo48):
    icon_id = 'microphone'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'capsule',18,4,30,28,6)
        path(self,'cradle',(8,26),('L',(8,28)),('A',16,12,False,(24,40)),('A',16,12,False,(40,28)),('L',(40,26)))
        line(self,'stand',(24,40),(24,44))
        contacts(self)
