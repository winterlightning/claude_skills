"""A detonator box with a T plunger and a wire looping to its right.

Keyshape SQUARE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide banknote: rounded rectangular enclosure. Original and atomic-debug inspected.
The plunger and looping wire carry identity; lettering is absent in the source. Right-hand wire creates deliberate asymmetry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class TntDetonatorPlunger(Container64):
    icon_id = 'tnt-detonator-plunger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('tnt', 'detonator', 'plunger')

    def build(self) -> None:
        self.add_line('box-top', (5, 20), (37, 20))
        self.add_arc('box-ne', (37, 20), (40, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-right', (40, 23), (40, 59))
        self.add_arc('box-se', (40, 59), (37, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-bottom', (37, 62), (5, 62))
        self.add_arc('box-sw', (5, 62), (2, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-left', (2, 59), (2, 23))
        self.add_arc('box-nw', (2, 23), (5, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('box', 'box-top', 'box-ne', 'box-right', 'box-se', 'box-bottom', 'box-sw', 'box-left', 'box-nw', closed=True)
        self.add_line('plunger', (21, 2), (21, 20))
        self.add_line('handle', (9, 2), (33, 2))
        self.relate("connect", 'handle', 'plunger')
        self.relate("connect", 'plunger', 'box')
        self.add_line('wire-out', (40, 52), (43, 52))
        self.add_arc('wire-up', (43, 52), (47, 48), radius_x=4, radius_y=4, sweep=False)
        self.add_line('wire-rise', (47, 48), (47, 38))
        self.add_arc('wire-crest', (47, 38), (55, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('wire-fall', (55, 38), (55, 58))
        self.add_arc('wire-foot', (55, 58), (59, 62), radius_x=4, radius_y=4, sweep=False)
        self.add_line('wire-end', (59, 62), (62, 62))
        self.add_contour('wire', 'wire-out', 'wire-up', 'wire-rise', 'wire-crest', 'wire-fall', 'wire-foot', 'wire-end', closed=False)
        self.relate("connect", 'wire', 'box')
