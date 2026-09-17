"""Smart Augmented Reality Glasses.

Symbol plan: AR glasses with deep nose notch and upper-left integral display corner. Paired exterior lobes use shared y coordinates; display is deliberately asymmetric. Lucide glasses informs lens/bridge hierarchy. Display enlarged to an 8-unit cell.
Keyshape HRECT_M; exact visible bounds (2, 8, 46, 40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3f157a4-4ba4-56cb-af69-39f5c5fe3376'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/device google glass_f3f157a4-4ba4-56cb-af69-39f5c5fe3376.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'augmented-reality-glasses-with-corner-display'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('smart', 'augmented', 'reality', 'glasses')

    def build(self):
        self.run('top',(8,10),(16,10),(40,10));self.add_arc('tr',(40,10),(44,14),radius_x=4)
        self.add_line('right',(44,14),(44,34));self.add_arc('br',(44,34),(40,38),radius_x=4)
        self.add_line('bottom-r',(40,38),(34,38));self.add_arc('lower-r',(34,38),(30,34),radius_x=4)
        self.add_line('nose-r',(30,34),(28,28));self.add_arc('nose',(28,28),(20,28),radius_x=4,sweep=False)
        self.add_line('nose-l',(20,28),(18,34));self.add_arc('lower-l',(18,34),(14,38),radius_x=4)
        self.add_line('bottom-l',(14,38),(8,38));self.add_arc('bl',(8,38),(4,34),radius_x=4)
        self.run('left',(4,34),(4,18),(4,14));self.add_arc('tl',(4,14),(8,10),radius_x=4)
        self.add_contour('frame','top-1','top-2','tr','right','br','bottom-r','lower-r','nose-r','nose','nose-l','lower-l','bottom-l','bl','left-1','left-2','tl',closed=True)
        self.add_polyline('display',(4,18),(16,18),(16,10));self.relate('connect','display','frame')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'{name}-{i}',a,b)
