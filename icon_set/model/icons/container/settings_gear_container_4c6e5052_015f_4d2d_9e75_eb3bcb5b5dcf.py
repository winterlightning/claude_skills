"""Mechanical Settings Gear: independently authored container.

Construction plan: Eight square-ended teeth on a single rotational outline; omit hub absent from the reference.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.svg. Lucide cog original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.svg'
AUTHOR = 'gpt-6'


class SettingsGearContainer(Container64):
    icon_id = 'settings-gear-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('settings', 'gear', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        quarter=[(26,2),(38,2),(38,10),(46,14),(52,8),(60,16),(54,22),(54,26),(62,26)]
        points=[]
        for k in range(4):
         for x,y in quarter[:-1]:
          for _ in range(k):x,y=64-y,x
          points.append((x,y))
        poly('gear',*points,closed=True)
