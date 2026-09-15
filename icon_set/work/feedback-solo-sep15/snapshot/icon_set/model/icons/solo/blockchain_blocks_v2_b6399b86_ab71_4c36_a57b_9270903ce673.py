"""Align both blocks in one left column with a centered connector and downward arrow on the right. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6399b86-ab71-4c36-a57b-9270903ce673'
SOURCE_PATH = 'pictographic-primitives/programing/amazon managed blockchain_b6399b86-ab71-4c36-a57b-9270903ce673.svg'
AUTHOR = 'gpt-6'

class BlockchainBlocksVariant2(Solo48):
    icon_id = 'blockchain-blocks-v2'
    variant_of = 'blockchain-blocks'
    variant_label = 'Align both blocks in one left column with a centered connector and downward arrow on the right.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/programming'
    aliases = ()
    keywords = ('blockchain', 'blocks', 'chain', 'ledger', 'link', 'sequence', 'crypto', 'arrow')

    def build(self):
        """Symbol plan: Align both blocks in one left column with a centered connector and downward arrow on the right. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('first', (6, 6), (20, 6), (20, 13), (20, 20), (6, 20), closed=True)
        poly('second', (6, 28), (20, 28), (20, 35), (20, 42), (6, 42), closed=True)
        poly('link', (20, 13), (36, 13), (36, 24), (36, 35), (20, 35))
        poly('arrow', (30, 18), (36, 24), (42, 18))
        join('link', 'first')
        join('link', 'second')
        join('arrow', 'link')
