"""Raised calendar header; retained two binding posts and the rounded page.
Independent review variant of blank-calendar-container. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 41]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (blank-calendar-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): reproportioned so a container symbol has more room (container-combination64 space check).
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '149fd072-7297-49b0-9f5d-d6b035d1779c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/calendar_149fd072-7297-49b0-9f5d-d6b035d1779c.svg'
AUTHOR = 'claude-opus-5-5'


class BlankCalendarContainer(Container64):
    icon_id = 'blank-calendar-container'
    keyshape = Keyshape.SQUARE
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('blank', 'calendar', 'container')

    def build(self) -> None:
        # Header band 12..20 (was 12..24) and posts 6..16 so the page below the header is 38 tall: room for a
        # symbol of about 28 with a 4 px gap.
        self.add_line('page-0', (10, 12), (54, 12))
        self.add_arc('page-1', (54, 12), (58, 16), radius_x=4)
        self.add_line('page-2', (58, 16), (58, 54))
        self.add_arc('page-3', (58, 54), (54, 58), radius_x=4)
        self.add_line('page-4', (54, 58), (10, 58))
        self.add_arc('page-5', (10, 58), (6, 54), radius_x=4)
        self.add_line('page-6', (6, 54), (6, 16))
        self.add_arc('page-7', (6, 16), (10, 12), radius_x=4)
        self.add_line('header', (6, 20), (58, 20))
        self.add_line('post-18', (20, 6), (20, 16))
        self.add_line('post-46', (44, 6), (44, 16))
        self.add_contour('page', 'page-0', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', 'page-6', 'page-7', closed=True)
        self.relate('connect', 'header', 'page')
        self.relate('connect', 'post-18', 'page')
        self.relate('connect', 'post-46', 'page')
