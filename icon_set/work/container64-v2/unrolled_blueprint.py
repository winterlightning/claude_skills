"""Unrolled blueprint: a flat plan sheet whose right-hand edge is still rolled.

Reconstructed from the reference render. The reference is one continuous
ribbon of paper: a large flat sheet on the left, a seam where the flat part
ends, and a narrow rolled band on the right that caps over at the top and
tucks its free end back under at the bottom. Two drawn parts carry all of
that -- a closed `roll` loop and an open `sheet` C -- and they genuinely
share both of their ends, so the one contact is declared and scoped.

Three choices differ from the reference and are deliberate. The rolled band
is capped with a half-ellipse dome rather than the reference's quarter-round
corner: at 64 pixels a quarter-round reads as a rounded rectangle, while the
dome reads as a tube seen end-on, which is the whole point of the icon. The
band is 12 centerlines wide instead of the reference's 12.85-of-64, so its
interior keeps 8 units of white. And the reference's free end spirals back on
itself; that loop is smaller than one stroke here, so it is drawn as the
single fold the spiral resolves to -- one 45-degree tuck from the point
where the sheet's bottom edge ends up to the foot of the seam, 8 above it,
which is where the reference puts the same fold.

Five treatments of that free end were rendered at 64 and compared: a flat
run with a dive, a symmetric pill with no fold at all, a longer flat run,
this single diagonal, and a reference-faithful quarter-round top. The
diagonal won. The flat-plus-dive versions put a step in the bottom edge
that reads as a snag rather than a fold; the pill is clean but drops the
one cue that says the sheet is rolled and not merely sitting beside a tube;
and the quarter-round top turns the roll back into a rounded rectangle
corner.

Every junction is tangent-continuous except the two that are real paper
edges: the crest at (46,14) where the sheet's top edge branches off the
rolled seam, and the point at (54,58) where the free end turns back.

Hosting, remeasured for batch 17 with compose.py: plus, heart and check
all fail clearance. The seam at x=48 limits the usable interior. Earlier
hosting notes described an older seam position; the current measurements
are recorded in container_icons/work/batch_17_review/hosting.json.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (unrolled-blueprint SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class UnrolledBlueprintContainer(Container64):
    icon_id = 'unrolled-blueprint'
    keyshape = Keyshape.SQUARE
    aliases = ('unrolled-architectural-blueprint', 'blueprint', 'rolled-blueprint', 'architectural-blueprint', 'plan-drawing', 'partially-unrolled-paper-scroll')
    keywords = ('blueprint', 'roll', 'rolled', 'paper', 'document', 'plan', 'drawing', 'draft', 'architecture', 'scroll', 'sheet', 'schematic')

    def build(self) -> None:
        self.add_arc('roll-cap-a', (45, 14), (52, 6), radius_x=7, radius_y=8)
        self.add_arc('roll-cap-b', (52, 6), (58, 14), radius_x=8, radius_y=9)
        self.add_line('roll-right', (58, 14), (58, 47))
        self.add_arc('roll-curl', (58, 47), (53, 58), radius_x=5, radius_y=11)
        self.add_line('roll-tuck', (53, 58), (45, 50))
        self.add_line('roll-seam', (45, 50), (45, 14))
        self.add_line('sheet-top', (45, 14), (6, 14))
        self.add_line('sheet-left', (6, 14), (6, 58))
        self.add_line('sheet-bottom', (6, 58), (53, 58))
        self.add_contour('roll', 'roll-cap-a', 'roll-cap-b', 'roll-right', 'roll-curl', 'roll-tuck', 'roll-seam', closed=True)
        self.add_contour('sheet', 'sheet-top', 'sheet-left', 'sheet-bottom')
        self.relate('connect', 'sheet', 'roll')
