"""A music-note monitor with a tall two-driver speaker on its right.

Symbol plan: a partially occluded monitor frame, joined beamed notes,
pedestal, and a rounded speaker with a pair of circular drivers.
Lucide monitor-speaker informed the overlapping device layout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ddfc1e41-af2e-4f27-a89f-8cb60796155a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/modern music monitor speaker_ddfc1e41-af2e-4f27-a89f-8cb60796155a.svg"
AUTHOR = "gpt-6"


class MusicMonitorAndSpeaker(Solo48):
    icon_id = "music-monitor-and-speaker"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/media"
    aliases = ("modern music monitor speaker", "music desktop speakers")
    keywords = ("audio", "computer", "speaker", "notes")

    def ring(self, name: str, x: int, y: int, radius: int) -> None:
        self.add_arc(name + "-right", (x, y - radius), (x, y + radius), radius_x=radius, sweep=True)
        self.add_arc(name + "-left", (x, y + radius), (x, y - radius), radius_x=radius, sweep=True)
        self.add_contour(name, name + "-right", name + "-left", closed=True)

    def build(self) -> None:
        self.add_line("monitor-top", (26, 8), (8, 8))
        self.add_arc("monitor-nw", (8, 8), (4, 12), radius_x=4, sweep=False)
        self.add_line("monitor-left", (4, 12), (4, 28))
        self.add_arc("monitor-sw", (4, 28), (8, 32), radius_x=4, sweep=False)
        self.add_line("monitor-bottom", (8, 32), (28, 32))
        self.add_contour("monitor", "monitor-top", "monitor-nw", "monitor-left", "monitor-sw", "monitor-bottom")
        self.add_line("stand-stem", (16, 32), (16, 40))
        self.add_line("stand-foot", (10, 40), (20, 40))
        self.relate("connect", "stand-stem", "stand-foot")
        self.relate("connect", "stand-stem", "monitor-bottom")

        # One eighth note retains music at native size, with ample screen clearance.
        self.add_polyline("music-note", (13,23), (18,23), (18,16), (24,16))
        r = 4
        self.add_line("speaker-top", (32, 16), (40, 16))
        self.add_arc("speaker-ne", (40, 16), (44, 20), radius_x=r, sweep=True)
        self.add_line("speaker-right", (44, 20), (44, 36))
        self.add_arc("speaker-se", (44, 36), (40, 40), radius_x=r, sweep=True)
        self.add_line("speaker-bottom", (40, 40), (32, 40))
        self.add_arc("speaker-sw", (32, 40), (28, 36), radius_x=r, sweep=True)
        self.add_line("speaker-left", (28, 36), (28, 20))
        self.add_arc("speaker-nw", (28, 20), (32, 16), radius_x=r, sweep=True)
        self.add_contour("speaker", "speaker-top", "speaker-ne", "speaker-right", "speaker-se", "speaker-bottom", "speaker-sw", "speaker-left", "speaker-nw", closed=True)
        self.relate("connect", "monitor-bottom", "speaker-left")
        self.add_dot("speaker-tweeter", (36,24))
        self.add_dot("speaker-woofer", (36,32))
