'drooling-face-with-open-mouth: independent smooth-curve repair.\n\nConstruction: Drooling face: circular border, paired eyes, open capsule mouth and a short centered drool stroke. Raise the mouth for clear separation from the border.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e03af256-a23a-5002-a487-fd64003fccc3'
SOURCE_PATH = 'pictographic-primitives/smileys/drool_e03af256-a23a-5002-a487-fd64003fccc3.svg'
AUTHOR = 'gpt-6'


class DroolingFaceWithOpenMouth(Solo48):
    icon_id = 'drooling-face-with-open-mouth'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drooling', 'drool', 'mouth', 'hungry', 'face', 'emoji')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        self.add_dot('eye-left',(17,15));self.add_dot('eye-right',(31,15))
        ellipse(self,'mouth',24,28,6,4)
        line(self,'drool',(24,32),(24,35))
        contacts(self)
