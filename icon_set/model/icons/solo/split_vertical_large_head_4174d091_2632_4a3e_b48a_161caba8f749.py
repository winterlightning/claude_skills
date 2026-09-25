"""Split vertical large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4174d091-2632-4a3e-b48a-161caba8f749'
SOURCE_PATH = 'pictographic-primitives/arrows/split vertical large head_4174d091-2632-4a3e-b48a-161caba8f749.svg'
AUTHOR = 'gpt-6'

class SplitVerticalLargeHead(Solo48):
    icon_id = 'split-vertical-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('split', 'vertical', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (24, 8), 'steps': [('L', 24, 26)], 'closed': False}, {'start': (24, 40), 'steps': [('L', 24, 26)], 'closed': False}, {'start': (24, 26), 'steps': [('A', 14, 16, 10, 10, False), ('L', 4, 16)], 'closed': False}, {'start': (24, 26), 'steps': [('A', 34, 16, 10, 10, True), ('L', 44, 16)], 'closed': False}, {'start': (9, 11), 'steps': [('L', 4, 16), ('L', 9, 21)], 'closed': False}, {'start': (39, 11), 'steps': [('L', 44, 16), ('L', 39, 21)], 'closed': False}]
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
