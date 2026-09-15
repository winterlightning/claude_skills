"""Lucide user-round: repeated heads and shoulder arcs. Three people and notched banner retained; folded second layer omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c276e80-fe1b-4163-a5a7-8cb3946d5876'
SOURCE_PATH = 'pictographic-primitives/school-learning/election campaign 2_9c276e80-fe1b-4163-a5a7-8cb3946d5876.svg'
AUTHOR = 'gpt-6'

class CampaignRally(Solo48):
    icon_id = 'campaign-rally'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'society/elections'
    aliases = ()
    keywords = ('rally', 'campaign', 'people', 'banner', 'election', 'crowd')

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
        self.add_polyline('banner', (6,16),(6,6),(42,6),(37,11),(42,16),(6,16))
        for i, x in enumerate((10, 24, 38)):
            self.bust('person-' + str(i), x, 27, r=3, width=7)
        self.relate('connect', 'person-0-shoulders', 'person-1-shoulders')
        self.relate('connect', 'person-1-shoulders', 'person-2-shoulders')
