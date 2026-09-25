"""Steady and fall large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c78b2f2-0d07-40e5-88ac-1010b7292e8f'
SOURCE_PATH = 'pictographic-primitives/arrows/steady and fall large head_7c78b2f2-0d07-40e5-88ac-1010b7292e8f.svg'
AUTHOR = 'gpt-6'

class SteadyAndFallLargeHead(Solo48):
    icon_id = 'steady-and-fall-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('steady', 'and', 'fall', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (6, 6), 'steps': [('L', 6, 20), ('A', 12, 26, 6, 6, False), ('L', 24, 26)], 'closed': False}, {'start': (24, 26), 'steps': [('L', 42, 26)], 'closed': False}, {'start': (24, 26), 'steps': [('L', 24, 42)], 'closed': False}, {'start': (37, 21), 'steps': [('L', 42, 26), ('L', 37, 31)], 'closed': False}, {'start': (19, 37), 'steps': [('L', 24, 42), ('L', 29, 37)], 'closed': False}]
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
