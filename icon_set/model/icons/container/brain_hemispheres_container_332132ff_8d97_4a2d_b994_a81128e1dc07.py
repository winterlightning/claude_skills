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
        self.add_line('fissure', (32, 15), (33, 52))
        self.add_arc('hemisphere--1-0', (32, 15), (16, 15), radius_x=8, radius_y=9, sweep=False)
        self.add_arc('hemisphere--1-1', (16, 15), (16, 37), radius_x=10, radius_y=11, sweep=False)
        self.add_arc('hemisphere--1-2', (16, 37), (21, 52), radius_x=8, sweep=False)
        self.add_arc('hemisphere--1-3', (21, 52), (33, 52), radius_x=6, sweep=False)
        self.add_arc('fold-top--1-0', (16, 15), (24, 23), radius_x=8, sweep=False)
        self.add_arc('fold-middle--1-0', (16, 37), (24, 35), radius_x=15, sweep=False)
        self.add_arc('fold-bottom--1-0', (21, 52), (24, 45), radius_x=9, sweep=False)
        self.add_arc('hemisphere-1-0', (32, 15), (48, 15), radius_x=8, radius_y=9)
        self.add_arc('hemisphere-1-1', (48, 15), (48, 37), radius_x=10, radius_y=11)
        self.add_arc('hemisphere-1-2', (48, 37), (43, 52), radius_x=8)
        self.add_arc('hemisphere-1-3', (43, 52), (33, 52), radius_x=6)
        self.add_arc('fold-top-1-0', (48, 15), (40, 23), radius_x=8)
        self.add_arc('fold-middle-1-0', (48, 37), (40, 35), radius_x=15)
        self.add_arc('fold-bottom-1-0', (43, 52), (40, 45), radius_x=9)
        self.add_contour('hemisphere--1', 'hemisphere--1-0', 'hemisphere--1-1', 'hemisphere--1-2', 'hemisphere--1-3')
        self.add_contour('fold-top--1', 'fold-top--1-0')
        self.add_contour('fold-middle--1', 'fold-middle--1-0')
        self.add_contour('fold-bottom--1', 'fold-bottom--1-0')
        self.add_contour('hemisphere-1', 'hemisphere-1-0', 'hemisphere-1-1', 'hemisphere-1-2', 'hemisphere-1-3')
        self.add_contour('fold-top-1', 'fold-top-1-0')
        self.add_contour('fold-middle-1', 'fold-middle-1-0')
        self.add_contour('fold-bottom-1', 'fold-bottom-1-0')
        self.relate('connect', 'fissure', 'hemisphere--1')
        self.relate('connect', 'hemisphere--1', 'fold-top--1')
        self.relate('connect', 'hemisphere--1', 'fold-middle--1')
        self.relate('connect', 'hemisphere--1', 'fold-bottom--1')
        self.relate('connect', 'fissure', 'hemisphere-1')
        self.relate('connect', 'hemisphere-1', 'fold-top-1')
        self.relate('connect', 'hemisphere-1', 'fold-middle-1')
        self.relate('connect', 'hemisphere-1', 'fold-bottom-1')
        self.relate('connect', 'hemisphere--1', 'hemisphere-1')
