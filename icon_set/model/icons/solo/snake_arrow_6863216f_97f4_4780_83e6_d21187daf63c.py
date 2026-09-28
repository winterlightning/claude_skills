"""Snake arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6863216f-97f4-4780-83e6-d21187daf63c'
SOURCE_PATH = 'pictographic-primitives/arrows/snake arrow_6863216f-97f4-4780-83e6-d21187daf63c.svg'
AUTHOR = 'gpt-6'

class SnakeArrow(Solo48):
    icon_id = 'snake-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('snake', 'arrow', 'arrows')

    def build(self):
        runs = [{'start': (22, 6), 'steps': [('L', 22, 12), ('A', 24, 14, 2, 2, False), ('L', 38, 14), ('A', 38, 22, 4, 4, True), ('L', 11, 22), ('A', 11, 32, 5, 5, False), ('L', 22, 32), ('A', 25, 35, 3, 3, True), ('L', 25, 42)], 'closed': False}, {'start': (20, 37), 'steps': [('L', 25, 42), ('L', 30, 37)], 'closed': False}]
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
