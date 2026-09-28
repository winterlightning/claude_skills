"""Modern Smart Glasses.

Symbol plan: One smart-glasses frame with paired raised temple arms. Shared x=24 axis, mirrored lens lobes and radius-4 corners. Lucide glasses informs rising temples and bridge; source supplies broad front. Simplify curled tips to short inward returns.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41ea4710-5cbf-4487-a05e-e8508ef3ba58'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/google glass_41ea4710-5cbf-4487-a05e-e8508ef3ba58.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'smart-glasses-with-raised-temple-arms'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('modern', 'smart', 'glasses')

    def build(self):
        self.add_line('top',(4,24),(44,24))
        self.add_line('right',(44,24),(44,36));self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom-r',(40,40),(32,40));self.add_arc('notch-r',(32,40),(28,36),radius_x=4)
        self.add_arc('nose',(28,36),(20,36),radius_x=4,sweep=False)
        self.add_arc('notch-l',(20,36),(16,40),radius_x=4)
        self.add_line('bottom-l',(16,40),(8,40));self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,24))
        self.add_contour('frame','top','right','br','bottom-r','notch-r','nose','notch-l','bottom-l','bl','left',closed=True)
        for i in range(2):
            def q(x,y):return (x if i==0 else 48-x,y)
            self.add_line(f'arm-{i}',q(4,24),q(8,12));self.add_arc(f'tip-{i}',q(8,12),q(12,8),radius_x=4,sweep=i==0)
            self.add_line(f'end-{i}',q(12,8),q(14,8));self.add_contour(f'temple-{i}',f'arm-{i}',f'tip-{i}',f'end-{i}');self.relate('connect',f'temple-{i}','frame')
