"""Round (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09113b60-330a-48f7-bd5a-2a66b63402bc'
SOURCE_PATH = 'icons-json/arrows/round_09113b60-330a-48f7-bd5a-2a66b63402bc.json'
AUTHOR = 'gpt-6'

class Round(Solo48):
    icon_id = 'round'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('round', 'arrows')

    def build(self):
        runs = [{'start': (6, 24), 'steps': [('A', 24, 6, 18, 18, True), ('A', 42, 24, 18, 18, True), ('A', 24, 42, 18, 18, True), ('A', 10, 32, 14, 10, True)], 'closed': False}, {'start': (6, 36), 'steps': [('L', 10, 32), ('L', 14, 36)], 'closed': False}]
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
