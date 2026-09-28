"""Arrow solid double bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '583b3a6d-5f81-55fe-aa87-3d6afa1f2e44'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow solid double bottom_583b3a6d-5f81-55fe-aa87-3d6afa1f2e44.svg'
AUTHOR = 'gpt-6'

class ArrowSolidDoubleBottom(Solo48):
    icon_id = 'arrow-solid-double-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'bottom', 'arrows')

    def build(self):
        runs = [{'start': [24, 44], 'steps': [('L', 8, 34), ('L', 8, 25), ('L', 24, 33), ('L', 40, 25), ('L', 40, 34), ('L', 24, 44)], 'closed': True}, {'start': [8, 4], 'steps': [('L', 8, 13), ('L', 24, 23), ('L', 40, 13), ('L', 40, 4), ('L', 24, 12), ('L', 8, 4)], 'closed': True}]
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
