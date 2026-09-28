"""Split vertical (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0426ebd5-cfe4-416c-bda2-27405f3e8a75'
SOURCE_PATH = 'pictographic-primitives/arrows/split vertical_0426ebd5-cfe4-416c-bda2-27405f3e8a75.svg'
AUTHOR = 'gpt-6'

class SplitVertical(Solo48):
    icon_id = 'split-vertical'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('split', 'vertical', 'arrows')

    def build(self):
        runs = [{'start': (24, 42), 'steps': [('L', 24, 22)], 'closed': False}, {'start': (24, 22), 'steps': [('A', 12, 10, 12, 12, False), ('L', 6, 10)], 'closed': False}, {'start': (24, 22), 'steps': [('A', 36, 10, 12, 12, True), ('L', 42, 10)], 'closed': False}, {'start': (10, 6), 'steps': [('L', 6, 10), ('L', 10, 14)], 'closed': False}, {'start': (38, 6), 'steps': [('L', 42, 10), ('L', 38, 14)], 'closed': False}]
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
