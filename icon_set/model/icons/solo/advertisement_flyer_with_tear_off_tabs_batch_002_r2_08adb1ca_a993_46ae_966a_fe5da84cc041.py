"""Advertisement Flyer with Tear-Off Tabs -- batch-002 r2 generation.

Subject: a posted flyer whose lower edge is a row of tear-off tabs; two tabs
still hang below it and the third has already been taken.

Plan: the printed sheet is one closed contour with square paper corners. Its
lower edge is a series of three equal semicircular arches (chord 12,
radius 6), one per tab, as in the reference. Radii 6, 7 and 8 were rendered
side by side; 6 reads most like rounded tab tops and passes hole QA. The
remaining tabs are an open run below the first two arches. It shares the
sheet's left foot and the second cusp, and one divider drops from the first
cusp. The taken tab leaves only its arch. One text line keeps 9 from the
arched sheet contour.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: the reference photo box and second text line are dropped. The
header band above the arches is 18 tall, which leaves room for only one line
with 4-unit clearance. The tabs carry the identity.
Construction reference: no useful Lucide flyer match; Lucide file/sticky-note
sheet construction (square sheet with one text stroke) informed the body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path

SOURCE_ICON_ID = '08adb1ca-a993-46ae-966a-fe5da84cc041'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/flyer taken_08adb1ca-a993-46ae-966a-fe5da84cc041.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/flyer taken_08adb1ca-a993-46ae-966a-fe5da84cc041.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
TAB_TOP, TAB_WIDTH, TAB_COUNT, ARCH_RADIUS = 30, 12, 3, 6
KEPT_TABS = 2
TEXT_Y, TEXT_LEFT, TEXT_RIGHT = TOP + 9, LEFT + 9, RIGHT - 9


class AdvertisementFlyerWithTearOffTabsBatch002R2(Solo48):
    icon_id = 'advertisement-flyer-with-tear-off-tabs-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('tear-off-flyer', 'notice', 'poster')
    keywords = ('flyer', 'advert', 'advertisement', 'notice', 'tabs', 'tear', 'poster', 'marketing')

    def build(self) -> None:
        cusps = [(RIGHT - i * TAB_WIDTH, TAB_TOP) for i in range(TAB_COUNT + 1)]
        arches = [('A', end, ARCH_RADIUS, ARCH_RADIUS, False) for end in cusps[1:]]
        path(self, 'sheet', (LEFT, TAB_TOP),
             ('L', (LEFT, TOP)), ('L', (RIGHT, TOP)), ('L', cusps[0]),
             *arches, closed=True)
        kept_right = LEFT + KEPT_TABS * TAB_WIDTH
        foot_nodes = [(LEFT + i * TAB_WIDTH, BOTTOM) for i in range(1, KEPT_TABS)]
        path(self, 'tabs', (LEFT, TAB_TOP), ('L', (LEFT, BOTTOM)),
             *[('L', p) for p in foot_nodes], ('L', (kept_right, BOTTOM)),
             ('L', (kept_right, TAB_TOP)))
        self.relate('connect', 'sheet', 'tabs')
        for i, (x, _) in enumerate(foot_nodes):
            self.add_line(f'tab-divider-{i + 1}', (x, TAB_TOP), (x, BOTTOM))
            self.relate('connect', 'sheet', f'tab-divider-{i + 1}')
            self.relate('connect', 'tabs', f'tab-divider-{i + 1}')
        self.add_line('text-line', (TEXT_LEFT, TEXT_Y), (TEXT_RIGHT, TEXT_Y))
