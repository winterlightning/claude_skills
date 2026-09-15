"""A sloping drafting table with a small stool beneath it."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6919f03e-21f5-43ff-b08a-b79e0601e670'
SOURCE_PATH = 'pictographic-primitives/office/drawing board_6919f03e-21f5-43ff-b08a-b79e0601e670.svg'
AUTHOR = 'gpt-6'


class DraftingTableWithStool(Solo48):
    icon_id = 'drafting-table-with-stool'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ()
    keywords = ('drafting', 'table', 'stool', 'drawing', 'board', 'office')

    # Construction reference: No close Lucide subject match; monitor provides simple structural-support construction. Perspective makes the support attachments asymmetric.
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
        # Plan: tilted board trapezoid, asymmetric support attachment, centered stool.
        # Centerline extremes (4,8)-(44,40). Drop paper inset and stool rung for clearance.
        path('board',(12,8),(44,8),(40,16),(36,24),(8,24),(4,24),closed=True)
        line('support-left',(8,24),(8,40))
        line('support-right',(40,16),(40,40))
        line('foot-left',(4,40),(8,40))
        line('foot-right',(40,40),(44,40))
        path('stool',(16,40),(18,32),(30,32),(32,40))
        join_contacts()
