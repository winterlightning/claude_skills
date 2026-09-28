"""A smiling young ninja with spiky hair and a forehead headband (Naruto-style).

Plan: VRECT_L (8,4)-(40,44). Three tall uneven hair spikes (a zigzag from (8,18) through peaks (11,7), (22,4) and (35,6) to (40,18), deliberately irregular so they read as hair rather than a crown) stand on the headband line y=18; the band is split at the spike valleys so each segment is a standalone straight line. The face hangs from the band: straight temples from (8,18) and (40,18) down to y=28 and an r16 semicircle jaw with its chin at (24,44). Dot eyes at (17,26)/(31,26) and an r6 smile from (20,34) to (28,34).
Review of the rejected drawing: the head was a box whose top was a shallow zigzag, with a band and a jaw that read as a bucket or a crown; the original has tall spiky hair over a headband and a round smiling face.
Omissions: the headband emblem and the ears (no 8-unit room inside or beside a 32-wide head).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8a1f6e9-9f3c-4664-9970-8b698723fca9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-ninja-with-headband/20260928T042731Z-thuan-mac-1/reference/ninja naruto shippuden_e8a1f6e9-9f3c-4664-9970-8b698723fca9.svg'
AUTHOR = 'claude-fable-5-1'


class SmilingNinjaWithHeadband(Solo48):
    icon_id = 'smiling-ninja-with-headband'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ('naruto-face', 'spiky-hair-ninja')
    keywords = ('ninja', 'naruto', 'shippuden', 'headband', 'anime', 'smiling', 'video-games')

    def build(self) -> None:
        band = 18
        self.add_polyline('hair', (8, band), (11, 7), (18, band), (22, 4), (30, band), (35, 6), (40, band))
        self.add_line('band-left', (8, band), (18, band))
        self.add_line('band-mid', (18, band), (30, band))
        self.add_line('band-right', (30, band), (40, band))
        for seg in ('band-left', 'band-mid', 'band-right'):
            self.relate('connect', seg, 'hair')
        self.relate('connect', 'band-left', 'band-mid')
        self.relate('connect', 'band-mid', 'band-right')
        self.add_line('temple-left', (8, band), (8, 28))
        self.add_arc('jaw-left', (8, 28), (24, 44), radius_x=16, sweep=False)
        self.add_arc('jaw-right', (24, 44), (40, 28), radius_x=16, sweep=False)
        self.add_line('temple-right', (40, 28), (40, band))
        self.add_contour('jaw', 'jaw-left', 'jaw-right')
        self.relate('connect', 'temple-left', 'band-left')
        self.relate('connect', 'temple-left', 'jaw')
        self.relate('connect', 'temple-right', 'jaw')
        self.relate('connect', 'temple-right', 'band-right')
        self.add_dot('eye-left', (17, 26))
        self.add_dot('eye-right', (31, 26))
        self.add_arc('smile', (20, 34), (28, 34), radius_x=6, sweep=False)
