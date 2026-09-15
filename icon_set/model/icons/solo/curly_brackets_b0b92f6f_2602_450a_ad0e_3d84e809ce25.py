'curly-brackets: independent smooth-curve repair.\n\nConstruction: Two mirrored braces, each made of four flowing cubics with coherent vertical end tangents.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/braces.svg and atomic-debug/braces.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b0b92f6f-2602-450a-ad0e-3d84e809ce25'
SOURCE_PATH = 'pictographic-primitives/programing/curly brackets_b0b92f6f-2602-450a-ad0e-3d84e809ce25.svg'
AUTHOR = 'gpt-6'


class CurlyBrackets(Solo48):
    icon_id = 'curly-brackets'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'left',(18,4),('C',(12,4),(12,9),(12,14)),('C',(12,19),(12,24),(8,24)),('C',(12,24),(12,29),(12,34)),('C',(12,39),(12,44),(18,44)))
        path(self,'right',(30,4),('C',(36,4),(36,9),(36,14)),('C',(36,19),(36,24),(40,24)),('C',(36,24),(36,29),(36,34)),('C',(36,39),(36,44),(30,44)))
        contacts(self)
