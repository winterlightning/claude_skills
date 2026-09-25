"""Raised calendar header; retained two binding posts and the rounded page.
Independent review variant of blank-calendar-container. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 41]. See container-fit-repair report for measured hosting results."""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '149fd072-7297-49b0-9f5d-d6b035d1779c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/calendar_149fd072-7297-49b0-9f5d-d6b035d1779c.svg'
AUTHOR = 'gpt-6'

class BlankCalendarContainer(Container64):
    icon_id = 'blank-calendar-container'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('blank', 'calendar', 'container')

    def build(self):
        rect(self, 'page', 2, 8, 62, 62, 4)
        self.add_line('header', (2, 20), (62, 20))
        self.relate('connect', 'header', 'page')
        for x in (18, 46):
            self.add_line(f'post-{x}', (x, 2), (x, 14))
            self.relate('connect', f'post-{x}', 'page')
