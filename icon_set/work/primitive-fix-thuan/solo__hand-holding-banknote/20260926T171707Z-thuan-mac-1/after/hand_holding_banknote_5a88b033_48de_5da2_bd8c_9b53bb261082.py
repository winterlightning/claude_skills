from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5a88b033-48de-5da2-bd8c-9b53bb261082'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-banknote/20260926T171707Z-thuan-mac-1/reference/cash payment bills_5a88b033-48de-5da2-bd8c-9b53bb261082.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


class Drawing(Solo48):
    icon_id = 'hand-holding-banknote'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases = ()
    keywords = ('cash', 'banknote', 'money', 'hand', 'payment', 'bill', 'holding', 'currency')

    def build(self) -> None:
        # Banknote (16..36 x 4..24) held in a rounded fist; the fist's r10 knuckle curve
        # (centre (30,34)) takes the note's lower-right corner at the lattice point (36,26).
        self.add_line('note-top', (16, 4), (36, 4))
        self.add_line('note-right', (36, 4), (36, 26))
        self.add_line('note-left-upper', (16, 4), (16, 20))
        self.add_line('note-left-lower', (16, 20), (16, 24))
        self.add_line('note-bottom', (16, 24), (30, 24))
        for a, b in (('note-top', 'note-right'), ('note-top', 'note-left-upper'), ('note-left-upper', 'note-left-lower'),
                     ('note-left-lower', 'note-bottom')):
            self.relate('connect', a, b)
        _circle(self, 'note-mark', 26, 14, 2)
        # Fist: thumb rising from the cuff to the note, cuff line, flat base, round knuckles.
        _path(self, 'fist', (16, 20), [(12, 24), (12, 44), (30, 44), ((40, 34), 10, 10, False),
                                        ((36, 26), 10, 10, False), ((30, 24), 10, 10, False)])
        # One finger crease from the knuckle extreme splits the grip into two curled fingers.
        self.add_line('finger-crease', (40, 34), (30, 34))
        # Sleeve: two edges running off to the left of the cuff line.
        self.add_line('sleeve-top', (8, 24), (12, 24))
        self.add_line('sleeve-bottom', (8, 44), (12, 44))
        for part in ('sleeve-top', 'sleeve-bottom', 'finger-crease', 'note-left-upper', 'note-left-lower',
                     'note-right', 'note-bottom'):
            self.relate('connect', 'fist', part)
