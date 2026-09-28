"""Arrow thick 3 top right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8fad2e27-b997-5300-b5e0-5c6556df18a6'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick 3 top right_8fad2e27-b997-5300-b5e0-5c6556df18a6.svg'
AUTHOR = 'gpt-6'

class ArrowThick3TopRight(Solo48):
    icon_id = 'arrow-thick-3-top-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'right', 'arrows')

    def build(self):
        runs = [{'start': (6, 12), 'steps': [('L', 16, 12), ('L', 16, 24), ('L', 34, 6), ('L', 42, 14), ('L', 24, 32), ('L', 36, 32), ('L', 36, 42), ('L', 6, 42)], 'closed': True}]
        rotation = 2

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
