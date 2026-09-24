"""modern music monitor speaker: standalone repair of supplied reference.

Plan: Monitor left and speaker right. Keyshape HRECT_L.
Reduction: Reduced paired notes to one note, omitted bezel divider, reduced two speaker rings to dots, squared speaker enclosure.
Construction references: local Lucide originals and atomic-debug: monitor-speaker.

All geometry is authored for SOLO48; earlier runs remain unchanged.
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
        self.add_line("monitor-top", (18, 8), (8, 8))
        self.add_arc("monitor-nw", (8, 8), (4, 12), radius_x=4, sweep=False)
        self.add_line("monitor-left", (4, 12), (4, 28))
        self.add_arc("monitor-sw", (4, 28), (8, 32), radius_x=4, sweep=False)
        self.add_line("monitor-bottom", (8, 32), (26, 32))
        self.add_contour("monitor", "monitor-top", "monitor-nw", "monitor-left", "monitor-sw", "monitor-bottom")
        self.add_line("stand-stem", (16, 32), (16, 40))
        self.add_line("stand-foot", (10, 40), (20, 40))
        self.relate("connect", "stand-stem", "stand-foot")
        self.relate("connect", "stand-stem", "monitor-bottom")

        # One eighth note retains music at native size, with ample screen clearance.
        self.add_polyline("music-note", (13,23), (16,23), (16,17), (18,17))
        self.add_polyline("speaker", (26,14),(44,14),(44,40),(26,40),(26,32),closed=True)
        self.relate("connect", "monitor-bottom", "speaker")
        self.add_dot("speaker-tweeter", (35,23))
        self.add_dot("speaker-woofer", (35,32))
