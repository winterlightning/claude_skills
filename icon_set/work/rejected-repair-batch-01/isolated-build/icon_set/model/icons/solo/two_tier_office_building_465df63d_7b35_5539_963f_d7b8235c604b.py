"""A stepped office building with paired windows and an arched entrance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '465df63d-7b35-5539-963f-d7b8235c604b'
SOURCE_PATH = 'pictographic-primitives/office/building double floor_465df63d-7b35-5539-963f-d7b8235c604b.svg'
AUTHOR = 'gpt-6'


class TwoTierOfficeBuilding(Solo48):
    icon_id = 'two-tier-office-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ()
    keywords = ('building', 'office', 'entrance', 'windows', 'architecture', 'workplace')

    # Construction reference: Lucide building: repeated window series and centered doorway.
    def build(self):
        # All contacts below are physical joints sharing exact endpoints.
        endpoints = {}
        def line(name, a, b):
            self.add_line(name, a, b)
            endpoints[name] = (a, b)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
            endpoints[name] = tuple(points)
        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
            endpoints[name] = (a, b)
        def join_contacts():
            names = list(endpoints)
            for i, a in enumerate(names):
                for b in names[i+1:]:
                    if set(endpoints[a]) & set(endpoints[b]):
                        self.relate("connect", a, b)
        # Plan: one stepped silhouette; a centered arched doorway; a 2x2 window series.
        # Centerline extremes (6,6)-(42,42). Symmetry axis x=24.
        axis = 24
        path('facade', (20,42),(6,42),(6,26),(12,26),(12,6),(36,6),(36,26),(42,26),(42,42),(28,42))
        line('door-left',(20,42),(20,34))
        arc('door-arch',(20,34),(28,34),4)
        line('door-right',(28,34),(28,42))
        line('threshold',(20,42),(28,42))
        for row in range(2):
            for col in range(2):
                self.add_dot(f'window-{row}-{col}',(axis-4+col*8,14+row*8))
        join_contacts()
