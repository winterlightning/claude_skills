"""A tapered waste bin with a lid bar and raised rounded handle.

Keyshape SQUARE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide trash: open body attached to a lid bar and symmetric handle. Original and atomic-debug inspected.
Source taper retained with long sloping sides; no additional slats or marks.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (trash-can-with-lid SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class TrashCanWithLid(Container64):
    icon_id = 'trash-can-with-lid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('trash', 'can', 'with', 'lid')

    def build(self) -> None:
        self.add_line('lid', (6, 18), (58, 18))
        self.add_line('handle-left', (22, 18), (22, 10))
        self.add_arc('handle-nw', (22, 10), (26, 6), radius_x=4)
        self.add_line('handle-top', (26, 6), (38, 6))
        self.add_arc('handle-ne', (38, 6), (42, 10), radius_x=4)
        self.add_line('handle-right', (42, 10), (42, 18))
        self.add_line('body-left', (10, 18), (14, 50))
        self.add_arc('body-sw', (14, 50), (22, 58), radius_x=8, sweep=False)
        self.add_line('body-base', (22, 58), (42, 58))
        self.add_arc('body-se', (42, 58), (50, 50), radius_x=8, sweep=False)
        self.add_line('body-right', (50, 50), (54, 18))
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right')
        self.add_contour('body', 'body-left', 'body-sw', 'body-base', 'body-se', 'body-right')
        self.relate('connect', 'handle', 'lid')
        self.relate('connect', 'body', 'lid')
