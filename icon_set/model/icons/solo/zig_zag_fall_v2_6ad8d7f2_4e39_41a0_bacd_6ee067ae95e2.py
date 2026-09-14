"""Zig zag fall (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ad8d7f2-4e39-41a0-bacd-6ee067ae95e2'
SOURCE_PATH = 'icons-json/arrows/zig zag fall_6ad8d7f2-4e39-41a0-bacd-6ee067ae95e2.json'
AUTHOR = 'gpt-6'

class ZigZagFallVariant2(Solo48):
    icon_id = 'zig-zag-fall-v2'
    variant_of = 'zig-zag-fall'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('zig', 'zag', 'fall', 'arrows')

    def build(self):
        runs = [{'start': (19, 4), 'steps': [('L', 19, 16), ('L', 40, 16), ('L', 8, 28), ('L', 27, 28), ('L', 27, 44)], 'closed': False}, {'start': (16, 39), 'steps': [('L', 27, 44)], 'closed': False}, {'start': (38, 39), 'steps': [('L', 27, 44)], 'closed': False}]
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
