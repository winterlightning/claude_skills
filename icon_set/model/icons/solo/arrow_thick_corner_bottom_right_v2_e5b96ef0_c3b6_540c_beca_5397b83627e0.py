"""Arrow thick corner bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5b96ef0-c3b6-540c-beca-5397b83627e0'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner bottom right_e5b96ef0-c3b6-540c-beca-5397b83627e0.json'
AUTHOR = 'gpt-6'

class ArrowThickCornerBottomRightVariant2(Solo48):
    icon_id = 'arrow-thick-corner-bottom-right-v2'
    variant_of = 'arrow-thick-corner-bottom-right'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'right', 'arrows')

    def build(self):
        runs = [{'start': (42, 16), 'steps': [('L', 34, 24), ('L', 16, 6), ('L', 6, 16), ('L', 24, 34), ('L', 16, 42), ('L', 42, 42), ('L', 42, 16)], 'closed': True}]
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
