"""Virtual Reality Headset.

Symbol plan: VR visor with broad curved upper band and central nose notch. All sides mirror around x=24. Lucide glasses informs bilateral front construction. Band simplified to smooth elliptical arch sharing side junctions.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56c21644-1317-469d-a939-8f46fe96b22c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable vr goggles_56c21644-1317-469d-a939-8f46fe96b22c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'vr-headset-with-broad-curved-upper-band'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('virtual', 'reality', 'headset')

    def build(self):
        self.add_line('top',(10,20),(38,20));self.add_arc('tr',(38,20),(44,26),radius_x=6)
        self.add_line('right',(44,26),(44,34));self.add_arc('br',(44,34),(38,40),radius_x=6)
        self.add_line('bottom-r',(38,40),(32,40));self.add_arc('nose-r',(32,40),(28,38),radius_x=5)
        self.add_arc('nose',(28,38),(20,38),radius_x=5,sweep=False)
        self.add_arc('nose-l',(20,38),(16,40),radius_x=5);self.add_line('bottom-l',(16,40),(10,40))
        self.add_arc('bl',(10,40),(4,34),radius_x=6);self.add_line('left',(4,34),(4,26));self.add_arc('tl',(4,26),(10,20),radius_x=6)
        self.add_contour('visor','top','tr','right','br','bottom-r','nose-r','nose','nose-l','bottom-l','bl','left','tl',closed=True)
        self.add_arc('band-left',(4,26),(14,8),radius_x=10,radius_y=18)
        self.add_line('band-top',(14,8),(34,8))
        self.add_arc('band-right',(34,8),(44,26),radius_x=10,radius_y=18)
        self.add_contour('band','band-left','band-top','band-right');self.relate('connect','band','visor')
