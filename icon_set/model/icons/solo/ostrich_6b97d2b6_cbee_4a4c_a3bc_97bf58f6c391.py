'Ostrich: independent spacing revision.\n\nOpen long neck and two separated legs; remove cramped neck outline and foot returns.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: bird: simplified body, open supporting limbs. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391.svg'
AUTHOR = 'gpt-6'

class Ostrich(Solo48):
    icon_id = 'ostrich'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('ostrich', 'emu', 'bird', 'standing', 'neck', 'legs', 'flightless', 'africa')

    def build(self):
        self.add_arc('bodya',(6, 27),(30, 27),radius_x=12,radius_y=6)
        self.add_arc('bodyb',(30, 27),(6, 27),radius_x=12,radius_y=6)
        self.add_contour('body','bodya','bodyb',closed=True)
        self.add_line('neck',(30, 27),(30, 12))
        self.add_arc('head',(30, 12),(36, 6),radius_x=6,radius_y=6,sweep=True)
        self.add_line('beak',(36, 6),(42, 6))
        self.add_contour('neck-head','neck','head','beak',closed=False)
        self.relate('connect','body','neck-head')
        self.add_polyline('left-leg',(18, 33),(18, 42),(22, 42),closed=False)
        self.add_polyline('right-leg',(30, 27),(30, 42),(36, 42),closed=False)
        self.relate('connect','body','left-leg')
        self.relate('connect','body','right-leg')
