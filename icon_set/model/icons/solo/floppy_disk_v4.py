"""Solid hub dot. Independent feedback revision; preserve source subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48975063-b353-533e-ada8-826f1f506264'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_48975063-b353-533e-ada8-826f1f506264.svg'
AUTHOR = 'gpt-6'

class FloppyDiskVariant4(Solo48):
    icon_id = 'floppy-disk-v4'
    variant_of = 'floppy-disk-v2'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'media', 'data')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        self.add_polyline('case', (6, 6), (42, 6), (42, 42), (6, 42), closed=True)
        for name, pts in [('shutter', [(15, 6), (15, 15), (33, 15), (33, 6)]), ('label', [(15, 42), (15, 33), (33, 33), (33, 42)])]:
            self.add_polyline(name, *pts)
            self.relate('connect', 'case', name)
        self.add_dot('hub', (24, 24))
