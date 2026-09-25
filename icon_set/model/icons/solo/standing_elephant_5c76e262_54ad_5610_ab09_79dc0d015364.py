'Standing elephant: independent spacing revision.\n\nOpen trunk tip and eight-unit legs; large ear retained without narrow doubled trunk.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c76e262-54ad-5610-ab09-79dc0d015364'
SOURCE_PATH = 'pictographic-primitives/animals/elephant_5c76e262-54ad-5610-ab09-79dc0d015364.svg'
AUTHOR = 'gpt-6'

class StandingElephant(Solo48):
    icon_id = 'standing-elephant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('standing', 'elephant')

    def build(self):
        self.add_arc('brow',(4, 20),(16, 8),radius_x=12,radius_y=12,sweep=True)
        self.add_line('crown',(16, 8),(28, 8))
        self.add_arc('ear',(28, 8),(18, 24),radius_x=10,radius_y=16,sweep=True)
        self.add_contour('head','brow','crown','ear',closed=False)
        self.add_line('trunk',(4, 20),(4, 34))
        self.add_arc('trunk-tip',(4, 34),(8, 38),radius_x=4,radius_y=4,sweep=False)
        self.add_contour('trunk-shape','trunk','trunk-tip',closed=False)
        self.add_polyline('shoulder',(28, 8),(34, 14),closed=False)
        self.add_arc('back',(34, 14),(44, 24),radius_x=10,radius_y=10,sweep=True)
        self.add_polyline('legs',(44, 24),(44, 40),(36, 40),(36, 30),(26, 30),(26, 40),(18, 40),(18, 24),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'shoulder']
        self.contours = [c for c in self.contours if c.contour_id != 'legs']
        self.add_contour('body','shoulder-1','back','legs-1','legs-2','legs-3','legs-4','legs-5','legs-6','legs-7',closed=False)
        self.relate('connect','head','body')
        self.relate('connect','head','trunk-shape')
