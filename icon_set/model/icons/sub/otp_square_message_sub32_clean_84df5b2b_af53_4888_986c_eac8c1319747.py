"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '84df5b2b-af53-4888-986c-eac8c1319747'
SOURCE_PATH = 'pictographic-primitives/state/message otp_84df5b2b-af53-4888-986c-eac8c1319747.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'uppercase OTP in source order')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': 'ef69ef35592ceff5f8f5d01c79bb32b4ca626a566d48b74624664ea2228ff4c3'}
    icon_id = 'otp-square-message-sub32-clean'
    variant_of = 'otp-square-message-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'OTP Message Bubble', 'core_parts': ('rounded square speech bubble', 'lower-left tail', 'uppercase OTP in source order'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Deepen the speech bubble and rebalance the three reused letters with a wider right margin.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'letter-t-uppercase', 'letter-p-uppercase')
    def build(self):
        self.message()
        self.primitives.append(Bezier('text-O-0-0-0-0',Point(*(6, 15)),Point(*(11, 15)),(((6, 14), (6, 12), (7, 11)), ((7, 11), (8, 10), (8, 10)), ((9, 10), (10, 11), (10, 11)), ((11, 12), (11, 14), (11, 15)))))
        self.primitives.append(Bezier('text-O-0-0-0-1',Point(*(11, 15)),Point(*(6, 15)),(((11, 16), (11, 18), (10, 19)), ((10, 19), (9, 20), (8, 20)), ((8, 20), (7, 19), (7, 19)), ((6, 18), (6, 16), (6, 15)))))
        self.add_contour('glyph-O-0-0-0',*['text-O-0-0-0-0', 'text-O-0-0-0-1'],closed=True)
        self.add_line('text-T-0-0-0-0',(15, 10),(19, 10))
        self.add_line('text-T-0-1-0-0',(17, 10),(17, 20))
        self.add_line('text-P-0-0-0-0',(23, 20),(23, 10))
        self.add_line('text-P-0-0-0-1',(23, 10),(25, 10))
        self.add_contour('glyph-P-0-0-0',*['text-P-0-0-0-0', 'text-P-0-0-0-1'],closed=False)
        self.primitives.append(Bezier('text-P-0-0-1-0',Point(*(25, 10)),Point(*(25, 15)),(((28, 10), (28, 15), (25, 15)),)))
        self.add_line('text-P-0-0-2-0',(25, 15),(23, 15))

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,25))
        self.add_arc('frame-br',(30,25),(28,27),radius_x=2)
        tail=[(28,27),(15,27),(9,30),(9,27),(4,27)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,27),(2,25),radius_x=2)
        self.add_line('frame-left',(2,25),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)

