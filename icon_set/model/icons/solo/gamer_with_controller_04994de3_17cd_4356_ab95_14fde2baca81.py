"""Gamer with Controller. Front-facing symmetric gamer; rounded arms hold a central controller, omit miniature buttons.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04994de3-17cd-4356-ab95-14fde2baca81'
SOURCE_PATH = 'pictographic-primitives/recreation/gamer_04994de3-17cd-4356-ab95-14fde2baca81.svg'
AUTHOR = 'gpt-6'


class GamerWithController(Solo48):
    icon_id = 'gamer-with-controller'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('gamer', 'with', 'controller')

    def build(self) -> None:
        self.add_arc('head-top', (20, 8), (28, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-bottom', (28, 8), (20, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('shoulders-1', (8, 29), (8, 25))
        self.add_line('shoulders-2', (8, 25), (13, 21))
        self.add_line('shoulders-3', (13, 21), (35, 21))
        self.add_line('shoulders-4', (35, 21), (40, 25))
        self.add_line('shoulders-5', (40, 25), (40, 29))
        self.add_contour('shoulders', 'shoulders-1', 'shoulders-2', 'shoulders-3', 'shoulders-4', 'shoulders-5', closed=False)
        self.add_arc('arm-left', (8, 29), (16, 37), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('arm-right', (32, 37), (40, 29), radius_x=8, radius_y=8, sweep=False)
        self.relate("connect", 'shoulders', 'arm-left')
        self.relate("connect", 'shoulders', 'arm-right')
        self.add_line('controller0', (19, 29), (29, 29))
        self.add_arc('controller1', (29, 29), (32, 32), radius_x=3, radius_y=3, sweep=True)
        self.add_line('controller2', (32, 32), (32, 34))
        self.add_arc('controller3', (32, 34), (29, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_line('controller4', (29, 37), (19, 37))
        self.add_arc('controller5', (19, 37), (16, 34), radius_x=3, radius_y=3, sweep=True)
        self.add_line('controller6', (16, 34), (16, 32))
        self.add_arc('controller7', (16, 32), (19, 29), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('controller', 'controller0', 'controller1', 'controller2', 'controller3', 'controller4', 'controller5', 'controller6', 'controller7', closed=True)
        self.relate("connect", 'controller', 'arm-left')
        self.relate("connect", 'controller', 'arm-right')
        self.add_line('leg-left', (16, 37), (16, 44))
        self.add_line('leg-right', (32, 37), (32, 44))
        self.relate("connect", 'controller', 'leg-left')
        self.relate("connect", 'controller', 'leg-right')
