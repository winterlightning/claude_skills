"""Wave down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c14d211-460c-47be-9d40-aba34bbb7672'
SOURCE_PATH = 'pictographic-primitives/arrows/wave down_8c14d211-460c-47be-9d40-aba34bbb7672.svg'
AUTHOR = 'gpt-6'

class WaveDown(Solo48):
    icon_id = 'wave-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('wave', 'down', 'arrows')

    def build(self):
        runs = [{'start': (4, 40), 'steps': [('L', 4, 14), ('A', 16, 14, 6, 6, True), ('L', 16, 34), ('A', 28, 34, 6, 6, False), ('L', 28, 14), ('A', 40, 14, 6, 6, True), ('L', 40, 27)], 'closed': False}, {'start': (36, 23), 'steps': [('L', 40, 27), ('L', 44, 23)], 'closed': False}]
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
