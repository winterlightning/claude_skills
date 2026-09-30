"""bitcoin-speech-bubble-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded speech bubble with a lower-left tail holding a Bitcoin B,
on VRECT_L (centerline box (8,4)-(40,44)).
- bubble: a ring of standalone lines and r8 corner arcs joined by
  connect, body (8,4)-(40,40), rounded on the top and the lower right;
  the left wall runs straight down to the tail tip (8,44) and a 45 degree
  edge returns to the bottom edge at (12,40) (Lucide message-square
  construction).
- B: spine x=19 with a 2-unit serif on the top and bottom bars (x=17);
  two equal r4 lobes (bars to x=27, apex x=31) meeting at the right end of
  the middle bar (27,22). The B ink spans x 15..33, centred on x=24; the
  serif ends sit 9 from the left wall (an exact 8 to a wall comes back
  as review).
- ticks: four standalone 2-unit lines at x=19 (spine) and x=27, 8 apart,
  ending at y=12 and y=32: exactly 8 from the bubble's top (4) and bottom
  (40) walls, which certifies because both sides are plain lines.
Every T-junction is split so the parts share real endpoints.

Keyshape: the metrics suggest SQUARE, but its 36-unit height cannot hold
bubble wall + 8 + ticked B (2 + 8 + 8 + 2) + 8 + wall (36 inside the
bubble) plus a tail below it; VRECT_L gives the 40 units needed.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4 with all gaps sized for it.
- stroke-count: NOT met, see below.
- clearance (all 14): ticks now 8 from the bubble walls, the ticks 8 apart,
  the B lobes 8 apart (bar to bar) and every other pair at >= 8 or joined.
- loose-join (both): spine, bars and ticks share exact endpoints and are
  declared with relate("connect").
- hole (both): lobes widened from ~7 to 8 on centerlines (4 ink); the
  metric's 6-ink target (10 on centerlines) is NOT met, see below.
Not fixed: the metric's 6-ink hole target would need lobes 10 tall; 2 x 10
+ ticks + 2 x 8 clearance is 40, more than the 36 inside the bubble, and
dropping the ticks loses the Bitcoin reading. The 8-unit lobes pass the
Solo48 validator and the build gate's hole rule.
Not fixed: stroke count. The ink forms 2 connected shapes (bubble, and
the B with its ticks), but the model uses 15 paths (8 bubble members,
2 lobes, spine, 4 ticks), over the budget of 6. The bubble and the ticks
must be standalone lines for the exact-8 wall gap to certify, and without
the ticks the B does not read as Bitcoin.

Lucide: bitcoin (serif bars, ticks from the spine) and message-square
(straight left wall into the tail) informed the construction.
Traced shape: 20260929-1824-bitcoin-speech-bubble-solo/bitcoin-speech-bubble-solo_raw.svg
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1b6ce2a0-ce30-49ce-99cf-a772bb04245d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1824-bitcoin-speech-bubble-solo/"
    "bitcoin-speech-bubble-solo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

L, R, T, B = 8, 40, 4, 40   # bubble body walls
CR = 8                      # bubble corner radius
TAIL_TIP = (8, 44)
TAIL_BASE = (12, 40)

SERIF_X = 17
SPINE_X = 19
TICK_X = 27
TOP_Y, MID_Y, BOT_Y = 14, 22, 30
TICK = 2
LOBE_R = 4
LOBE_END = 27               # bar ends, apex 31


class BitcoinSpeechBubbleSoloRedraw(Solo48):
    icon_id = "bitcoin-speech-bubble-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("bitcoin-message", "crypto-chat")
    keywords = ("bitcoin", "btc", "crypto", "currency", "speech bubble",
                "message", "chat", "payment")

    def build(self) -> None:
        # Bubble, clockwise from the top-left corner.
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (R - CR, B), TAIL_BASE)
        self.add_line("tail", TAIL_BASE, TAIL_TIP)
        self.add_line("left", TAIL_TIP, (L, T + CR))
        self.add_arc("tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        # Standalone members joined in a ring: a flat wall certifies an exact
        # 8 to the ticks only as its own line, not inside an arc contour.
        ring = ("top", "tr", "right", "br", "bottom", "tail", "left", "tl")
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)

        # Upper lobe: serif, top bar, arc, back along the middle bar.
        self.add_line("serif-top", (SERIF_X, TOP_Y), (SPINE_X, TOP_Y))
        self.add_line("bar-top", (SPINE_X, TOP_Y), (LOBE_END, TOP_Y))
        self.add_arc("lobe-upper", (LOBE_END, TOP_Y), (LOBE_END, MID_Y),
                     radius_x=LOBE_R, sweep=True)
        self.add_line("mid", (LOBE_END, MID_Y), (SPINE_X, MID_Y))
        self.add_contour("b-upper", "serif-top", "bar-top", "lobe-upper", "mid")

        # Lower lobe: serif, bottom bar, arc up to the middle bar's end.
        self.add_line("serif-bot", (SERIF_X, BOT_Y), (SPINE_X, BOT_Y))
        self.add_line("bar-bot", (SPINE_X, BOT_Y), (LOBE_END, BOT_Y))
        self.add_arc("lobe-lower", (LOBE_END, BOT_Y), (LOBE_END, MID_Y),
                     radius_x=LOBE_R, sweep=False)
        self.add_contour("b-lower", "serif-bot", "bar-bot", "lobe-lower")

        # Spine with its own ticks, split at every bar.
        self.add_line("spine-top", (SPINE_X, TOP_Y), (SPINE_X, MID_Y))
        self.add_line("spine-bot", (SPINE_X, MID_Y), (SPINE_X, BOT_Y))
        self.add_contour("spine", "spine-top", "spine-bot")
        self.relate("connect", "b-upper", "b-lower")
        self.relate("connect", "spine", "b-upper")
        self.relate("connect", "spine", "b-lower")

        # Four plain tick lines (a straight line certifies an exact 8 to the
        # bubble's flat walls; a contour or polyline there comes back review).
        for name, x in (("l", SPINE_X), ("r", TICK_X)):
            self.add_line(f"tick-{name}-top", (x, TOP_Y - TICK), (x, TOP_Y))
            self.add_line(f"tick-{name}-bot", (x, BOT_Y), (x, BOT_Y + TICK))
            self.relate("connect", f"tick-{name}-top", "b-upper")
            self.relate("connect", f"tick-{name}-bot", "b-lower")
