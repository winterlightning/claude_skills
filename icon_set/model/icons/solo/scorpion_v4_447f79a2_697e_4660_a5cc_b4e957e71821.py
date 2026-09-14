# Variant of scorpion-v2; parent file remains unchanged.
'Scorpion v2: independent spacing revision.\n\nOpen eight-unit pincers and reduce crowded legs to one clear pair; preserve curled tail.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '447f79a2-697e-4660-a5cc-b4e957e71821'
SOURCE_PATH = 'pictographic-primitives/animals/insect scorpion_447f79a2-697e-4660-a5cc-b4e957e71821.svg'
AUTHOR = 'gpt-6'

class ScorpionVariant4(Solo48):
    icon_id = 'scorpion-v4'
    variant_of = 'scorpion-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('scorpion', 'sting', 'claws', 'arachnid', 'tail', 'desert', 'venom', 'zodiac')

    def build(self):
        self.add_arc('body-top',(18, 24),(30, 24),radius_x=6,radius_y=6,sweep=True)
        self.add_line('body-right',(30, 24),(30, 28))
        self.add_arc('body-bottom-right',(30, 28),(24, 34),radius_x=6,radius_y=6,sweep=True)
        self.add_arc('body-bottom-left',(24, 34),(18, 28),radius_x=6,radius_y=6,sweep=True)
        self.add_line('body-left',(18, 28),(18, 24))
        self.add_contour('body','body-top','body-right','body-bottom-right','body-bottom-left','body-left',closed=True)
        self.add_line('claw-left-outer',(6, 6),(6, 10))
        self.add_arc('claw-left-a',(6, 10),(10, 14),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('claw-left-b',(10, 14),(14, 10),radius_x=4,radius_y=4,sweep=False)
        self.add_line('claw-left-inner',(14, 10),(14, 6))
        self.add_contour('claw-left','claw-left-outer','claw-left-a','claw-left-b','claw-left-inner',closed=False)
        self.add_line('claw-right-outer',(42, 6),(42, 10))
        self.add_arc('claw-right-a',(42, 10),(38, 14),radius_x=4,radius_y=4,sweep=True)
        self.add_arc('claw-right-b',(38, 14),(34, 10),radius_x=4,radius_y=4,sweep=True)
        self.add_line('claw-right-inner',(34, 10),(34, 6))
        self.add_contour('claw-right','claw-right-outer','claw-right-a','claw-right-b','claw-right-inner',closed=False)
        self.add_polyline('arm-left',(10, 14),(10, 18),(18, 24),closed=False)
        self.add_polyline('arm-right',(38, 14),(38, 18),(30, 24),closed=False)
        self.add_polyline('leg-left',(18, 28),(6, 30),closed=False)
        self.add_polyline('leg-right',(30, 28),(42, 30),closed=False)
        self.add_arc('tail-turn',(24, 34),(14, 42),radius_x=10,radius_y=8,sweep=True)
        self.add_line('tail-tip',(14, 42),(6, 42))
        self.add_contour('tail','tail-turn','tail-tip',closed=False)
        self.relate('connect','claw-left','arm-left')
        self.relate('connect','claw-right','arm-right')
        self.relate('connect','arm-left','body')
        self.relate('connect','arm-right','body')
        self.relate('connect','leg-left','body')
        self.relate('connect','leg-right','body')
        self.relate('connect','tail','body')
