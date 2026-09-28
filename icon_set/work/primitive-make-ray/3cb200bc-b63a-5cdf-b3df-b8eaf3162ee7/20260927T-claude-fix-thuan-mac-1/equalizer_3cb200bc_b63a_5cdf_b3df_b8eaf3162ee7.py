"""Equalizer: three vertical slider tracks, each with a round knob set at a
different level -- low, high, lowest.

Revision (disapproved, reason not recorded): the rejected drawing squashed the
knobs into flat ovals with pinched slits for counters and crowded the tracks, so
the round knobs of the original read as eyes or beads; the original's knobs are
full circles that interrupt their tracks. Round knobs on evenly spaced tracks
are restored.

Symbol plan: tracks x=9, 24, 39 from y=8 to y=40. Knobs: radius-5 rings on the
tracks at (9,28), (24,16) and (39,33) -- left low, middle high, right lowest, as
in the reference; each track stops at its knob's top and bottom. Knobs are 10
clear of the neighbouring tracks.
Lucide construction: 'sliders-vertical' (tracks with knobs).
Keyshape HRECT_L: centerline x 4..44 (outer knobs), y 8..40 (tracks).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3cb200bc-b63a-5cdf-b3df-b8eaf3162ee7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__equalizer/20260926T182653Z-thuan-mac-1/reference/equalizer_3cb200bc-b63a-5cdf-b3df-b8eaf3162ee7.svg"
AUTHOR = "claude-opus-5-5"

KNOB_R = 5
SLIDERS = ((9, 28), (24, 16), (39, 33))


class Equalizer(Solo48):
    icon_id = "equalizer"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "media/audio"
    aliases = ("sliders", "mixer", "eq")
    keywords = ("equalizer", "eq", "sliders", "mixer", "audio", "sound", "settings", "levels")

    def build(self) -> None:
        r = KNOB_R
        for i, (x, y) in enumerate(SLIDERS):
            k = f"knob-{i}"
            self.add_arc(f"{k}-a", (x - r, y), (x, y - r), radius_x=r)
            self.add_arc(f"{k}-b", (x, y - r), (x + r, y), radius_x=r)
            self.add_arc(f"{k}-c", (x + r, y), (x, y + r), radius_x=r)
            self.add_arc(f"{k}-d", (x, y + r), (x - r, y), radius_x=r)
            self.add_contour(k, f"{k}-a", f"{k}-b", f"{k}-c", f"{k}-d", closed=True)
            self.add_line(f"track-{i}-top", (x, 8), (x, y - r))
            self.add_line(f"track-{i}-bottom", (x, y + r), (x, 40))
            self.relate("connect", k, f"track-{i}-top")
            self.relate("connect", k, f"track-{i}-bottom")
