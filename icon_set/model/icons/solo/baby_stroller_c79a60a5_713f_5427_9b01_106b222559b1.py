"""Side-facing baby carriage with quarter-round hood and round wheels. Lucide bed informs body corners. Small axle omitted; paired supports attach the wheels to the body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c79a60a5-713f-5427-9b01-106b222559b1'
SOURCE_PATH = 'pictographic-primitives/babies/baby care trolley_c79a60a5-713f-5427-9b01-106b222559b1.svg'
AUTHOR = 'gpt-6'


class BabyStroller(Solo48):
    icon_id = 'baby-stroller'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    aliases = ()
    keywords = ('baby', 'stroller', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Centerline keyshape: SQUARE; Side-facing baby carriage with quarter-round hood and round wheels. Lucide bed informs body corners. Small axle omitted; paired supports attach the wheels to the body.
        self.add_arc('hood', (42, 20), (28, 6), radius_x=14, radius_y=14, sweep=False)
        self.add_line('hood-back', (28, 6), (28, 20))
        self.add_contour('hood-shell', 'hood', 'hood-back', closed=False)
        self.add_line('rim', (42, 20), (12, 20))
        self.relate("connect", 'hood-shell', 'rim')
        self.add_line('body-left', (42, 20), (42, 24))
        self.add_arc('body-bottom-left', (42, 24), (36, 34), radius_x=6, radius_y=10, sweep=True)
        self.add_line('body-bottom', (36, 34), (22, 34))
        self.add_arc('body-bottom-right', (22, 34), (12, 24), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-right', (12, 24), (12, 20))
        self.add_contour('body', 'body-left', 'body-bottom-left', 'body-bottom', 'body-bottom-right', 'body-right', closed=False)
        self.relate("connect", 'body', 'rim')
        self.relate("connect", 'body', 'hood-shell')
        self.add_arc('handle-curve', (12, 20), (6, 10), radius_x=6, radius_y=10, sweep=False)
        self.add_line('handle-tip', (6, 10), (6, 10))
        self.add_contour('handle', 'handle-curve', 'handle-tip', closed=False)
        self.relate("connect", 'handle', 'rim')
        self.relate("connect", 'handle', 'body')
        self.add_arc('wheel-10-a', (38, 40), (38, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wheel-10-b', (38, 42), (38, 40), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wheel-10', 'wheel-10-a', 'wheel-10-b', closed=True)
        self.add_line('leg-10', (36, 34), (38, 40))
        self.relate("connect", 'leg-10', 'body')
        self.relate("connect", 'leg-10', 'wheel-10')
        self.add_arc('wheel-30-a', (18, 40), (18, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wheel-30-b', (18, 42), (18, 40), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wheel-30', 'wheel-30-a', 'wheel-30-b', closed=True)
        self.add_line('leg-30', (22, 34), (18, 40))
        self.relate("connect", 'leg-30', 'body')
        self.relate("connect", 'leg-30', 'wheel-30')
