"""Concert stage with a microphone: a stand microphone standing on the stage
floor.
Review (meaning, "micro"): the earlier figure with a hook-like mic was
unreadable. The microphone is now the whole subject at full size: the Lucide capsule in
its U cradle on a stem that stands on a full-width stage floor line.
Keyshape SQUARE (6,6)-(42,42).
Symbol plan: capsule (r6 caps) cradled by a concentric r15 U (9 clear:
an exact 8 between arcs is not certifiable), stem joined at the U's bottom node, stage line split at the stem foot;
mirrored about x=24. The U bottom stays 8 above the floor.
Lucide construction: mic (rect x9 y2 w6 h13 rx3, U arc r7, stem) at 2x.
Omissions: the stage frame, bunting and singer figure; a stick figure plus a readable mic cannot both
keep 8-unit clearances in 36 units, and the review asked for the mic; the
floor line carries the stage.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "a37d9a40-16b7-4abd-b2f5-962b0ceb5244"
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__concert-stage-with-singer/20260926T125430Z-thuan-mac/reference/concert microphone_a37d9a40-16b7-4abd-b2f5-962b0ceb5244.svg'
AUTHOR = 'claude-opus-5-5'


class _Shapes:
    def circle(self, n, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r), (x - r, y)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f"{n}-{i}", a, b, radius_x=r)
        self.add_contour(n, *(f"{n}-{i}" for i in range(4)), closed=True)

    def lines(self, n, *pts, closed=False):
        """Plain add_line segments grouped in one contour (members joinable by relate)."""
        seq = list(pts) + ([pts[0]] if closed else [])
        ids = []
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            self.add_line(f"{n}-{i}", a, b)
            ids.append(f"{n}-{i}")
        self.add_contour(n, *ids, closed=closed)
        return ids

class ConcertStageWithSinger(_Shapes, Solo48):
    icon_id = 'concert-stage-with-singer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment/music'
    categories = ('entertainment',)
    aliases = ('concert microphone', 'stage microphone')
    keywords = ('concert', 'stage', 'microphone', 'mic', 'singer', 'music', 'performance', 'karaoke')

    def build(self):
        L, R, B = 6, 42, 42
        a = self.add_arc
        # Lucide mic at 2x: capsule x 18..30 with r6 caps, y 6..25
        a('cap-top', (18, 12), (30, 12), radius_x=6)
        self.add_line('cap-r', (30, 12), (30, 19))
        a('cap-bottom', (30, 19), (18, 19), radius_x=6)
        self.add_line('cap-l', (18, 19), (18, 12))
        self.add_contour('capsule', 'cap-top', 'cap-r', 'cap-bottom', 'cap-l', closed=True)
        # cradle concentric with the capsule's lower cap: r15 about (24,19)
        self.add_line('cradle-arm-l', (9, 15), (9, 19))
        a('cradle-l', (9, 19), (24, 34), radius_x=15, sweep=False)
        a('cradle-r', (24, 34), (39, 19), radius_x=15, sweep=False)
        self.add_line('cradle-arm-r', (39, 19), (39, 15))
        self.add_contour('cradle', 'cradle-arm-l', 'cradle-l', 'cradle-r', 'cradle-arm-r')
        self.add_line('stem', (24, 34), (24, B))
        self.lines('stage', (L, B), (24, B), (R, B))
        self.relate('connect', 'cradle', 'stem')
        self.relate('connect', 'stem', 'stage')
