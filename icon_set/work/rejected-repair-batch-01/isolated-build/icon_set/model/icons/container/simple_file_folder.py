"""A tabbed folder has a low overlapping front pocket.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide folder-open: tab transitions and overlapping pocket construction; original and atomic-debug inspected.
Unequal front and back heights and left tabs preserve the source asymmetry. No features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SimpleFileFolder(Container64):
    icon_id = 'simple-file-folder'
    keyshape = Keyshape.SQUARE
    aliases = ('file-folder',)
    keywords = ('simple', 'file', 'folder')

    def build(self) -> None:
        self.add_line('rear-left', (6, 44), (6, 6))
        self.add_arc('rear-nw', (6, 6), (10, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_line('rear-tab', (10, 2), (20, 2))
        self.add_arc('rear-tab-down', (20, 2), (26, 4), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('rear-tab-level', (26, 4), (32, 6), radius_x=10, radius_y=10, sweep=False)
        self.add_line('rear-top', (32, 6), (54, 6))
        self.add_arc('rear-ne', (54, 6), (58, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('rear-right', (58, 10), (58, 50))
        self.add_contour('rear', 'rear-left', 'rear-nw', 'rear-tab', 'rear-tab-down', 'rear-tab-level', 'rear-top', 'rear-ne', 'rear-right', closed=False)
        self.add_line('front-tab', (6, 44), (14, 44))
        self.add_line('front-slope', (14, 44), (24, 50))
        self.add_line('front-top', (24, 50), (58, 50))
        self.add_arc('front-ne', (58, 50), (62, 54), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-right', (62, 54), (62, 58))
        self.add_arc('front-se', (62, 58), (58, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-bottom', (58, 62), (6, 62))
        self.add_arc('front-sw', (6, 62), (2, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-left', (2, 58), (2, 48))
        self.add_arc('front-nw', (2, 48), (6, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('front', 'front-tab', 'front-slope', 'front-top', 'front-ne', 'front-right', 'front-se', 'front-bottom', 'front-sw', 'front-left', 'front-nw', closed=True)
        self.relate("connect", 'front', 'rear')
