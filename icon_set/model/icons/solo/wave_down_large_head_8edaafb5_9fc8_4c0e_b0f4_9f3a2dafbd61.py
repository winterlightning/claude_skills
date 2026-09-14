"""Wave down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61'
SOURCE_PATH = 'icons-json/arrows/wave down large head_8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61.json'
AUTHOR = 'gpt-6'

class WaveDownLargeHead(Solo48):
    icon_id = 'wave-down-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'down', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (4, 8), 'steps': [('L', 7, 8), ('A', 13, 14, 6, 6, True), ('L', 13, 33), ('A', 27, 33, 7, 7, False), ('L', 27, 14), ('A', 39, 14, 6, 6, True), ('L', 39, 26)], 'closed': False}, {'start': (34, 21), 'steps': [('L', 39, 26), ('L', 44, 21)], 'closed': False}]
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
