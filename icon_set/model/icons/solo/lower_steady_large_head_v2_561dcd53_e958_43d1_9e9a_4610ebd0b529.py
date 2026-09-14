"""Lower steady large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '561dcd53-e958-43d1-9e9a-4610ebd0b529'
SOURCE_PATH = 'icons-json/arrows/lower steady large head_561dcd53-e958-43d1-9e9a-4610ebd0b529.json'
AUTHOR = 'gpt-6'

class LowerSteadyLargeHeadVariant2(Solo48):
    icon_id = 'lower-steady-large-head-v2'
    variant_of = 'lower-steady-large-head'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('lower', 'steady', 'large', 'head', 'arrows')

    def build(self):
        runs = [{'start': (6, 6), 'steps': [('L', 6, 35), ('A', 20, 35, 7, 7, False), ('L', 20, 25), ('A', 26, 19, 6, 6, True), ('L', 42, 19)], 'closed': False}, {'start': (35, 12), 'steps': [('L', 42, 19), ('L', 35, 26)], 'closed': False}]
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
