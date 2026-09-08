"""Side-facing baby carriage with quarter-round hood and round wheels. Lucide bed informs body corners. Small axle omitted; paired supports attach the wheels to the body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '416f7dcc-429d-5dce-9524-9e881dd4a7b9'
SOURCE_PATH = 'pictographic-primitives/babies/baby care trolley_416f7dcc-429d-5dce-9524-9e881dd4a7b9.svg'
AUTHOR = 'gpt-6'


class BabyPram(Solo48):
    icon_id = 'baby-pram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('baby', 'pram', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: SQUARE; Side-facing baby carriage with quarter-round hood and round wheels. Lucide bed informs body corners. Small axle omitted; paired supports attach the wheels to the body.
        self.add_arc('hood', (2, 20), (20, 2), radius_x=18, radius_y=18, sweep=True)
        self.add_line('hood-back', (20, 2), (20, 20))
        self.add_contour('hood-shell', 'hood', 'hood-back', closed=False)
        self.add_line('rim', (2, 20), (36, 20))
        self.relate("connect", 'hood-shell', 'rim')
        self.add_line('body-left', (2, 20), (2, 24))
        self.add_arc('body-bottom-left', (2, 24), (12, 34), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-bottom', (12, 34), (26, 34))
        self.add_arc('body-bottom-right', (26, 34), (36, 24), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-right', (36, 24), (36, 20))
        self.add_contour('body', 'body-left', 'body-bottom-left', 'body-bottom', 'body-bottom-right', 'body-right', closed=False)
        self.relate("connect", 'body', 'rim')
        self.relate("connect", 'body', 'hood-shell')
        self.add_arc('handle-curve', (36, 20), (44, 10), radius_x=8, radius_y=10, sweep=True)
        self.add_line('handle-tip', (44, 10), (46, 10))
        self.add_contour('handle', 'handle-curve', 'handle-tip', closed=False)
        self.relate("connect", 'handle', 'rim')
        self.relate("connect", 'handle', 'body')
        self.add_arc('wheel-10-a', (10, 40), (10, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wheel-10-b', (10, 46), (10, 40), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wheel-10', 'wheel-10-a', 'wheel-10-b', closed=True)
        self.add_line('leg-10', (12, 34), (10, 40))
        self.relate("connect", 'leg-10', 'body')
        self.relate("connect", 'leg-10', 'wheel-10')
        self.add_arc('wheel-30-a', (30, 40), (30, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wheel-30-b', (30, 46), (30, 40), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wheel-30', 'wheel-30-a', 'wheel-30-b', closed=True)
        self.add_line('leg-30', (26, 34), (30, 40))
        self.relate("connect", 'leg-30', 'body')
        self.relate("connect", 'leg-30', 'wheel-30')
