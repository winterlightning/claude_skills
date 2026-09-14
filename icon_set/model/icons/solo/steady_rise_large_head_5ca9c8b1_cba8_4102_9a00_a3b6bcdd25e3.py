"""Steady rise large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ca9c8b1-cba8-4102-9a00-a3b6bcdd25e3'
SOURCE_PATH = 'icons-json/arrows/steady rise large head_5ca9c8b1-cba8-4102-9a00-a3b6bcdd25e3.json'
AUTHOR = 'gpt-6'

class SteadyRiseLargeHead(Solo48):
    icon_id = 'steady-rise-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'rise', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (4, 40), 'steps': [('L', 10, 40), ('A', 16, 34, 6, 6, False), ('L', 16, 30), ('A', 22, 24, 6, 6, True), ('L', 28, 24), ('L', 44, 8)], 'closed': False}, {'start': (36, 8), 'steps': [('L', 44, 8), ('L', 44, 16)], 'closed': False}]
        rotation = 0

        def point(x, y):
            for _ in range(rotation):
                x, y = (48 - y, x)
            return (x, y)
        contacts = []
        for ri, run in enumerate(runs):
            start = point(*run['start'])
            previous = start
            members, nodes = ([], {start})
            for si, step in enumerate(run['steps']):
                end = point(step[1], step[2])
                if previous == end:
                    continue
                name = f'run-{ri}-{si}'
                if step[0] == 'L':
                    self.add_line(name, previous, end)
                else:
                    rx, ry = step[3:5]
                    if rotation % 2:
                        rx, ry = (ry, rx)
                    self.add_arc(name, previous, end, radius_x=rx, radius_y=ry, sweep=step[5])
                members.append(name)
                nodes.add(end)
                previous = end
            if run['closed'] and previous != start:
                name = f'run-{ri}-close'
                self.add_line(name, previous, start)
                members.append(name)
            contour = f'outline-{ri}'
            self.add_contour(contour, *members, closed=run['closed'])
            contacts.append((contour, nodes))
        for j, (a, points_a) in enumerate(contacts):
            for b, points_b in contacts[j + 1:]:
                if points_a & points_b:
                    self.relate('connect', a, b)
