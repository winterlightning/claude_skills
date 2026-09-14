# Variant of standing-lion; parent file remains unchanged.
'Standing lion: independent spacing revision.\n\nClear teardrop mane, simple eye, eight-unit paws and open raised tail; remove crowded inner muzzle.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48ee2f2f-fef8-43a6-b301-d910d4dce828'
SOURCE_PATH = 'pictographic-primitives/animals/lion body_48ee2f2f-fef8-43a6-b301-d910d4dce828.svg'
AUTHOR = 'gpt-6'

class StandingLionVariant3(Solo48):
    icon_id = 'standing-lion-v3'
    variant_of = 'standing-lion'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('standing', 'lion', 'animal')

    def build(self):
        self.add_arc('crown',(4, 18),(14, 8),radius_x=10,radius_y=10,sweep=True)
        self.add_arc('mane-right',(14, 8),(26, 20),radius_x=12,radius_y=12,sweep=True)
        self.add_arc('mane-low',(26, 20),(18, 34),radius_x=8,radius_y=14,sweep=True)
        self.add_arc('mane-left',(18, 34),(4, 24),radius_x=14,radius_y=10,sweep=True)
        self.add_line('snout',(4, 24),(4, 18))
        self.add_contour('mane','crown','mane-right','mane-low','mane-left','snout',closed=True)
        self.add_dot('eye',(14, 20))
        self.add_line('back',(26, 20),(36, 20))
        self.add_arc('rump',(36, 20),(44, 28),radius_x=8,radius_y=8,sweep=True)
        self.add_polyline('legs',(44, 28),(44, 40),(36, 40),(36, 32),(26, 32),(26, 40),(18, 40),(18, 34),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'legs']
        self.add_contour('body','back','rump','legs-1','legs-2','legs-3','legs-4','legs-5','legs-6','legs-7',closed=False)
        self.add_line('tail',(44, 28),(44, 10))
        self.relate('connect','mane','body')
        self.relate('connect','body','tail')
