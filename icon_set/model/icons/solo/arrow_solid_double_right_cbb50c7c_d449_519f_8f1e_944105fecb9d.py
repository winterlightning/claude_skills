"""Arrow solid double right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbb50c7c-d449-519f-8f1e-944105fecb9d'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow solid double right_cbb50c7c-d449-519f-8f1e-944105fecb9d.svg'
AUTHOR = 'gpt-6'

class ArrowSolidDoubleRight(Solo48):
    icon_id = 'arrow-solid-double-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'right', 'arrows')

    def build(self):
        runs = [{'start': [44, 24], 'steps': [('L', 34, 40), ('L', 25, 40), ('L', 33, 24), ('L', 25, 8), ('L', 34, 8), ('L', 44, 24)], 'closed': True}, {'start': [4, 40], 'steps': [('L', 13, 40), ('L', 23, 24), ('L', 13, 8), ('L', 4, 8), ('L', 12, 24), ('L', 4, 40)], 'closed': True}]
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
