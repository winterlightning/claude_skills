"""Open medicine capsule: two pulled-apart capsule halves with two grains of medicine spilling between them.

Plan: CIRCLE (only the two rounded ends reach radius 20 at (4,24) and (44,24)). Each half is a D 10 wide and 20 tall: a standalone flat cut edge joined to an r10 semicircle built from two cardinal quarter arcs. The halves mirror about x=24 and two grains sit between them on a slight diagonal, 8 and 12 from the cut edges.
Review of the rejected drawing: the halves were 28 tall, 14 wide flattened ellipses with chamfered corners and no spilled grains, so it read as two heavy brackets rather than an opened capsule; the reference halves are compact D caps with medicine between them.
Deliberate simplification: the reference tilts each half a few degrees; both are drawn upright so the cut edges and grains stay on the integer grid.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ef3bc9e5-1036-4389-a440-3f7857af80b0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-medicine-capsule-solo/20260928T042731Z-thuan-mac-1/reference/pill open_ef3bc9e5-1036-4389-a440-3f7857af80b0.svg'
AUTHOR = 'claude-fable-5-1'


class OpenMedicineCapsuleSolo(Solo48):
    icon_id = 'open-medicine-capsule-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    categories = ('other', 'primitives')
    aliases = ('opened-capsule', 'pill-open')
    keywords = ('pill', 'open', 'capsule', 'medicine', 'drug', 'pharmacy')

    def build(self) -> None:
        top, bottom, r = 14, 34, 10
        for side, sign in (('left', -1), ('right', 1)):
            def p(x, y):
                return (24 + sign * (x - 24), y)
            cut = 14                                   # 14 on the left, 34 on the right
            self.add_line(f'{side}-cut', p(cut, top), p(cut, bottom))
            self.add_arc(f'{side}-cap-lower', p(cut, bottom), p(cut - r, 24), radius_x=r, sweep=sign > 0)
            self.add_arc(f'{side}-cap-upper', p(cut - r, 24), p(cut, top), radius_x=r, sweep=sign > 0)
            self.add_contour(f'{side}-cap', f'{side}-cap-lower', f'{side}-cap-upper')
            self.relate('connect', f'{side}-cut', f'{side}-cap')
        # grains spill on a slight diagonal, as in the reference
        self.add_dot('grain-upper', (22, 19))
        self.add_dot('grain-lower', (26, 29))
