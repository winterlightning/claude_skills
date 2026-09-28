'Overhead barbell lifter: independent spacing revision.\n\nEight-unit weight/arm gaps and a filled head, retaining the overhead lifting pose.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0ef4671-045f-4232-9fac-dc95fbe6d288'
SOURCE_PATH = 'pictographic-primitives/sports/weightlift_d0ef4671-045f-4232-9fac-dc95fbe6d288.svg'
AUTHOR = 'gpt-6'

class OverheadBarbellLifter(Solo48):
    icon_id = 'overhead-barbell-lifter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('overhead', 'barbell', 'lifter', 'sport')

    def build(self):
        self.add_polyline('bar',(6, 18),(6, 6),(14, 6),(34, 6),(42, 6),(42, 18),closed=False)
        self.add_polyline('arms',(14, 6),(14, 32),(24, 32),(34, 32),(34, 6),closed=False)
        self.relate('connect','bar','arms')
        self.add_dot('head',(24, 19))
        self.add_line('torso',(24, 32),(24, 34))
        self.add_polyline('legs',(18, 42),(24, 34),(30, 42),closed=False)
        self.relate('connect','arms','torso')
        self.relate('connect','torso','legs')
