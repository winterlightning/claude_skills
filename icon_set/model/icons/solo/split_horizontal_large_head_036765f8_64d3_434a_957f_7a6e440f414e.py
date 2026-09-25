"""Split horizontal large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '036765f8-64d3-434a-957f-7a6e440f414e'
SOURCE_PATH = 'pictographic-primitives/arrows/split horizontal large head_036765f8-64d3-434a-957f-7a6e440f414e.svg'
AUTHOR = 'gpt-6'

class SplitHorizontalLargeHead(Solo48):
    icon_id = 'split-horizontal-large-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('split', 'horizontal', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (8, 24), 'steps': [('L', 27, 24)], 'closed': False}, {'start': (27, 24), 'steps': [('A', 33, 18, 6, 6, False), ('L', 33, 4)], 'closed': False}, {'start': (27, 24), 'steps': [('A', 33, 30, 6, 6, True), ('L', 33, 44)], 'closed': False}, {'start': (26, 11), 'steps': [('L', 33, 4), ('L', 40, 11)], 'closed': False}, {'start': (26, 37), 'steps': [('L', 33, 44), ('L', 40, 37)], 'closed': False}]
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
