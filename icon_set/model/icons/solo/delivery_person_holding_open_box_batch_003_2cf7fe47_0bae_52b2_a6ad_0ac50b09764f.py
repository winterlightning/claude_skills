"""delivery-person-holding-open-box-batch-003: independent batch-003 SOLO48 result for brief 03.

Subject: A right-facing courier stick figure in a peaked cap carrying an open box with a raised rear flap.
Keyshape: SQUARE -- a full-height standing figure beside a chest-height box fills a square.
Plan: Stick figure from human_ref/full_body_ref.png: head r5 at (11,11), torso junction (11,24) exactly 8 below the head outline, bent arm to the box's lower-left corner; box is a closed rectangle whose rear flap (parallelogram) rises from its top edge to the corner.
Reduction: Outlined torso reduced to the shared stick-figure vocabulary; cap reduced to a brim leaving the head at its band line.
Construction reference: package-open (box with raised flap) for the box; human anatomy from the shared human reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cf7fe47-0bae-52b2-a6ad-0ac50b09764f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/construction/folding pocket knife_2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/folding pocket knife_2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/03-delivery-person-with-open-box--2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.md'


class DeliveryPersonHoldingOpenBoxBatch003(Solo48):
    icon_id = 'delivery-person-holding-open-box-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('delivery', 'person', 'box', 'parcel', 'courier', 'holding')

    # -- local construction helpers ------------------------------------------
    def _run(self, name, start, commands, closed=False):
        """One stroke run: ('L', end) lines, ('A', end, rx, ry, sweep[, large]) arcs,
        ('C', end, c1, c2) cubics. Members are grouped into one contour."""
        here, members = start, []
        for index, (kind, end, *args) in enumerate(commands, 1):
            ident = f"{name}-{index}"
            if kind == "L":
                self.add_line(ident, here, end)
            elif kind == "A":
                rx, ry, sweep = args[:3]
                large = args[3] if len(args) > 3 else False
                self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large)
            elif kind == "C":
                self.add_bezier(ident, here, (args[0], args[1], end))
            members.append(ident)
            here = end
        self.add_contour(name, *members, closed=closed)
        return members

    def _circle(self, name, cx, cy, r):
        self._run(name, (cx - r, cy), [("A", (cx + r, cy), r, r, True), ("A", (cx - r, cy), r, r, True)], closed=True)

    def build(self) -> None:
        # Courier stick figure (human_ref/full_body_ref.png): head r5, detached 8 above the torso.
        ax, hy, hr = 11, 11, 5
        neck, hip = (ax, hy + hr + 8), (ax, 34)
        # The upper half of the head reads as the cap crown; its brim leaves the band at the
        # head's east point, so the head stays two cardinal semicircles.
        self._circle("head", ax, hy, hr)
        self.add_line("cap-visor", (ax + hr, hy), (ax + hr + 4, hy))
        self.relate("connect", "head", "cap-visor")
        self.add_line("torso", neck, hip)
        self._run("legs", (ax - 4, 42), [("L", hip), ("L", (ax + 4, 42))])
        self.relate("connect", "torso", "legs")
        # Bent carrying arm: shoulder -> elbow (8 clear of the torso) -> hand under the box.
        elbow, hand = (19, 30), (26, 30)
        self._run("arm", neck, [("L", elbow), ("L", hand)])
        self.relate("connect", "torso", "arm")
        # Open box (26..42 x 18..30) with a tall rear flap rising from its top edge to the corner.
        bx1, by0 = 42, 18
        flap_foot, flap_top = (33, by0), [(30, 6), (39, 6)]
        self._run("box", hand, [("L", (bx1, hand[1])), ("L", (bx1, by0)), ("L", flap_foot),
                                ("L", (hand[0], by0)), ("L", hand)], closed=True)
        self._run("flap", flap_foot, [("L", flap_top[0]), ("L", flap_top[1]), ("L", (bx1, by0))])
        self.relate("connect", "box", "flap")
        self.relate("connect", "arm", "box")
        self.mark_human_figure("courier", head="head", torso="torso", torso_junction="start")
