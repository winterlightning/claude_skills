from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '05bd420f-ccd3-45f2-a021-10901b4a7362'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tog/20260925T034659Z-thuan-mac/reference/tog_05bd420f-ccd3-45f2-a021-10901b4a7362.svg'
AUTHOR = 'gpt-6'
# Plan: folded duvet with three equal rising warmth waves; user clarified thermal tog rating.
# HRECT_L extremes (4,8)-(44,40); 10-unit centerline wave-to-duvet gap.
# Lucide heater: repeated rising heat strokes, reauthored with tangent circular arcs.
class AuthoredIcon(Solo48):
    icon_id = 'tog'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('duvet warmth','thermal insulation')
    keywords = ('tog','duvet','warmth','insulation','rating')
    def build(self):
        for i,x in enumerate((12,24,36)):
            self.add_arc(f'heat-lower-{i}',(x,16),(x,12),radius_x=2,sweep=False)
            self.add_arc(f'heat-upper-{i}',(x,12),(x,8),radius_x=2)
            self.add_contour(f'heat-{i}',f'heat-lower-{i}',f'heat-upper-{i}')
        self.add_line('top-1',(8,26),(28,26))
        self.add_line('top-2',(28,26),(40,26))
        self.add_arc('tr',(40,26),(44,30),radius_x=4)
        self.add_line('right',(44,30),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom-1',(40,40),(28,40))
        self.add_line('bottom-2',(28,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,30))
        self.add_arc('tl',(4,30),(8,26),radius_x=4)
        self.add_contour('duvet','top-1','top-2','tr','right','br','bottom-1','bottom-2','bl','left','tl',closed=True)
        self.add_line('fold',(28,26),(28,40))
        self.relate('connect','fold','duvet')
