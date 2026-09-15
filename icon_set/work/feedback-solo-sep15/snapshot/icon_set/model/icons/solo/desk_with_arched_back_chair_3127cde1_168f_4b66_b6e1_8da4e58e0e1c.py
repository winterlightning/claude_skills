"""An arched-back chair in front of a desk with a right drawer pedestal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3127cde1-168f-4b66-b6e1-8da4e58e0e1c'
SOURCE_PATH = 'pictographic-primitives/office/chair table_3127cde1-168f-4b66-b6e1-8da4e58e0e1c.svg'
AUTHOR = 'gpt-6'


class DeskWithArchedBackChair(Solo48):
    icon_id = 'desk-with-arched-back-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ()
    keywords = ('desk', 'chair', 'furniture', 'office', 'workstation', 'seat')

    # Construction reference: Lucide monitor: joined rectangular construction; source sets chair arch and offset pedestal.
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
        # Plan: chair arch radius 8, split upright rails, seat and offset desk pedestal.
        # Centerline extremes (4,8)-(44,40). Deliberate pedestal asymmetry.
        axis=20
        arc('chair-arch',(axis-8,16),(axis+8,16),8)
        for side,x in [('left',axis-8),('right',axis+8)]:
            path(f'chair-{side}',(x,16),(x,24),(x,32),(x,40))
        line('seat',(12,32),(28,32))
        path('desk-top',(4,24),(12,24),(28,24),(36,24),(44,24))
        line('desk-leg',(4,24),(4,40))
        path('pedestal',(36,24),(36,40),(44,40),(44,32),(44,24))
        line('drawer',(36,32),(44,32))
        join_contacts()
