"""Steady and fall (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3ce2565-5b74-4cc9-91e5-8808ecc070e9'
SOURCE_PATH = 'pictographic-primitives/arrows/steady and fall_e3ce2565-5b74-4cc9-91e5-8808ecc070e9.svg'
AUTHOR = 'gpt-6'

class SteadyAndFall(Solo48):
    icon_id = 'steady-and-fall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'and', 'fall', 'arrows')

    def build(self):
        runs = [{'start': (4, 8), 'steps': [('L', 4, 20), ('A', 10, 26, 6, 6, False), ('L', 24, 26)], 'closed': False}, {'start': (24, 26), 'steps': [('L', 44, 26)], 'closed': False}, {'start': (24, 26), 'steps': [('L', 24, 40)], 'closed': False}, {'start': (39, 21), 'steps': [('L', 44, 26), ('L', 39, 31)], 'closed': False}, {'start': (19, 35), 'steps': [('L', 24, 40), ('L', 29, 35)], 'closed': False}]
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
