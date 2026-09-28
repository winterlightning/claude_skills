"""A film frame: a rounded frame with a perforated strip along the top and bottom around a large picture area.

Symbol plan: one closed rounded rectangle (r3 corners), its side walls split where the
two strip dividers attach, 8 below the top and 8 above the bottom. Each strip is divided
by two perforation ticks (edge to divider, shared endpoints) into three sprocket
windows 10 wide. The picture area between the dividers is 20 tall.
The reference's floating dash perforations become ticks joining edge and divider: a
dash would need 8 units of clearance above and below inside an 8-tall strip.
Lucide construction: 'film' - frame with strip dividers and perforation ticks.
Keyshape SQUARE: centerline x 6..42, y 6..42 (frame).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2c0caaff-251d-42ec-9746-332bd5f92647"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chamfered-film-strip-frame/20260926T044250Z-thuan-mac/reference/film_2c0caaff-251d-42ec-9746-332bd5f92647.svg"
AUTHOR = "claude-opus-5-5"


class ChamferedFilmStripFrame(Solo48):
    icon_id = "chamfered-film-strip-frame"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "media/video"
    aliases = ("film", "film frame", "film strip")
    keywords = ("film", "movie", "cinema", "frame", "video", "reel", "strip", "photo")

    def build(self) -> None:
        l, r, t, b, cr = 6, 42, 6, 42, 3
        d1, d2 = t + 8, b - 8
        ticks = (17, 31)
        top_nodes = [l + cr, *ticks, r - cr]
        bot_nodes = list(reversed(top_nodes))
        members = []

        def line(name, a, c):
            self.add_line(name, a, c)
            members.append(name)

        for i in range(len(top_nodes) - 1):
            line(f"top-{i}", (top_nodes[i], t), (top_nodes[i + 1], t))
        self.add_arc("corner-tr", (r - cr, t), (r, t + cr), radius_x=cr)
        members.append("corner-tr")
        line("right-0", (r, t + cr), (r, d1))
        line("right-1", (r, d1), (r, d2))
        line("right-2", (r, d2), (r, b - cr))
        self.add_arc("corner-br", (r, b - cr), (r - cr, b), radius_x=cr)
        members.append("corner-br")
        for i in range(len(bot_nodes) - 1):
            line(f"bottom-{i}", (bot_nodes[i], b), (bot_nodes[i + 1], b))
        self.add_arc("corner-bl", (l + cr, b), (l, b - cr), radius_x=cr)
        members.append("corner-bl")
        line("left-0", (l, b - cr), (l, d2))
        line("left-1", (l, d2), (l, d1))
        line("left-2", (l, d1), (l, t + cr))
        self.add_arc("corner-tl", (l, t + cr), (l + cr, t), radius_x=cr)
        members.append("corner-tl")
        self.add_contour("frame", *members, closed=True)
        for y, edge in ((d1, t), (d2, b)):
            nodes = [l, *ticks, r]
            names = []
            for i in range(len(nodes) - 1):
                n = f"divider-{y}-{i}"
                self.add_line(n, (nodes[i], y), (nodes[i + 1], y))
                names.append(n)
            self.add_contour(f"divider-{y}", *names)
            self.relate("connect", "frame", f"divider-{y}")
            for x in ticks:
                self.add_line(f"tick-{y}-{x}", (x, edge), (x, y))
                self.relate("connect", "frame", f"tick-{y}-{x}")
                self.relate("connect", f"divider-{y}", f"tick-{y}-{x}")
