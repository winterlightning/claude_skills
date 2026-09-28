"""A front-facing head-and-shoulder bust sits at the lower right of a large speech bubble. The bubble has rounded corners, a pointed downward tail and two short horizontal text lines.
Lucide message-square and user construction. Upper-left speech balloon and lower-right speaker retain the conversational scene. Both text rules omitted because they do not fit with legal clearance. Deliberate diagonal arrangement.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9720e290-377b-45be-b2a5-c6a9615a4ebe'
SOURCE_PATH = 'pictographic-primitives/work/work from home presentation_9720e290-377b-45be-b2a5-c6a9615a4ebe.svg'
AUTHOR = 'gpt-6'


class PersonSpeaking(Solo48):
    icon_id = 'person-speaking'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'speaking', 'speech', 'presentation', 'chat', 'conversation')

    def build(self) -> None:
        self.add_line('bubble-top', (10, 6), (22, 6))
        self.add_arc('corner-ne', (22, 6), (26, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bubble-right', (26, 10), (26, 14))
        self.add_arc('corner-se', (26, 14), (22, 18), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_polyline('tail', (22, 18), (20, 22), (14, 18), (10, 18), closed=False)
        self.add_arc('corner-sw', (10, 18), (6, 14), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bubble-left', (6, 14), (6, 10))
        self.add_arc('corner-nw', (6, 10), (10, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('bubble', 'bubble-top', 'corner-ne', 'bubble-right', 'corner-se', closed=False)
        self.relate("connect", 'bubble', 'tail')
        self.relate("connect", 'tail', 'corner-sw')
        self.relate("connect", 'corner-sw', 'bubble-left')
        self.relate("connect", 'bubble-left', 'corner-nw')
        self.relate("connect", 'corner-nw', 'bubble')
        self.add_arc('front-head-top', (30, 27), (38, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('front-head-bottom', (38, 27), (30, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('front-head', 'front-head-top', 'front-head-bottom', closed=True)
        self.add_arc('front-left', (26, 42), (34, 40), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('front-right', (34, 40), (42, 42), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('front-bust', 'front-left', 'front-right', closed=False)
