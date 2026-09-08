"""A rounded business case has a centered top carrying handle.

HRECT_XL: visible bounds (0, 4, 64, 60), chosen for the subject proportions.
Lucide briefcase: rounded enclosure and symmetrical handle; original and atomic-debug inspected.
Source plain case retained without added straps; no source features dropped.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SimpleBusinessBriefcase(Container64):
    icon_id = 'simple-business-briefcase'
    keyshape = Keyshape.HRECT_XL
    aliases = ('business-briefcase',)
    keywords = ('simple', 'business', 'briefcase')

    def build(self) -> None:
        self.add_line('case0', (10, 18), (54, 18))
        self.add_arc('case1', (54, 18), (62, 26), radius_x=8, radius_y=8, sweep=True)
        self.add_line('case2', (62, 26), (62, 50))
        self.add_arc('case3', (62, 50), (54, 58), radius_x=8, radius_y=8, sweep=True)
        self.add_line('case4', (54, 58), (10, 58))
        self.add_arc('case5', (10, 58), (2, 50), radius_x=8, radius_y=8, sweep=True)
        self.add_line('case6', (2, 50), (2, 26))
        self.add_arc('case7', (2, 26), (10, 18), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('case', 'case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', closed=True)
        self.add_line('handle-left', (22, 18), (22, 12))
        self.add_arc('handle-nw', (22, 12), (28, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_line('handle-top', (28, 6), (36, 6))
        self.add_arc('handle-ne', (36, 6), (42, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_line('handle-right', (42, 12), (42, 18))
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right', closed=False)
        self.relate("connect", 'handle', 'case')
