"""Lower steady (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '64a3ba6a-5e3e-4e12-a04c-b8e6de012c65'
SOURCE_PATH = 'pictographic-primitives/arrows/lower steady_64a3ba6a-5e3e-4e12-a04c-b8e6de012c65.svg'
AUTHOR = 'gpt-6'

class LowerSteady(Solo48):
    icon_id = 'lower-steady'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('lower', 'steady', 'arrows')

    def build(self):
        runs = [{'start': (6, 6), 'steps': [('L', 6, 35), ('A', 20, 35, 7, 7, False), ('L', 20, 26), ('A', 25, 21, 5, 5, True), ('L', 42, 21)], 'closed': False}, {'start': (37, 16), 'steps': [('L', 42, 21), ('L', 37, 26)], 'closed': False}]
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
