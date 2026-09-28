"""Two opposed cupped hands protecting a heart between them.

Plan: CIRCLE. An outlined heart (r4 lobes, 16 wide, r5 shoulders) sits at the centre. Each hand is a cupped palm drawn as a quarter arc of radius 20 about the centre, with a thumb spur turning inwards at its wrist end: the upper-right hand runs from the top point to the right point with its thumb pointing down-left, and the lower-left hand is the same shape rotated 180 degrees. Only the two palm arcs reach the CIRCLE envelope.
Review of the rejected drawing: the heart was a tiny lumpy shape with a hole in it and the two hands were bent single strokes that read as hooks or brackets, so nothing read as hands around a heart; the original shows a large clear heart cradled between an upper and a lower open hand.
Deliberate asymmetry: the hands are rotationally, not mirror, symmetric, as in the original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '59eb4021-6108-44f6-8147-e5750c232c19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opposed-hands-protecting-heart/20260928T042731Z-thuan-mac-1/reference/support 2_59eb4021-6108-44f6-8147-e5750c232c19.svg'
AUTHOR = "claude-fable-5-1"


class OpposedHandsProtectingHeart(Solo48):
    icon_id = 'opposed-hands-protecting-heart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('hands-around-heart', 'support-heart')
    keywords = ('support', 'care', 'hands', 'heart', 'protect', 'charity')

    def build(self) -> None:
        # heart: lobes r4 centred (20,23)/(28,23), r5 shoulders, straight sides to the tip
        cx, y, r, tip = 24, 23, 4, 33
        self.add_arc('heart-lobe-left', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
        self.add_arc('heart-shoulder-left', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
        self.add_line('heart-side-left', (cx - 2 * r + 2, y + 4), (cx, tip))
        self.add_line('heart-side-right', (cx, tip), (cx + 2 * r - 2, y + 4))
        self.add_arc('heart-shoulder-right', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
        self.add_arc('heart-lobe-right', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
        self.add_contour('heart', 'heart-lobe-left', 'heart-shoulder-left', 'heart-side-left',
                         'heart-side-right', 'heart-shoulder-right', 'heart-lobe-right', closed=True)
        # hands: palm arc r20 about (24,24) plus an inward thumb at the wrist end
        for name, sign in (('upper-hand', 1), ('lower-hand', -1)):
            def p(x, y):
                return (24 + sign * (x - 24), 24 + sign * (y - 24))
            self.add_arc(f'{name}-palm', p(24, 4), p(44, 24), radius_x=20, sweep=True)
            self.add_line(f'{name}-thumb', p(44, 24), p(40, 30))
            self.add_contour(name, f'{name}-palm', f'{name}-thumb')
