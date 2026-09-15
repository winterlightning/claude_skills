"""Arrow dot left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ebf9acc-12df-4295-afb7-797830fc7f91'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'
AUTHOR = 'gpt-6'

class ArrowDotLeft(Solo48):
    icon_id = 'arrow-dot-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'left', 'arrows')

    def build(self):
        runs = [{'start': (16, 24), 'steps': [('L', 4, 24)], 'closed': False}, {'start': (4, 24), 'steps': [('L', 11, 40)], 'closed': False}, {'start': (4, 24), 'steps': [('L', 11, 8)], 'closed': False}, {'start': (24, 24), 'steps': [('L', 30, 24)], 'closed': False}, {'start': (38, 24), 'steps': [('L', 44, 24)], 'closed': False}]
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
