"""A tapered waste bin with a lid bar and raised rounded handle.

Keyshape SQUARE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide trash: open body attached to a lid bar and symmetric handle. Original and atomic-debug inspected.
Source taper retained with long sloping sides; no additional slats or marks.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class TrashCanWithLid(Container64):
    icon_id = 'trash-can-with-lid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('trash', 'can', 'with', 'lid')

    def build(self) -> None:
        self.add_line('lid', (2, 14), (62, 14))
        self.add_line('handle-left', (18, 14), (18, 6))
        self.add_arc('handle-nw', (18, 6), (22, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-top', (22, 2), (42, 2))
        self.add_arc('handle-ne', (42, 2), (46, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-right', (46, 6), (46, 14))
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right', closed=False)
        self.relate("connect", 'handle', 'lid')
        self.add_line('body-left', (6, 14), (10, 54))
        self.add_arc('body-sw', (10, 54), (18, 62), radius_x=8, radius_y=8, sweep=False)
        self.add_line('body-base', (18, 62), (46, 62))
        self.add_arc('body-se', (46, 62), (54, 54), radius_x=8, radius_y=8, sweep=False)
        self.add_line('body-right', (54, 54), (58, 14))
        self.add_contour('body', 'body-left', 'body-sw', 'body-base', 'body-se', 'body-right', closed=False)
        self.relate("connect", 'body', 'lid')
