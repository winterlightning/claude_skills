"""Caged Transport Trailer.

Symbol plan: Cage with repeated vertical bars; single wheel interrupts bottom chassis, hitch extends left. Visible (2,6)-(46,42). Omit extra lower panel line.
Construction references: Lucide bus: cage/window uprights and wheel interrupts chassis.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '690885d5-4763-4595-85c9-2acbb6772ae8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/prisoner transport_690885d5-4763-4595-85c9-2acbb6772ae8.svg'
AUTHOR = 'gpt-6'


class CagedTransportTrailer(Solo48):
    icon_id = 'caged-transport-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('caged', 'transport', 'trailer')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('cage',(24,34),[(16,34),((12,30),4,4,True),(12,12),((16,8),4,4,True),(24,8),(34,8),(40,8),((44,12),4,4,True),(44,30),((40,34),4,4,True),(36,34)])
        circle('wheel',30,34,6)
        self.relate('connect','wheel','cage')
        self.add_line('hitch',(4,30),(12,30))
        self.relate('connect','hitch','cage')
        for j,x in enumerate((24,34)):
         self.add_line(f'bar-{j}',(x,8),(x,20))
         self.relate('connect',f'bar-{j}','cage')
