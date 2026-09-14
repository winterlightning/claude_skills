"""Fall fast (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f263955d-755c-4538-a5ad-b9d1d495268d'
SOURCE_PATH = 'icons-json/arrows/fall fast_f263955d-755c-4538-a5ad-b9d1d495268d.json'
AUTHOR = 'gpt-6'

class FallFast(Solo48):
    icon_id = 'fall-fast'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('fall', 'fast', 'arrows')

    def build(self):
        runs = [{'start': (4, 8), 'steps': [('L', 4, 17), ('A', 11, 24, 7, 7, False), ('L', 31, 24), ('A', 38, 31, 7, 7, True), ('L', 38, 40)], 'closed': False}, {'start': (32, 34), 'steps': [('L', 38, 40), ('L', 44, 34)], 'closed': False}]
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
