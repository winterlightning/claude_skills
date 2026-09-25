'Charging battery: spacious terminal and a clear lightning stroke inside a balanced body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'


class BatteryChargingVertical(Solo48):
    icon_id = 'battery-charging-vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('battery', 'charging', 'power', 'energy', 'charge', 'electric', 'level', 'device')

    def build(self):
        # Plan: Lucide battery-charging: broad rounded housing, shared terminal nodes and an open lightning stroke with longer turns.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('body',(12,14), [('L',(16,14)),('L',(32,14)),('L',(36,14)),('A',(40,18),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,18)),('A',(12,14),4,4,True)],True)
        poly('terminal',(16,14),(16,4),(32,4),(32,14));join('terminal','body')
        poly('charge',(24,23),(17,29),(31,29),(24,35))
