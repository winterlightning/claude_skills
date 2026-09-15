'Flamingo: independent spacing revision.\n\nOpen hooked neck and beak; ellipse body and separated supporting/tucked legs.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: bird: simplified body, open supporting limbs. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0eedad4e-672e-40c7-9399-bd5db48d8049'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flamingo_0eedad4e-672e-40c7-9399-bd5db48d8049.svg'
AUTHOR = 'gpt-6'

class Flamingo(Solo48):
    icon_id = 'flamingo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('flamingo', 'standing', 'one leg', 'bird', 'pink', 'tropical', 'wading', 'beak')

    def build(self):
        self.add_arc('bodya',(8, 29),(30, 29),radius_x=11,radius_y=5)
        self.add_arc('bodyb',(30, 29),(8, 29),radius_x=11,radius_y=5)
        self.add_contour('body','bodya','bodyb',closed=True)
        self.add_line('neck',(30, 29),(30, 10))
        self.add_arc('head',(30, 10),(36, 4),radius_x=6,radius_y=6,sweep=True)
        self.add_line('beak',(36, 4),(40, 4))
        self.add_contour('neck-head','neck','head','beak',closed=False)
        self.relate('connect','body','neck-head')
        self.add_line('leg',(19, 34),(19, 44))
        self.add_polyline('tucked',(19, 34),(8, 42),closed=False)
        self.relate('connect','body','leg')
        self.relate('connect','body','tucked')
