"""Rotation z axis (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b58c0737-d7c6-49b0-8338-9a42c1c26334'
SOURCE_PATH = 'icons-json/arrows/rotation z axis_b58c0737-d7c6-49b0-8338-9a42c1c26334.json'
AUTHOR = 'gpt-6'

class RotationZAxisVariant2(Solo48):
    icon_id = 'rotation-z-axis-v2'
    variant_of = 'rotation-z-axis'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rotation', 'z', 'axis', 'arrows')

    def build(self):
        runs = [{'start': (6, 24), 'steps': [('A', 24, 42, 18, 18, False), ('A', 42, 24, 18, 18, False), ('A', 24, 6, 18, 18, False), ('A', 8, 14, 16, 8, False)], 'closed': False}, {'start': (14, 14), 'steps': [('L', 8, 14), ('L', 8, 8)], 'closed': False}, {'start': (20, 24), 'steps': [('A', 28, 24, 4, 4, True), ('A', 20, 24, 4, 4, True)], 'closed': True}]
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
