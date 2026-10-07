"""Symmetrical Brain Hemispheres: independently authored container.

Construction plan: Two broad mirrored lobed hemispheres share one central fissure. Three attached folds per side; no detached head or body.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg. Lucide brain original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus, heart and check pass automated checks.
The continuous central fissure remains intrinsic furniture; composition may need
to mask that seam behind a child, as the source chip composition does.
SQUARE preserves the broad top-view silhouette. Lucide brain informed shared
seam and attached fold construction; the source owns the four-lobe silhouette.
Human bust references are not applicable to this isolated organ.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (brain-hemispheres-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn with an open centre (no full fissure, short folds) so a symbol of 24 fits (container-combination64).
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '332132ff-8d97-4a2d-b994-a81128e1dc07'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg'
AUTHOR = 'claude-opus-5-5'


class BrainHemispheresContainer(Container64):
    icon_id = 'brain-hemispheres-container'
    keyshape = Keyshape.SQUARE
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'hemispheres', 'container')

    def build(self) -> None:
        # Open-centre brain: each hemisphere is four lobes drawn as Bezier runs whose knots are the lobe tops
        # (tangent to the keyshape at 6/58) and the inward joins; the fissure is only the notches at (32,10) and
        # (32,56), and each join carries a short fold, so the middle stays empty for a symbol of 24 with a 4 px
        # gap. The right hemisphere mirrors the left about x = 32.
        lobes = [((32, 10), ((31, 7.5), (27, 6), (23, 6)), ((19, 6), (16, 7.5), (15, 10))),
                 ((15, 10), ((10, 10), (6, 14), (6, 19)), ((6, 24), (7, 28), (9, 30))),
                 ((9, 30), ((7, 33), (6, 37), (6, 41)), ((6, 46), (8, 49), (12, 51))),
                 ((12, 51), ((14, 56), (18, 58), (22, 58)), ((26, 58), (30, 57.5), (32, 56)))]
        mirror = lambda p: (64 - p[0], p[1])
        for side, f in (('left', lambda p: p), ('right', mirror)):
            for n, (start, *segments) in enumerate(lobes):
                self.add_bezier(f'{side}-{n}', f(start), *[tuple(f(p) for p in seg) for seg in segments])
            self.add_contour(side, *(f'{side}-{n}' for n in range(4)))
        for side, f in (('left', lambda p: p), ('right', mirror)):
            for name, a, b in (('top', (15, 10), (17, 13)), ('middle', (9, 30), (12, 30)), ('bottom', (12, 51), (14, 48))):
                self.add_line(f'fold-{name}-{side}', f(a), f(b))
                self.relate('connect', side, f'fold-{name}-{side}')
        self.relate('connect', 'left', 'right')
