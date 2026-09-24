"""video edit split: repaired SOLO48 composition.
Plan: Repeated rounded panel corners and a coherent triangular marker.
Keyshape: SQUARE balances panels with the top split marker.
Reduction: Two rather than three cut dashes; marker enlarged and cut dashes lowered.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.profiles import Profile

SOURCE_ICON_ID = '2dcda804-d52b-4984-9a4e-b6abdfa0030f'
SOURCE_PATH = 'pictographic-primitives/video/video edit split_2dcda804-d52b-4984-9a4e-b6abdfa0030f.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'monitor, square-play'

class Drawing(Solo48):
    icon_id = 'video-edit-split'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'edit', 'split')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        for (name, l, r) in [('left', 6, 16), ('right', 32, 42)]:
            self.rounded(name, l, 22, r, 42, 3, breaks={2: [(r, 34)], 6: [(l, 34)]})
            self.add_line(name + '-footer', (l, 34), (r, 34))
            self.relate('connect', name + '-footer', name)
        self.add_polyline('marker', (16, 6), (32, 6), (24, 18), closed=True)
        for (i, y) in enumerate((26, 38)):
            self.add_line(f'cut-{i}', (24, y), (24, y + 4))

    def rounded(self, name, l, t, r, b, rad, breaks=None):
        pts = [(l + rad, t), (r - rad, t), (r, t + rad), (r, b - rad), (r - rad, b), (l + rad, b), (l, b - rad), (l, t + rad), (l + rad, t)]
        members = []
        breaks = breaks or {}
        for (i, (a, z)) in enumerate(zip(pts, pts[1:])):
            if i % 2:
                m = f'{name}-{i}'
                self.add_arc(m, a, z, radius_x=rad)
                members.append(m)
            else:
                nodes = [a] + breaks.get(i, []) + [z]
                for (j, (start, end)) in enumerate(zip(nodes, nodes[1:])):
                    if start == end:
                        continue
                    m = f'{name}-{i}-{j}'
                    self.add_line(m, start, end)
                    members.append(m)
        self.add_contour(name, *members, closed=True)
