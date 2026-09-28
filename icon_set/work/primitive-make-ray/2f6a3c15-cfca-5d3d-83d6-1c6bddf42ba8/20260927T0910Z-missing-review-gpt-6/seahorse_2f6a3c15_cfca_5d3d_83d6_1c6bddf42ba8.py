'Seahorse: independent spacing revision.\n\nDeepen snout and fin; open inner tail return to preserve clearance around the curl.\nNative solo family, VRECT_M keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seahorse/20260927T084430Z-thuan-mac-1/reference/seahorse_2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8.svg'
AUTHOR = "gpt-6"

class Seahorse(Solo48):
    icon_id = 'seahorse'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('seahorse', 'sea', 'ocean', 'marine', 'fish', 'curl', 'tail', 'aquarium')

    def build(self):
        self.add_bezier('tail-start',(14,36),((8,38),(12,44),(20,44)))
        self.add_arc('tail-turn',(20, 44),(32, 32),radius_x=12,radius_y=12,sweep=False)
        self.add_line('back',(32, 32),(32, 20))
        self.add_arc('head-back',(32, 20),(40, 4),radius_x=20,radius_y=20,sweep=True)
        self.add_bezier('head-top',(40,4),((29,4),(27,10),(8,10)))
        self.add_line('snout-front',(8,10),(8,18))
        self.add_line('snout-bottom',(8,18),(20,18))
        self.add_arc('throat',(20, 18),(24, 22),radius_x=4,radius_y=4,sweep=True)
        self.add_arc('belly',(24, 22),(22, 32),radius_x=20,radius_y=20,sweep=False)

 
        self.add_contour('outline','tail-start','tail-turn','back','head-back','head-top','snout-front','snout-bottom','throat','belly',closed=False)
        self.add_polyline('fin',(32, 22),(40, 20),(40, 32),(32, 28),closed=False)
        self.relate('connect','outline','fin')
