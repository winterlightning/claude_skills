"""Assassin hood: a tall pointed hood seen from the front, flaring into two cape
panels at the bottom, with a wide diamond-shaped face opening.

Symbol plan: mirror symmetry about x=24 (points mirrored with x -> 48-x).
- Outer body: one open stroke. From the bottom, each cape panel is a straight lower
  edge out to its tip and a curved (upward-bowing) upper edge back in to the hood's
  leg; the leg narrows inward below the widest point, then the smooth side rises
  to a softly pointed top where the two sides meet at an obtuse angle.
- Inner shape: a closed face opening with slanted straight upper sides and curved
  lower sides that meet in a downward-pointing tip; 9+ from the hood on every side.
Revision (reviewer): taller outer body with a softly pointed top and smooth sides;
narrowed lower body before the panels; symmetric outward-flaring panels with curved
upper edges; a wider inner shape with slanted upper sides, curved lower sides and a
downward tip; clear spacing between inner and outer shapes.
Lucide construction: no hood; soft-pointed arch as in 'shield' / 'flame' tops.
Keyshape SQUARE: centerline 6..42 (panel tips, hood top, panel bottoms).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "12378975-bc57-56b2-b920-526922d97f3d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__assassin-hood/20260926T073832Z-thuan-mac/reference/assasin creed_12378975-bc57-56b2-b920-526922d97f3d.svg"
AUTHOR = "claude-opus-5-5"


def mx(p):
    return (48 - p[0], p[1])


def mseg(seg):
    return tuple(mx(p) for p in seg)


# Left half, from the left panel's bottom to the top point.
PANEL_BOTTOM, PANEL_TIP, LEG_FOOT, WIDEST, TOP = (20, 42), (6, 39), (12, 31), (9, 22), (24, 6)
UPPER_EDGE = ((9, 32), (7, 34), PANEL_TIP)            # reversed below: tip -> leg foot
LEG = ((9, 27), (10, 30), LEG_FOOT)                       # widest -> leg foot
SIDE = ((9, 14), (18, 9), TOP)                           # widest -> top


class AssassinHood(Solo48):
    icon_id = "assassin-hood"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gaming"
    aliases = ("assassin-creed", "hooded-figure")
    keywords = ("assassin", "hood", "cloak", "stealth", "game", "mystery", "cape")

    def build(self) -> None:
        # Left: bottom -> tip -> leg foot -> widest -> top.
        self.add_line("panel-left-lower", PANEL_BOTTOM, PANEL_TIP)
        self.add_bezier("panel-left-upper", PANEL_TIP, ((7, 34), (9, 32), LEG_FOOT))
        self.add_bezier("leg-left", LEG_FOOT, ((10, 30), (9, 27), WIDEST))
        self.add_bezier("side-left", WIDEST, SIDE)
        # Right: top -> widest -> leg foot -> tip -> bottom (mirror, reversed).
        self.add_bezier("side-right", TOP, ((30, 9), (39, 14), mx(WIDEST)))
        self.add_bezier("leg-right", mx(WIDEST), mseg(LEG))
        self.add_bezier("panel-right-upper", mx(LEG_FOOT), mseg(UPPER_EDGE))
        self.add_line("panel-right-lower", mx(PANEL_TIP), mx(PANEL_BOTTOM))
        self.add_contour("hood", "panel-left-lower", "panel-left-upper", "leg-left", "side-left",
                         "side-right", "leg-right", "panel-right-upper", "panel-right-lower")
        # Face opening.
        face_top, shoulder, tip = (24, 17), (18, 24), (24, 34)
        self.add_line("face-upper-left", face_top, shoulder)
        self.add_bezier("face-lower-left", shoulder, ((19, 28), (21.5, 32), tip))
        self.add_bezier("face-lower-right", tip, ((26.5, 32), (29, 28), mx(shoulder)))
        self.add_line("face-upper-right", mx(shoulder), face_top)
        self.add_contour("face", "face-upper-left", "face-lower-left", "face-lower-right",
                         "face-upper-right", closed=True)
