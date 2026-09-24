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
        self.add_bezier('vertical',(24,4),((30,4),(30,15),(30,21)),((30,23),(30,25),(30,27)),((30,33),(30,44),(24,44)),((18,44),(18,33),(18,27)),((18,25),(18,23),(18,21)),((18,15),(18,4),(24,4)))
        self.add_bezier('diagonal-a',(7,14),((10,9),(19,15),(24,18)),((26,19),(28,20),(30,21)),((35,24),(44,29),(41,34)),((38,39),(29,33),(24,30)),((22,29),(20,28),(18,27)),((13,24),(4,19),(7,14)))
        self.add_bezier('diagonal-b',(41,14),((44,19),(35,24),(30,27)),((28,28),(26,29),(24,30)),((19,33),(10,39),(7,34)),((4,29),(13,24),(18,21)),((20,20),(22,19),(24,18)),((29,15),(38,9),(41,14)))
        self.relate('connect','vertical','diagonal-a','diagonal-b')
        self.add_dot('nucleus',(24,24))
