"""Curvy both direction large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc11795e-9c7b-4522-995a-d02107828f81'
SOURCE_PATH = 'pictographic-primitives/arrows/curvy both direction large head_fc11795e-9c7b-4522-995a-d02107828f81.svg'
AUTHOR = 'gpt-6'

class CurvyBothDirectionLargeHead(Solo48):
    icon_id = 'curvy-both-direction-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('curvy', 'both', 'direction', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (42, 12), 'steps': [('L', 20, 12), ('A', 20, 24, 6, 6, False), ('L', 26, 24), ('A', 26, 36, 6, 6, True), ('L', 6, 36)], 'closed': False}, {'start': (36, 6), 'steps': [('L', 42, 12), ('L', 36, 18)], 'closed': False}, {'start': (12, 30), 'steps': [('L', 6, 36), ('L', 12, 42)], 'closed': False}]
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
