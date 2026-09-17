"""Simple Square Calendar Organizer: independently authored container.

Construction plan: Rounded page with two equal binding posts and a header rule; shared x positions.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/calendar_149fd072-7297-49b0-9f5d-d6b035d1779c.svg. Lucide calendar original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '149fd072-7297-49b0-9f5d-d6b035d1779c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/calendar_149fd072-7297-49b0-9f5d-d6b035d1779c.svg'
AUTHOR = 'gpt-6'


class BlankCalendarContainer(Container64):
    icon_id = 'blank-calendar-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('blank', 'calendar', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'page',2,10,62,62,4)
        line('header',(2,26),(62,26));join('header','page')
        for x in (18,46):
         line(f'post-{x}',(x,2),(x,16));join(f'post-{x}','page')
