"""Curve rise (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3bc2c809-c730-49ec-8c35-8017ae225463'
SOURCE_PATH = 'icons-json/arrows/curve rise_3bc2c809-c730-49ec-8c35-8017ae225463.json'
AUTHOR = 'gpt-6'

class CurveRise(Solo48):
    icon_id = 'curve-rise'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'arrows')

    def build(self):
        runs = [{'start': (4, 23), 'steps': [('L', 4, 16), ('A', 20, 16, 8, 8, True), ('L', 20, 31), ('A', 38, 31, 9, 9, False), ('L', 38, 13)], 'closed': False}, {'start': (32, 20), 'steps': [('L', 38, 13), ('L', 44, 20)], 'closed': False}]
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
