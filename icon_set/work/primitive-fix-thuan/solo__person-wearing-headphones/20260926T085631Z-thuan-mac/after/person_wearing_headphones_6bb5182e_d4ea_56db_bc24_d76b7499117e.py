"""A front-facing head and shoulder bust wears over-ear headphones. The band curves over the oval head, two earcups sit at the sides, and the shoulders broaden into a flat-bottomed torso.
Lucide headphones semicircular band and paired earcups. Inner top head contour and closed torso base omitted to avoid doubled tight curves; open jaw and shoulders retain the wearer.
VRECT_L: centerline extremes (8,6)-(40,42); independently authored on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6bb5182e-d4ea-56db-bc24-d76b7499117e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-wearing-headphones/20260926T085631Z-thuan-mac/reference/meeting headphones_6bb5182e-d4ea-56db-bc24-d76b7499117e.svg'
AUTHOR = 'claude-opus-5-5'

class PersonWearingHeadphones(Solo48):
    icon_id = 'person-wearing-headphones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('person', 'headphones', 'audio', 'meeting', 'listener', 'headset')

    def build(self) -> None:
        # Review: make the headphones clear. SQUARE (6,6)-(42,42), mirrored about x=24.
        # Earcups are closed 8x12 rounded boxes at the head's sides; the band is a
        # half ellipse (rx14, ry10) from the middle of each cup top over the head
        # (top at y=6), and the jaw hangs between the cups' inner walls. Shoulders
        # sit 8 below the jaw (detached bust, as in human_ref/user.svg).
        def cup(name, x0, x1, join_x):
            # join_x: inner wall (x) where the jaw attaches; top middle joins the band
            mid = (x0 + x1) // 2
            inner_left = join_x == x0
            pts = []
            self.add_line(f'{name}-top-a', (x0 + 2, 16), (mid, 16))
            self.add_line(f'{name}-top-b', (mid, 16), (x1 - 2, 16))
            self.add_arc(f'{name}-c1', (x1 - 2, 16), (x1, 18), radius_x=2, sweep=True)
            if inner_left:
                self.add_line(f'{name}-right', (x1, 18), (x1, 26))
            else:
                self.add_line(f'{name}-right-a', (x1, 18), (x1, 21))
                self.add_line(f'{name}-right-b', (x1, 21), (x1, 26))
            self.add_arc(f'{name}-c2', (x1, 26), (x1 - 2, 28), radius_x=2, sweep=True)
            self.add_line(f'{name}-bottom', (x1 - 2, 28), (x0 + 2, 28))
            self.add_arc(f'{name}-c3', (x0 + 2, 28), (x0, 26), radius_x=2, sweep=True)
            if inner_left:
                self.add_line(f'{name}-left-a', (x0, 26), (x0, 21))
                self.add_line(f'{name}-left-b', (x0, 21), (x0, 18))
            else:
                self.add_line(f'{name}-left', (x0, 26), (x0, 18))
            self.add_arc(f'{name}-c4', (x0, 18), (x0 + 2, 16), radius_x=2, sweep=True)
            members = [f'{name}-top-a', f'{name}-top-b', f'{name}-c1']
            members += [f'{name}-right'] if inner_left else [f'{name}-right-a', f'{name}-right-b']
            members += [f'{name}-c2', f'{name}-bottom', f'{name}-c3']
            members += [f'{name}-left-a', f'{name}-left-b'] if inner_left else [f'{name}-left']
            members += [f'{name}-c4']
            self.add_contour(name, *members, closed=True)

        cup('cup-left', 6, 14, 14)
        cup('cup-right', 34, 42, 34)
        self.add_arc('band', (10, 16), (38, 16), radius_x=14, radius_y=10, sweep=True)
        self.add_arc('jaw', (14, 21), (34, 21), radius_x=10, radius_y=7, sweep=False)
        for part in ('cup-left', 'cup-right'):
            self.relate('connect', 'band', part)
            self.relate('connect', 'jaw', part)
        self.add_arc('shoulder-left', (8, 42), (16, 36), radius_x=8, radius_y=6, sweep=True)
        self.add_line('shoulder-top', (16, 36), (32, 36))
        self.add_arc('shoulder-right', (32, 36), (40, 42), radius_x=8, radius_y=6, sweep=True)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-top', 'shoulder-right')
