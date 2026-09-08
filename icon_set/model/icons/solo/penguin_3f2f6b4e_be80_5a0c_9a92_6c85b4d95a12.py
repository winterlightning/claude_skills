"""Left-facing upright penguin with a domed head and curved flipper. Lucide bird informs head and wing arcs. Ground line omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12'
SOURCE_PATH = 'pictographic-primitives/animals/penguin_3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12.svg'
AUTHOR = 'gpt-6'


class StandingPenguin(Solo48):
    icon_id = 'standing-penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('penguin', 'standing', 'bird', 'antarctic', 'flipper', 'beak', 'ice', 'simple')

    def build(self) -> None:
        self.add_line('outline-1', (8, 18), (12, 14))
        self.add_arc('outline-2', (12, 14), (24, 2), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('outline-3', (24, 2), (36, 16), radius_x=12, radius_y=14, sweep=True)
        self.add_line('outline-4', (36, 16), (36, 38))
        self.add_arc('outline-5', (36, 38), (40, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_line('outline-6', (40, 46), (22, 46))
        self.add_arc('outline-7', (22, 46), (16, 38), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('outline-8', (16, 38), (18, 18), radius_x=24, radius_y=20, sweep=True)
        self.add_line('outline-9', (18, 18), (8, 18))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', closed=True)
        self.add_arc('flipper-1', (24, 24), (28, 34), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('flipper', 'flipper-1', closed=False)
        self.add_dot('eye', (24, 12))
