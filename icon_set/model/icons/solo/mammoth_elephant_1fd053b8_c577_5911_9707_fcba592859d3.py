"""Left-facing mammoth with domed forehead, one broad upturned tusk, and hooked trunk. Overlapping source ribbons simplified into coherent contours. No useful Lucide mammoth match; natural asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fd053b8-c577-5911-9707-fcba592859d3'
SOURCE_PATH = 'pictographic-primitives/animals/mammoth elephant_1fd053b8-c577-5911-9707-fcba592859d3.svg'
AUTHOR = 'gpt-6'


class MammothHead(Solo48):
    icon_id = 'mammoth-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('mammoth', 'head', 'animal')

    def build(self) -> None:
        # HRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_arc('crown', (25, 19), (34, 6), radius_x=9, radius_y=14, sweep=True)
        self.add_arc('head-back', (34, 6), (42, 17), radius_x=12, radius_y=12, sweep=True)
        self.add_line('neck', (42, 17), (42, 42))
        self.add_contour('head', 'crown', 'head-back', 'neck', closed=False)
        self.add_arc('tusk-low', (6, 24), (29, 27), radius_x=20, radius_y=13, sweep=False)
        self.add_line('tusk-root', (29, 27), (25, 19))
        self.add_arc('tusk-top', (25, 19), (6, 24), radius_x=19, radius_y=11, sweep=True)
        self.add_contour('tusk', 'tusk-low', 'tusk-root', 'tusk-top', closed=True)
        self.relate("connect", 'tusk', 'head')
        self.add_arc('trunk-outer', (29, 27), (18, 42), radius_x=18, radius_y=18, sweep=True)
        self.add_line('trunk-tip', (18, 42), (11, 38))
        self.add_arc('trunk-inner', (11, 38), (20, 30), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('trunk', 'trunk-outer', 'trunk-tip', 'trunk-inner', closed=False)
        self.relate("connect", 'trunk', 'tusk')
        self.add_dot('eye', (36, 19))
