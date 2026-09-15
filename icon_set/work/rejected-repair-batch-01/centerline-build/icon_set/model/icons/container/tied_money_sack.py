"""A full rounded sack with a flared mouth and a tied neck.

Keyshape VRECT_XL: (4, 0, 60, 64); chosen for the reference silhouette.
Construction reference: Lucide circle: coherent arc construction; no useful local sack match. Original and atomic-debug inspected.
Mirrored body uses circular shoulders tangent to the elliptical base. Two leftward tie ends preserve the source asymmetry.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class TiedMoneySack(Container64):
    icon_id = 'tied-money-sack'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('tied', 'money', 'sack')

    def build(self) -> None:
        self.add_arc('body-left', (22, 18), (6, 50), radius_x=40, radius_y=40, sweep=False)
        self.add_arc('body-sw', (6, 50), (32, 62), radius_x=26, radius_y=12, sweep=False)
        self.add_arc('body-se', (32, 62), (58, 50), radius_x=26, radius_y=12, sweep=False)
        self.add_arc('body-right', (58, 50), (42, 18), radius_x=40, radius_y=40, sweep=False)
        self.add_line('neck', (42, 18), (22, 18))
        self.add_contour('body', 'body-left', 'body-sw', 'body-se', 'body-right', 'neck', closed=True)
        self.add_line('mouth-left', (22, 18), (18, 4))
        self.add_arc('mouth-top', (18, 4), (46, 4), radius_x=14, radius_y=2, sweep=True)
        self.add_line('mouth-right', (46, 4), (42, 18))
        self.add_contour('mouth', 'mouth-left', 'mouth-top', 'mouth-right', closed=False)
        self.relate("connect", 'body', 'mouth')
        self.add_line('tie-top', (22, 18), (10, 14))
        self.add_line('tie-bottom', (22, 18), (8, 25))
        self.relate("connect", 'tie-top', 'body')
        self.relate("connect", 'tie-top', 'mouth')
        self.relate("connect", 'tie-bottom', 'body')
        self.relate("connect", 'tie-bottom', 'mouth')
        self.relate("connect", 'tie-top', 'tie-bottom')
