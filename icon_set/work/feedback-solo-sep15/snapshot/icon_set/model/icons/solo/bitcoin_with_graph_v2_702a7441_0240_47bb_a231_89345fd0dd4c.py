"""Center the arrowhead on the rising graph direction and use a coherent shared tip. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '702a7441-0240-47bb-a231-89345fd0dd4c'
SOURCE_PATH = 'pictographic-primitives/symbol/bitcoin with graph_702a7441-0240-47bb-a231-89345fd0dd4c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BitcoinWithGraphVariant2(Solo48):
    icon_id = 'bitcoin-with-graph-v2'
    variant_of = 'bitcoin-with-graph'
    variant_label = 'Center the arrowhead on the rising graph direction and use a coherent shared tip.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bitcoin', 'with', 'graph', 'symbol')

    def build(self):
        """Symbol plan: Center the arrowhead on the rising graph direction and use a coherent shared tip. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        poly('graph',(4,38),(16,17),(26,40),(42,8))
        poly('arrow',(32,13),(42,8),(44,19))
        join('arrow', 'graph')

