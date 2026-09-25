'Sleeping deer: independent spacing revision.\n\nBroader curled body and forked antler; omit cramped sleep mark.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ce1c8b37-f882-45e5-9fea-ed732cc8d936'
SOURCE_PATH = 'pictographic-primitives/animals/deer sleep_ce1c8b37-f882-45e5-9fea-ed732cc8d936.svg'
AUTHOR = 'gpt-6'

class SleepingDeer(Solo48):
    icon_id = 'sleeping-deer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('deer', 'sleep', 'rest', 'curled', 'antlers', 'night', 'zzz', 'animal')

    def build(self):
        self.add_arc('rump',(6, 32),(16, 22),radius_x=10,radius_y=10,sweep=True)
        self.add_line('tuck',(16, 22),(20, 22))
        self.add_arc('muzzle',(20, 22),(20, 14),radius_x=4,radius_y=4,sweep=True)
        self.add_polyline('face',(20, 14),(34, 10),(34, 16),closed=False)
        self.add_arc('neck',(34, 16),(42, 26),radius_x=14,radius_y=14,sweep=False)
        self.add_arc('underside',(42, 26),(24, 42),radius_x=18,radius_y=16,sweep=True)
        self.add_line('bottom',(24, 42),(16, 42))
        self.add_arc('haunch',(16, 42),(6, 32),radius_x=10,radius_y=10,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'face']
        self.add_contour('deer','rump','tuck','muzzle','face-1','face-2','neck','underside','bottom','haunch',closed=True)
        self.add_polyline('antler',(27, 12),(20, 6),(12, 6),closed=False)
        self.relate('connect','deer','antler')
