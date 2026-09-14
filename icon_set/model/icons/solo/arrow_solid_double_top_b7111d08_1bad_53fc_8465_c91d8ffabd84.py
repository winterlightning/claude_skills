"""Arrow solid double top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7111d08-1bad-53fc-8465-c91d8ffabd84'
SOURCE_PATH = 'icons-json/arrows/arrow solid double top_b7111d08-1bad-53fc-8465-c91d8ffabd84.json'
AUTHOR = 'gpt-6'

class ArrowSolidDoubleTop(Solo48):
    icon_id = 'arrow-solid-double-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'top', 'arrows')

    def build(self):
        runs = [{'start': [24, 4], 'steps': [('L', 40, 14), ('L', 40, 23), ('L', 24, 15), ('L', 8, 23), ('L', 8, 14), ('L', 24, 4)], 'closed': True}, {'start': [24, 36], 'steps': [('L', 40, 44), ('L', 40, 35), ('L', 24, 25), ('L', 8, 35), ('L', 8, 44), ('L', 24, 36)], 'closed': True}]
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
