"""Navigation direction top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '71974ceb-9902-5835-a118-8a822fff467f'
SOURCE_PATH = 'icons-json/arrows/navigation direction top_71974ceb-9902-5835-a118-8a822fff467f.json'
AUTHOR = 'gpt-6'

class NavigationDirectionTopVariant2(Solo48):
    icon_id = 'navigation-direction-top-v2'
    variant_of = 'navigation-direction-top'
    variant_label = 'Clean geometry and balanced construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'direction', 'top', 'arrows')

    def build(self):
        runs = [{'start': (44, 27), 'steps': [('L', 44, 22), ('A', 16, 22, 14, 14, False), ('L', 16, 40)], 'closed': False}, {'start': (4, 31), 'steps': [('L', 16, 40), ('L', 28, 31)], 'closed': False}]
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
