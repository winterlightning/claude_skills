"""A zipper-mouth face: a round face with dot eyes and a zipped-shut mouth.

Symbol plan: the head is one circle (r20). Two dot eyes. The mouth is a zipper: one
horizontal line crossed by two short teeth (each tooth split with the line at its exact
node, 8 apart), ending at the right in the slider's pull hanging down. Everything inside
stays within radius 12 of the centre so it keeps 8 from the rim.
The reference's rounded pull tab overlapping the rim and its extra teeth are reduced: at
48 only two teeth 8 apart and a straight pull fit inside the face.
Lucide construction: 'smile'/'meh' face construction (circle, dot eyes, mouth line).
Keyshape CIRCLE: centerline radius 20 about (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "553978e0-a38a-465c-89ce-33f54387ba69"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__zipper-mouth-face/20260926T044250Z-thuan-mac/reference/zipped_553978e0-a38a-465c-89ce-33f54387ba69.svg"
AUTHOR = "claude-opus-5-5"


class ZipperMouthFace(Solo48):
    icon_id = "zipper-mouth-face"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotion"
    aliases = ("zipped mouth", "lips sealed", "secret face")
    keywords = ("zipper", "mouth", "secret", "quiet", "silence", "sealed", "emoji", "face", "mute")

    def build(self) -> None:
        c, r = 24, 20
        self.add_arc("head-top", (c - r, c), (c + r, c), radius_x=r)
        self.add_arc("head-bottom", (c + r, c), (c - r, c), radius_x=r)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_dot("eye-left", (18, 15))
        self.add_dot("eye-right", (30, 15))
        y, x0, x1, teeth, t = 26, 13, 31, (15, 23), 3
        stops = [x0, *teeth, x1]
        segs = []
        for i in range(len(stops) - 1):
            segs.append(f"zip-{i}")
            self.add_line(f"zip-{i}", (stops[i], y), (stops[i + 1], y))
        self.add_line("pull", (x1, y), (x1, y + 5))
        segs.append("pull")
        self.add_contour("zipper", *segs)
        for i, x in enumerate(teeth):
            self.add_line(f"tooth-{i}-up", (x, y - t), (x, y))
            self.add_line(f"tooth-{i}-down", (x, y), (x, y + t))
            self.add_contour(f"tooth-{i}", f"tooth-{i}-up", f"tooth-{i}-down")
            self.relate("connect", "zipper", f"tooth-{i}")
