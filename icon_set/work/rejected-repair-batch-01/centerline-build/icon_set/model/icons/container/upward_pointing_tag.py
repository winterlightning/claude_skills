"""An upright tag enclosure with a peaked top and rounded bottom corners.

Keyshape VRECT_L: (8, 0, 56, 64); chosen for the reference silhouette.
Construction reference: Lucide house: axial roof and equal lower quarter-circle corners. Original and atomic-debug inspected.
No door is added: the source is an empty tag. Deliberate roof corners remain.
Hosting measured with compose.py: plus passes, heart passes, check does not pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class UpwardPointingTag(Container64):
    icon_id = 'upward-pointing-tag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('upward', 'pointing', 'tag')

    def build(self) -> None:
        self.add_line('roof-1', (10,22), (32,2))
        self.add_line('roof-2', (32,2), (54,22))
        self.add_line('roof-3', (54,22), (54,58))
        self.add_arc('se', (54, 58), (50, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('base', (50, 62), (14, 62))
        self.add_arc('sw', (14, 62), (10, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (10, 58), (10, 22))
        self.add_contour('outline', 'roof-1', 'roof-2', 'roof-3', 'se', 'base', 'sw', 'left', closed=True)
