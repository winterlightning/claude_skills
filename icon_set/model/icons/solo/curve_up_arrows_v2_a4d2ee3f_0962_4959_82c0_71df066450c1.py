"""Curve up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4d2ee3f-0962-4959-82c0-71df066450c1'
SOURCE_PATH = 'icons-json/arrows/curve up_a4d2ee3f-0962-4959-82c0-71df066450c1.json'
AUTHOR = 'gpt-6'

class CurveUpArrowsVariant2(Solo48):
    icon_id = 'curve-up-arrows-v2'
    variant_of = 'curve-up-arrows'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'arrows')

    def build(self):
        runs = [{'start': (6, 42), 'steps': [('L', 15, 42), ('A', 22, 35, 7, 7, False), ('L', 22, 20), ('A', 31, 11, 9, 9, True), ('L', 42, 11)], 'closed': False}, {'start': (37, 6), 'steps': [('L', 42, 11), ('L', 37, 16)], 'closed': False}]
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
