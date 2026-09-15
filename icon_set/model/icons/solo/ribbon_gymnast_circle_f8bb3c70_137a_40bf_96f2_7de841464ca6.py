# Repair: Lengthen the torso and lift the free hand clear of the dancing legs.
"""Ribbon gymnast: an open circular ribbon sweeps from the left hand past the head; its free right end stays separate from the right hand. Radius4 head (24,19), torso(24,31), exact4 gap. Preserve the dancing legs, with deliberate asymmetry from the source.

Ribbon gymnast: separate the open circular ribbon from the arms so it no longer reads as an umbrella. Radius4 head (24,16), torso junction (24,28), exact4 visible gap; preserve the spread arms and dancing legs of the source and full_body_ref.png.

Ribbon gymnast circle, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8bb3c70-137a-40bf-96f2-7de841464ca6'
SOURCE_PATH = 'pictographic-primitives/sports/ribbon person_f8bb3c70-137a-40bf-96f2-7de841464ca6.svg'
AUTHOR = 'gpt-6'

class RibbonGymnastCircle(Solo48):
    icon_id = 'ribbon-gymnast-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('ribbon', 'gymnast', 'circle')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        """Ribbon gymnast: an open circular ribbon sweeps from the left hand past the head; its free right end stays separate from the right hand. Radius4 head (24,19), torso(24,31), exact4 gap. Preserve the dancing legs, with deliberate asymmetry from the source."""
        self.ring('head', 24, 19, 4)
        self.add_line('torso', (24, 31), (24, 39))
        self.branches([('left-arm', [(24, 31), (12, 31), (6, 24)]), ('right-arm', [(24, 31), (36, 31)]), ('left-leg', [(24, 39), (18, 42)]), ('right-leg', [(24, 39), (34, 42)])])
        for p in ['left-arm-0', 'right-arm-0', 'left-leg-0', 'right-leg-0']:
            self.relate('connect', 'torso', p)
        self.add_arc('ribbon', (6, 24), (42, 24), radius_x=18)
        self.relate('connect', 'ribbon', 'left-arm-1')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
