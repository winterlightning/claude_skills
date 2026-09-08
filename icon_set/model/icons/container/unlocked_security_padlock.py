"""An open padlock with a rounded body and a raised disengaged shackle.

Keyshape VRECT_XL: (4, 0, 60, 64); chosen for the reference silhouette.
Construction reference: Lucide lock-open: rounded body and open circular shackle. Original and atomic-debug inspected.
The shackle is intentionally open on the right, preserving the source asymmetry. No extra keyhole is added.
Hosting measured with compose.py: plus passes, heart does not pass, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class UnlockedSecurityPadlock(Container64):
    icon_id = 'unlocked-security-padlock'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('unlocked', 'security', 'padlock')

    def build(self) -> None:
        self.add_line('body-top', (12, 28), (52, 28))
        self.add_arc('body-ne', (52, 28), (58, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-right', (58, 34), (58, 56))
        self.add_arc('body-se', (58, 56), (52, 62), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-bottom', (52, 62), (12, 62))
        self.add_arc('body-sw', (12, 62), (6, 56), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-left', (6, 56), (6, 34))
        self.add_arc('body-nw', (6, 34), (12, 28), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('body', 'body-top', 'body-ne', 'body-right', 'body-se', 'body-bottom', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_line('shackle-left', (16, 28), (16, 18))
        self.add_arc('shackle-arch', (16, 18), (48, 18), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('shackle', 'shackle-left', 'shackle-arch', closed=False)
        self.relate("connect", 'shackle', 'body')
