"""A broad ladies cloche hat with small rounded ribbon loops and a curved brim. Revised in place."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '458f50aa-9a12-44e8-b8a4-281764c436e5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/hat lady_458f50aa-9a12-44e8-b8a4-281764c436e5.svg'
AUTHOR = 'gpt-6'

class LadiesHatWithBow(Solo48):
    icon_id = 'ladies-hat-with-bow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('ladies', 'hat', 'with', 'bow')

    def build(self) -> None:
        # The hat (excluding its ribbon) is symmetric about x=24. Both sides
        # follow one line from the crown shoulder through the band to the brim:
        # left (12,16)->(8,24)->(4,32); right is its exact mirror.
        # A deeper rounded dome meets each straight side with a matching tangent.
        # The original rounded bow is restored, translated left four and up one unit to
        # sit on the narrower right wall; its shape and dimensions are unchanged.
        # HRECT_L centerline extremes: (4,8)-(44,40). Lucide hat-glasses informs
        # the simple crown/brim; the supplied source retains the side ribbon.
        axis = 24
        mirror = lambda p: (2 * axis - p[0], p[1])
        shoulder = (12, 16)
        band_left = (8, 24)
        brim_left = (4, 32)
        crown_top = (axis, 8)
        control_shoulder, control_top = (14, 12), (18, 8)
        self.add_line('side-left-upper', band_left, shoulder)
        self.add_bezier('crown-left', shoulder,
                        (control_shoulder, control_top, crown_top))
        self.add_bezier('crown-right', crown_top,
                        (mirror(control_top), mirror(control_shoulder), mirror(shoulder)))
        self.add_line('side-right-upper', mirror(shoulder), (38, 20))
        self.add_contour('crown', 'side-left-upper', 'crown-left',
                         'crown-right', 'side-right-upper')
        self.add_line('brim-left', band_left, brim_left)
        self.add_arc('brim-lower-left', brim_left, (axis, 40),
                     radius_x=20, radius_y=8, sweep=False)
        self.add_arc('brim-lower-right', (axis, 40), mirror(brim_left),
                     radius_x=20, radius_y=8, sweep=False)
        self.add_line('brim-right', mirror(brim_left), mirror(band_left))
        self.add_contour('brim', 'brim-left', 'brim-lower-left',
                         'brim-lower-right', 'brim-right')
        self.add_line('band', band_left, (20, 24))
        # Restore the curved loops that were present before the mistaken edit.
        bow_x, bow_y = 30, 24
        knot = (bow_x, bow_y)
        for side in ('left', 'right'):
            sign = -1 if side == 'left' else 1
            point = lambda dx, dy: (bow_x + sign * dx, bow_y + dy)
            prefix = 'bow-' + side
            self.add_arc(prefix + '-top', knot, point(8, -4),
                         radius_x=8, radius_y=4, sweep=side == 'right')
            self.add_arc(prefix + '-outer-top', point(8, -4), point(10, 0),
                         radius_x=2, radius_y=4, sweep=side == 'right')
            self.add_arc(prefix + '-outer-bottom', point(10, 0), point(8, 4),
                         radius_x=2, radius_y=4, sweep=side == 'right')
            self.add_arc(prefix + '-bottom', point(8, 4), knot,
                         radius_x=8, radius_y=4, sweep=side == 'right')
            self.add_contour(prefix, prefix + '-top', prefix + '-outer-top',
                             prefix + '-outer-bottom', prefix + '-bottom', closed=True)
        for a, b in [('crown', 'brim'), ('crown', 'band'), ('brim', 'band'),
                     ('bow-left', 'bow-right'), ('crown', 'bow-right'),
                     ('band', 'bow-left'), ('brim', 'bow-right')]:
            self.relate('connect', a, b)
