"""Rearing cobra with flared hood and wide base coil. Extrema (6,6)-(42,42). Hood sits left of the rising tail; short raised tail restored. No useful Lucide match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2629056c-fce2-5c6a-9cb5-0859b52071a1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hooded-cobra/20260927T145836Z-thuan-mac-1/reference/reptile cobra_2629056c-fce2-5c6a-9cb5-0859b52071a1.svg'
AUTHOR = "gpt-6"

class HoodedCobra(Solo48):
    icon_id = 'hooded-cobra'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'coil', 'venom', 'rear')

    def build(self):
        # Symmetric hood uses radius-12 quarters; base coil has a full 8-unit centerline opening and radius-4 ends. Eye pair shares y=16. No useful Lucide cobra match.
        self.add_line('head-top', (16, 6), (28, 6))
        self.add_arc('hood-right', (28, 6), (36, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('taper-right', (36, 14), (26, 26), radius_x=10, radius_y=12, sweep=True)
        self.add_line('neck-right', (26, 26), (26, 34))
        self.add_line('coil-top-right', (26, 34), (38, 34))
        self.add_arc('coil-right', (38, 34), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-bottom', (38, 42), (10, 42))
        self.add_arc('coil-left', (10, 42), (10, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-top-left', (10, 34), (18, 34))
        self.add_line('neck-left', (18, 34), (18, 26))
        self.add_arc('taper-left', (18, 26), (8, 14), radius_x=10, radius_y=12, sweep=True)
        self.add_arc('hood-left', (8, 14), (16, 6), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('outline', 'head-top', 'hood-right', 'taper-right', 'neck-right', 'coil-top-right', 'coil-right', 'coil-bottom', 'coil-left', 'coil-top-left', 'neck-left', 'taper-left', 'hood-left', closed=True)
        # The source is an eyeless cobra silhouette with a slim raised neck.
        self.add_line('raised-tail',(38,34),(42,26))
        self.relate('connect','raised-tail','outline')
