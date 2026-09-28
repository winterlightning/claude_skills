"""Two Christmas bells hanging under a ribbon bow.

Plan: SQUARE (6,6)-(42,42). The bow is a figure-eight of two ellipses (rx9, ry4) sharing the knot point (24,10), so the loops touch the SQUARE top and sides. Below it two matching bells mirror about x=24: an r6 dome, flared skirt lines, a flat lip and a short clapper stroke hanging from the lip centre.
Review of the rejected drawing: the bow was a bare chevron and the bells were 12 units tall with tiny domes, so the drawing read as a v over two thimbles; the original has full ribbon loops and large flared bells.
Omissions: the ribbon tails (no 8-unit room between the bells) and the bells' inner clapper balls (a hanging stroke stands in).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '71902e74-498c-4f90-9102-f4805b93d83d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__paired-christmas-bells-with-bow/20260928T042731Z-thuan-mac-1/reference/christmas bells_71902e74-498c-4f90-9102-f4805b93d83d.svg'
AUTHOR = "claude-fable-5-1"


class PairedChristmasBellsWithBow(Solo48):
    icon_id = 'paired-christmas-bells-with-bow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('jingle-bells-with-bow',)
    keywords = ('christmas', 'bells', 'bow', 'ribbon', 'jingle', 'holiday')

    def build(self) -> None:
        knot, ky, rx, ry = 24, 10, 9, 4
        for name, cx in (('loop-left', knot - rx), ('loop-right', knot + rx)):
            pts = [(cx - rx, ky), (cx, ky - ry), (cx + rx, ky), (cx, ky + ry)]
            ids = []
            for i in range(4):
                self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=rx, radius_y=ry, sweep=True)
                ids.append(f'{name}-{i}')
            self.add_contour(name, *ids, closed=True)
        self.relate('connect', 'loop-left', 'loop-right')
        # bells: dome r6 centred (cx,30), skirt to cx+-7 at the lip y=36, clapper to 42
        for name, cx in (('bell-left', 13), ('bell-right', 35)):
            self.add_arc(f'{name}-dome', (cx - 6, 30), (cx + 6, 30), radius_x=6, sweep=True)
            self.add_line(f'{name}-skirt-right', (cx + 6, 30), (cx + 7, 36))
            self.add_line(f'{name}-lip-right', (cx + 7, 36), (cx, 36))
            self.add_line(f'{name}-lip-left', (cx, 36), (cx - 7, 36))
            self.add_line(f'{name}-skirt-left', (cx - 7, 36), (cx - 6, 30))
            self.add_contour(name, f'{name}-dome', f'{name}-skirt-right', f'{name}-lip-right',
                             f'{name}-lip-left', f'{name}-skirt-left', closed=True)
            self.add_line(f'{name}-clapper', (cx, 36), (cx, 42))
            self.relate('connect', f'{name}-clapper', name)
