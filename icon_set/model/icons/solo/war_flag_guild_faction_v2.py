"""War flag guild faction (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a677ecd4-20fe-4fb0-b00c-927e74c53dff'
SOURCE_PATH = 'icons-json/video-games/war flag guild faction_a677ecd4-20fe-4fb0-b00c-927e74c53dff.json'
AUTHOR = 'gpt-6'

class WarFlagGuildFactionVariant2(Solo48):
    icon_id = 'war-flag-guild-faction-v2'
    variant_of = 'war-flag-guild-faction'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('war', 'flag', 'guild', 'faction', 'video-games')

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
        self._circle('finial', 13, 9, 5)
        self.add_polyline('pole', (13, 14), (13, 18), (13, 34), (13, 44))
        self.add_polyline('flag', (13, 18), (40, 18), (34, 26), (40, 34), (13, 34))
        self.relate('connect', 'finial', 'pole')
        self.relate('connect', 'pole', 'flag')
