"""End point triangle arrow 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50e2631e-8d3a-4df5-902e-0a6b04d1633d'
SOURCE_PATH = 'pictographic-primitives/arrows/end point triangle arrow 2_50e2631e-8d3a-4df5-902e-0a6b04d1633d.svg'
AUTHOR = 'gpt-6'

class EndPointTriangleArrow2(Solo48):
    icon_id = 'end-point-triangle-arrow-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('end', 'point', 'triangle', 'arrow', 'arrows')

    def build(self):
        runs = [{'start': (4, 24), 'steps': [('L', 29, 24)], 'closed': False}, {'start': (29, 24), 'steps': [('L', 29, 8), ('L', 44, 24), ('L', 29, 40), ('L', 29, 24)], 'closed': True}]
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
