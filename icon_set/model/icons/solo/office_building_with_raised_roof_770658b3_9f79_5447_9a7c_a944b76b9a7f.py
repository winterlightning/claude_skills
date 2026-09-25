"""An office building with a raised roof block, paired windows, and an arched entrance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '770658b3-9f79-5447-9a7c-a944b76b9a7f'
SOURCE_PATH = 'pictographic-primitives/office/building tall_770658b3-9f79-5447-9a7c-a944b76b9a7f.svg'
AUTHOR = 'gpt-6'


class OfficeBuildingWithRaisedRoof(Solo48):
    icon_id = 'office-building-with-raised-roof'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    aliases = ()
    keywords = ('building', 'office', 'roof', 'windows', 'architecture', 'workplace')

    # Construction reference: Lucide building: paired facade details and doorway.
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
        # Plan: symmetric roof block, overhanging ledge, facade and centered doorway.
        # Centerline extremes (8,4)-(40,44); axis x=24.
        axis=24
        path('roof-block',(16,12),(16,4),(32,4),(32,12))
        path('ledge',(8,12),(12,12),(16,12),(32,12),(36,12),(40,12))
        path('wall-left',(12,12),(12,44),(20,44))
        path('wall-right',(28,44),(36,44),(36,12))
        path('base-left',(8,44),(12,44))
        path('base-right',(36,44),(40,44))
        line('door-left',(20,44),(20,36))
        arc('door-arch',(20,36),(28,36),4)
        line('door-right',(28,36),(28,44))
        line('threshold',(20,44),(28,44))
        for col in range(2):
            line(f'window-{col}',(axis-4+col*8,22),(axis-4+col*8,24))
        join_contacts()
