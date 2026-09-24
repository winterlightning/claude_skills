"""Scientific Atom Symbol.

Plan: Three crossing elliptical orbits and circular nucleus. Bounds6,6,42,42. Retain three orbits; no false joins at crossings.
Construction reference: atom.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f2265828-4def-5cb0-be87-edeb3a4d341e'
SOURCE_PATH = 'pictographic-primitives/programing/amazon web service sagemaker_f2265828-4def-5cb0-be87-edeb3a4d341e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'atom-three-orbits-reference'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('atom', 'three', 'orbits', 'reference')

    def build(self):
        # Three coherent crossing orbits, with their shared intersections explicit.
        self.add_bezier('vertical',(24,4),((30,4),(33,12),(33,19)),((34,22),(34,26),(33,29)),((33,36),(30,44),(24,44)),((18,44),(15,36),(15,29)),((14,26),(14,22),(15,19)),((15,12),(18,4),(24,4)))
        self.add_bezier('diagonal-a',(7,14),((10,9),(18,11),(24,14)),((28,16),(30,17),(33,19)),((39,23),(44,29),(41,34)),((38,39),(30,37),(24,34)),((20,32),(18,31),(15,29)),((9,25),(4,19),(7,14)))
        self.add_bezier('diagonal-b',(41,14),((44,19),(39,25),(33,29)),((30,31),(28,32),(24,34)),((18,37),(10,39),(7,34)),((4,29),(9,23),(15,19)),((18,17),(20,16),(24,14)),((30,11),(38,9),(41,14)))
        self.relate('connect','vertical','diagonal-a','diagonal-b')
        self.add_dot('nucleus',(24,24))
