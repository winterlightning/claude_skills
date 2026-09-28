"""Muslim dad son 1 avatar: a father and his young son side by side, both wearing
kufi prayer caps; the father stands taller on the right.

Revision (disapproved, reason not recorded): the rejected drawing was a single
bust with a flat hat band, so the son -- half of the subject -- was missing. The
original shows two figures, the taller father behind-right and the son left,
each in a kufi. Both figures are restored.

Symbol plan: two busts on the shared avatar construction, one per figure axis.
Each head is a kufi dome of radius 8 closed by its hem, with a radius-8 jaw
hanging from the hem (the face); each body is one shoulder arch on the head's own
axis, its top 4 below the chin (touching ink, avatar rule; jaw and arch share
the axis). Father: axis x=36, dome top 8, hem y=16, chin 24, arch rx 8 ry 12
(top 28) to the ground line y=40. Son: axis x=12, dome top 12, hem y=20, chin 28,
arch rx 7 ry 8 (top 32), so he stands shorter. The heads are 8.3 apart at their
nearest and the arches' feet 9 apart.
Omissions: the father's arm and the robes' seams (no 8-unit room between the two
bodies).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'users' (two busts side by side).
Keyshape HRECT_L: centerline x 4 (son) .. 44 (father), y 8 (father) .. 40.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "0bb8bb81-d201-4d3a-8d27-21a8a54273b5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__muslim-dad-son-1-avatar/20260926T175625Z-thuan-mac-1/reference/muslim dad son_0bb8bb81-d201-4d3a-8d27-21a8a54273b5.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

HEAD_R = 8
GROUND = 40


class MuslimDadSon1Avatar(Solo48):
    icon_id = "muslim-dad-son-1-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("muslim-father-son", "father-and-son")
    keywords = ("muslim", "dad", "father", "son", "child", "family", "kufi", "cap", "avatar", "people")

    def figure(self, name: str, x: int, hem: int, arch_rx: int) -> None:
        r = HEAD_R
        self.add_arc(f"{name}-kufi-left", (x - r, hem), (x, hem - r), radius_x=r)
        self.add_arc(f"{name}-kufi-right", (x, hem - r), (x + r, hem), radius_x=r)
        self.add_line(f"{name}-hem", (x + r, hem), (x - r, hem))
        self.add_contour(f"{name}-kufi", f"{name}-kufi-left", f"{name}-kufi-right", f"{name}-hem", closed=True)
        self.add_arc(f"{name}-jaw", (x + r, hem), (x - r, hem), radius_x=r)
        self.relate("connect", f"{name}-kufi", f"{name}-jaw")
        top = hem + r + HEAD_BODY_CENTERLINE_GAP
        self.add_arc(f"{name}-shoulders", (x - arch_rx, GROUND), (x + arch_rx, GROUND),
                     radius_x=arch_rx, radius_y=GROUND - top)
        self.relate("connect", f"{name}-jaw", f"{name}-shoulders")

    def build(self) -> None:
        self.figure("dad", 36, 16, 8)
        self.figure("son", 12, 20, 7)
