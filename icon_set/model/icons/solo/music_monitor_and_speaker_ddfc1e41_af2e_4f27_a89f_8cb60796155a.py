"""A music-note monitor with a tall two-driver speaker on its right.

Symbol plan: a partially occluded monitor frame, joined beamed notes,
pedestal, and a rounded speaker with a pair of circular drivers.
Lucide monitor-speaker informed the overlapping device layout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

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
        self.add_line("monitor-left", (4, 12), (4, 30))
        self.add_arc("monitor-sw", (4, 30), (8, 34), radius_x=4, sweep=False)
        self.add_line("monitor-bottom", (8, 34), (28, 34))
        self.add_contour("monitor", "monitor-top", "monitor-nw", "monitor-left", "monitor-sw", "monitor-bottom")
        self.add_line("monitor-bezel", (4, 27), (28, 27))
        self.relate("connect", "monitor-bezel", "monitor-left")
        self.add_line("stand-stem", (16, 34), (16, 40))
        self.add_line("stand-foot", (10, 40), (20, 40))
        self.relate("connect", "stand-stem", "stand-foot")
        self.relate("connect", "stand-stem", "monitor-bottom")

        self.add_arc("left-notehead", (12, 23), (16, 21), radius_x=3, radius_y=2, sweep=False)
        self.add_line("left-note-stem", (16, 21), (16, 16))
        self.add_line("note-beam", (16, 16), (23, 14))
        self.add_line("right-note-stem", (23, 14), (23, 20))
        self.add_arc("right-notehead", (23, 20), (19, 22), radius_x=3, radius_y=2, sweep=True)
        self.add_contour("music-notes", "left-notehead", "left-note-stem", "note-beam", "right-note-stem", "right-notehead")

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
        self.relate("connect", "monitor-bezel", "speaker-left")
        self.ring("speaker-tweeter", 36, 23, 2)
        self.ring("speaker-woofer", 36, 33, 4)
