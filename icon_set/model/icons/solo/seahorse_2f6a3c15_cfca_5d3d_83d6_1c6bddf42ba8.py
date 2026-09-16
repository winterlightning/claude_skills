'Seahorse: independent spacing revision.\n\nDeepen snout and fin; open inner tail return to preserve clearance around the curl.\nNative solo family, VRECT_M keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8'
SOURCE_PATH = 'pictographic-primitives/animals/seahorse_2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8.svg'
AUTHOR = 'gpt-6'

class Seahorse(Solo48):
    icon_id = 'seahorse'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('seahorse', 'sea', 'ocean', 'marine', 'fish', 'curl', 'tail', 'aquarium')

    def build(self):
        self.add_polyline('tail-start',(14, 36),(8, 40),(20, 44),closed=False)
        self.add_arc('tail-turn',(20, 44),(32, 32),radius_x=12,radius_y=12,sweep=False)
        self.add_line('back',(32, 32),(32, 20))
        self.add_arc('head-back',(32, 20),(40, 4),radius_x=20,radius_y=20,sweep=True)
        self.add_polyline('head',(40, 4),(24, 4),(8, 10),(8, 18),(20, 18),closed=False)
        self.add_arc('throat',(20, 18),(24, 22),radius_x=4,radius_y=4,sweep=True)
        self.add_arc('belly',(24, 22),(22, 32),radius_x=20,radius_y=20,sweep=False)
        self.contours = [c for c in self.contours if c.contour_id != 'tail-start']
        self.contours = [c for c in self.contours if c.contour_id != 'head']
        self.add_contour('outline','tail-start-1','tail-start-2','tail-turn','back','head-back','head-1','head-2','head-3','head-4','throat','belly',closed=False)
        self.add_polyline('fin',(32, 22),(40, 20),(40, 32),(32, 28),closed=False)
        self.relate('connect','outline','fin')
