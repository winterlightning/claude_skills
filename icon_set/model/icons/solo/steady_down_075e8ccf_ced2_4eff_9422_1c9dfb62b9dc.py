"""Steady down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '075e8ccf-ced2-4eff-9422-1c9dfb62b9dc'
SOURCE_PATH = 'pictographic-primitives/arrows/steady down_075e8ccf-ced2-4eff-9422-1c9dfb62b9dc.svg'
AUTHOR = 'gpt-6'

class SteadyDown(Solo48):
    icon_id = 'steady-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('steady', 'down', 'arrows')

    def build(self):
        runs = [{'start': (8, 22), 'steps': [('L', 22, 22)], 'closed': False}, {'start': (22, 22), 'steps': [('L', 22, 13), ('A', 40, 13, 9, 9, True), ('A', 31, 22, 9, 9, True), ('L', 22, 22)], 'closed': True}, {'start': (22, 22), 'steps': [('L', 22, 44)], 'closed': False}, {'start': (17, 39), 'steps': [('L', 22, 44), ('L', 27, 39)], 'closed': False}]
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
