"""Lucide user-round: equal candidate busts. Three unequal bars are single strokes to preserve spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ac79d01-139c-4591-8b68-f54402dc9829'
SOURCE_PATH = 'pictographic-primitives/school-learning/election candidate poll_1ac79d01-139c-4591-8b68-f54402dc9829.svg'
AUTHOR = 'gpt-6'

class CandidatePollChart(Solo48):
    icon_id = 'candidate-poll-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'school-learning'
    aliases = ()
    keywords = ('poll', 'chart', 'candidate', 'election', 'people', 'comparison')

    def circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        ids = []
        for j, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(j)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name + '-head', x, y, r)
        self.add_arc(name + '-sl', (max(6, x - width), y + 15), (x, y + r + 8), radius_x=min(width, x - 6), radius_y=4)
        self.add_arc(name + '-sr', (x, y + r + 8), (min(42, x + width), y + 15), radius_x=min(width, 42 - x), radius_y=4)
        self.add_contour(name + '-shoulders', name + '-sl', name + '-sr')

    def build(self) -> None:
        """Open the three equal head rings and give every person exactly4 ink units to its shoulder apex, following full_body_ref.png."""
        self.add_polyline('baseline', (6,16),(10,16),(24,16),(38,16),(42,16))
        for i, (x, y) in enumerate(((10,12),(24,6),(38,10))):
            self.add_line('bar-' + str(i), (x, y), (x,16))
            self.relate('connect', 'baseline', 'bar-' + str(i))
            self.bust('candidate-' + str(i), x, 27, r=3, width=7)
        self.relate('connect', 'candidate-0-shoulders', 'candidate-1-shoulders')
        self.relate('connect', 'candidate-1-shoulders', 'candidate-2-shoulders')
