"""A corded capsule mouse with a horizontal button seam and central divider.

VRECT_M extremes (11,2)-(37,46) fit a tall capsule plus cord. Lucide mouse
informs tangent capsule arcs; source button split and cable remain.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af38802b-7208-5060-b370-9b6f0871299d'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/mouse_af38802b-7208-5060-b370-9b6f0871299d.svg'


class CordedComputerMouse(Solo48):
    icon_id = 'corded-computer-mouse'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'corded', 'wired', 'cable', 'click', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('body-ne', (24, 10), (37, 23), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_line('body-right', (37, 23), (37, 33))
        self.add_arc('body-se', (37, 33), (24, 46), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('body-sw', (24, 46), (11, 33), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_line('body-left', (11, 33), (11, 23))
        self.add_arc('body-nw', (11, 23), (24, 10), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('body', 'body-ne', 'body-right', 'body-se', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_line('cord', (24, 2), (24, 10))
        self.relate('connect', 'body', 'cord')
        self.add_polyline('buttons', (11, 23), (24, 23), (37, 23), closed=False)
        self.relate('connect', 'body', 'buttons')
        self.add_line('divider', (24, 16), (24, 23))
        self.relate('connect', 'buttons', 'divider')
