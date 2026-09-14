"""Curve down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f627d99-cc89-49b7-ac11-0ac2532c6671'
SOURCE_PATH = 'icons-json/arrows/curve down_6f627d99-cc89-49b7-ac11-0ac2532c6671.json'
AUTHOR = 'gpt-6'

class CurveDown(Solo48):
    icon_id = 'curve-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'down', 'arrows')

    def build(self):
        runs = [{'start': (6, 6), 'steps': [('L', 6, 13), ('A', 12, 19, 6, 6, False), ('L', 31, 19), ('A', 37, 25, 6, 6, True), ('L', 37, 42)], 'closed': False}, {'start': (32, 37), 'steps': [('L', 37, 42), ('L', 42, 37)], 'closed': False}]
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
