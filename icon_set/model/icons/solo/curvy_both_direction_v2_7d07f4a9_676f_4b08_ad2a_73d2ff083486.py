"""Curvy both direction (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d07f4a9-676f-4b08-ad2a-73d2ff083486'
SOURCE_PATH = 'icons-json/arrows/curvy both direction_7d07f4a9-676f-4b08-ad2a-73d2ff083486.json'
AUTHOR = 'gpt-6'

class CurvyBothDirectionVariant2(Solo48):
    icon_id = 'curvy-both-direction-v2'
    variant_of = 'curvy-both-direction'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'both', 'direction', 'arrows')

    def build(self):
        runs = [{'start': (44, 12), 'steps': [('L', 20, 12), ('A', 20, 24, 6, 6, False), ('L', 26, 24), ('A', 26, 36, 6, 6, True), ('L', 4, 36)], 'closed': False}, {'start': (40, 8), 'steps': [('L', 44, 12), ('L', 40, 16)], 'closed': False}, {'start': (8, 32), 'steps': [('L', 4, 36), ('L', 8, 40)], 'closed': False}]
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
