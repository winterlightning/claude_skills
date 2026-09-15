"""Enlarge the matching wheels to radius eight and keep their baseline level. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '71cc0503-f8f3-434e-9c8e-e1524bb2498d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'
SOURCE_REFERENCES = (('71cc0503-f8f3-434e-9c8e-e1524bb2498d', 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'), ('7e9c7c99-94c3-4ae5-a57d-56a00190f3e6', 'pictographic-primitives/transportation/bicycle_7e9c7c99-94c3-4ae5-a57d-56a00190f3e6.svg'))
AUTHOR = 'gpt-6'

class BicycleAngledHandlebar(Solo48):
    icon_id = 'bicycle-angled-handlebar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'pedal', 'transport', 'two wheels', 'ride', 'city bike')

    def build(self):
        """Symbol plan: Enlarge the matching wheels to radius eight and keep their baseline level. Reference: Lucide bike: matched circular wheels."""

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
        for n, x in [('rear', 12), ('front', 36)]:
            oval(n, x, 32, 8, 8)
        poly('frame', (12, 24), (20, 16), (30, 16), (36, 24))
        poly('seat', (8, 8), (16, 8), (20, 16))
        join('seat', 'frame')
        poly('bar', (30, 16), (30, 11), (36, 8))
        join('bar', 'frame')
        join('rear', 'frame')
        join('front', 'frame')
