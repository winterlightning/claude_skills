'Two way label: independent spacing revision.\n\nKeep every character, wrapped as 2W / AY, with ten units beside the curved numeral and eight between rows.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: type and percent: consistent monoline characters and separated counters. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd9bea8f-8517-461f-8200-f3e2227f3c22'
SOURCE_PATH = 'pictographic-primitives/symbol/2 way (text)_cd9bea8f-8517-461f-8200-f3e2227f3c22.svg'
AUTHOR = 'gpt-6'

class TwoWayLabel(Solo48):
    icon_id = 'two-way-label'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/labels'
    aliases = ()
    keywords = ('2-way', 'two-way', 'bidirectional', 'label', 'text', 'exchange', 'traffic', 'two')

    def build(self):
        self.add_arc('two-top',(6,10),(16,10),radius_x=5,radius_y=4)
        self.add_polyline('two-base',(16,10),(6,18),(18,18))
        self.relate('connect','two-top','two-base')
        self.add_polyline('w',(26, 6),(26, 18),(34, 10),(42, 18),(42, 6),closed=False)
        self.add_polyline('a',(10, 42),(10, 34),(10, 26),(18, 26),(18, 34),(18, 42),closed=False)
        self.add_line('a-bar',(10, 34),(18, 34))
        self.relate('connect','a','a-bar')
        self.add_polyline('y',(30, 26),(34, 34),(38, 26),closed=False)
        self.add_line('y-stem',(34, 34),(34, 42))
        self.relate('connect','y','y-stem')
