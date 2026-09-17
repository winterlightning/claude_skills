"""Sedan Car Profile: independently authored container.

Construction plan: Side-view cabin with sloping shoulders and two wheel arches; directional profile retained, Lucide informs wheel circles.
Keyshape HRECT_S; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg. Lucide car-front original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 16, 64, 48).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
AUTHOR = 'gpt-6'


class SedanProfileContainer(Container64):
    icon_id = 'sedan-profile-container'
    keyshape = Keyshape.HRECT_S
    aliases = ()
    keywords = ('sedan', 'profile', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'body',(10,40),[('L',(6,40)),('A',(2,36),4,4,True),('L',(2,30)),('A',(6,26),4,4,True),('L',(12,26)),('L',(22,18)),('L',(38,18)),('L',(48,26)),('L',(58,28)),('A',(62,32),4,4,True),('L',(62,40)),('L',(54,40))])
        line('sill',(22,40),(42,40))
        for x in (16,48):
         ellipse(self,f'wheel-{x}',x,40,6)
        for n in ('wheel-16','wheel-48'):join('body',n);join('sill',n)
