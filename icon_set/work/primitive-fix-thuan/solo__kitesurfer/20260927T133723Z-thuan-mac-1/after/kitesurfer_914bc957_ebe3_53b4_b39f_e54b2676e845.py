"""Kitesurfer. Rider balances below a crescent kite joined by a tether; omit canopy divisions and doubled line.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: a coherent fabric silhouette; person-standing: sparse limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '914bc957-ebe3-53b4-b39f-e54b2676e845'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kitesurfer/20260927T133723Z-thuan-mac-1/reference/sport kitesurfing_914bc957-ebe3-53b4-b39f-e54b2676e845.svg'
AUTHOR = "gpt-6"


class Kitesurfer(Solo48):
    icon_id = 'kitesurfer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('kitesurfer',)

    def build(self) -> None:
        self.add_arc('canopy-outer', (6, 24), (30, 24), radius_x=12, radius_y=18, sweep=True)
        self.add_arc('canopy-inner', (30, 24), (6, 24), radius_x=12, radius_y=5, sweep=False)
        self.add_contour('kite', 'canopy-outer', 'canopy-inner', closed=True)
        self.add_line('tether-1', (30, 24), (39, 22))
        self.add_contour('tether', 'tether-1', closed=False)
        self.relate("connect", 'kite', 'tether')
        self.add_arc('head-top', (36, 11), (42, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (42, 11), (36, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (39, 22), (35, 32))
        self.add_line('rear-leg', (35, 32), (30, 42))
        self.add_line('front-leg', (35, 32), (40, 42))
        self.add_line('board', (26, 42), (42, 42))
        self.relate("connect", 'torso', 'tether')
        self.relate("connect", 'torso', 'rear-leg')
        self.relate("connect", 'torso', 'front-leg')
        self.relate("connect", 'board', 'rear-leg')
        self.relate("connect", 'board', 'front-leg')
        self.mark_human_figure('rider', head='head', torso='torso', torso_junction='start')
