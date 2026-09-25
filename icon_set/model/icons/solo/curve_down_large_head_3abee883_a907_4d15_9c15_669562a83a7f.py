"""Curve down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3abee883-a907-4d15-9c15-669562a83a7f'
SOURCE_PATH = 'pictographic-primitives/arrows/curve down large head_3abee883-a907-4d15-9c15-669562a83a7f.svg'
AUTHOR = 'gpt-6'

class CurveDownLargeHead(Solo48):
    icon_id = 'curve-down-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('curve', 'down', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (6, 6), 'steps': [('L', 6, 13), ('A', 12, 19, 6, 6, False), ('L', 26, 19), ('A', 34, 27, 8, 8, True), ('L', 34, 42)], 'closed': False}, {'start': (26, 34), 'steps': [('L', 34, 42), ('L', 42, 34)], 'closed': False}]
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
