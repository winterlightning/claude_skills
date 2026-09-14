"""Curvy large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2c9e1073-40ac-499b-9c75-8c1fc2f12243'
SOURCE_PATH = 'icons-json/arrows/curvy large head_2c9e1073-40ac-499b-9c75-8c1fc2f12243.json'
AUTHOR = 'gpt-6'

class CurvyLargeHead(Solo48):
    icon_id = 'curvy-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (4, 30), 'steps': [('L', 4, 30), ('A', 24, 30, 10, 10, False), ('L', 24, 22), ('A', 32, 14, 8, 8, True), ('L', 44, 14)], 'closed': False}, {'start': (38, 8), 'steps': [('L', 44, 14), ('L', 38, 20)], 'closed': False}]
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
