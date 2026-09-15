"""Rising Trading Chart.

Plan: A rising zigzag with an arrow tip; three regular x positions own the trading bars. Bounds (6,6)-(42,42).
Construction references: Lucide chart-line: one coherent trend polyline.
Simplification: Dense trading marks reduced to three separated stems.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ecb064a-e1c1-5a45-89fb-d124161c89fd'
SOURCE_PATH = 'pictographic-primitives/business/trading graph_6ecb064a-e1c1-5a45-89fb-d124161c89fd.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


class RisingTradingChart(Solo48):
    icon_id = 'rising-trading-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('rising', 'trading', 'chart')

    def build(self):
        self.add_polyline('trend',(6,42),(18,30),(26,36),(42,20))
        self.add_polyline('arrow',(30,20),(42,20),(42,32))
        self.relate('connect','trend','arrow')
        for index,(x,top,bottom) in enumerate(((6,22,30),(18,6,16),(30,6,10))):
            self.add_line(f'trade-{index}',(x,top),(x,bottom))
