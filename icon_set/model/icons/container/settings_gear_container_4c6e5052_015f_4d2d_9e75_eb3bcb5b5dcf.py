"""Mechanical Settings Gear: independently authored container.

Construction plan: Eight square-ended teeth on a single rotational outline; omit hub absent from the reference.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.svg. Lucide cog original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (settings-gear-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: v1 gear scaled uniformly by 52/60 about the centre, symmetric rounding.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.svg'
AUTHOR = 'claude-opus-5-5'


class SettingsGearContainer(Container64):
    icon_id = 'settings-gear-container'
    keyshape = Keyshape.SQUARE
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('settings', 'gear', 'container')

    def build(self) -> None:
        self.add_line('gear-1', (27, 6), (37, 6))
        self.add_line('gear-2', (37, 6), (37, 13))
        self.add_line('gear-3', (37, 13), (44, 16))
        self.add_line('gear-4', (44, 16), (49, 11))
        self.add_line('gear-5', (49, 11), (56, 18))
        self.add_line('gear-6', (56, 18), (51, 23))
        self.add_line('gear-7', (51, 23), (51, 27))
        self.add_line('gear-8', (51, 27), (58, 27))
        self.add_line('gear-9', (58, 27), (58, 37))
        self.add_line('gear-10', (58, 37), (51, 37))
        self.add_line('gear-11', (51, 37), (48, 44))
        self.add_line('gear-12', (48, 44), (53, 49))
        self.add_line('gear-13', (53, 49), (46, 56))
        self.add_line('gear-14', (46, 56), (41, 51))
        self.add_line('gear-15', (41, 51), (37, 51))
        self.add_line('gear-16', (37, 51), (37, 58))
        self.add_line('gear-17', (37, 58), (27, 58))
        self.add_line('gear-18', (27, 58), (27, 51))
        self.add_line('gear-19', (27, 51), (20, 48))
        self.add_line('gear-20', (20, 48), (15, 53))
        self.add_line('gear-21', (15, 53), (8, 46))
        self.add_line('gear-22', (8, 46), (13, 41))
        self.add_line('gear-23', (13, 41), (13, 37))
        self.add_line('gear-24', (13, 37), (6, 37))
        self.add_line('gear-25', (6, 37), (6, 27))
        self.add_line('gear-26', (6, 27), (13, 27))
        self.add_line('gear-27', (13, 27), (16, 20))
        self.add_line('gear-28', (16, 20), (11, 15))
        self.add_line('gear-29', (11, 15), (18, 8))
        self.add_line('gear-30', (18, 8), (23, 13))
        self.add_line('gear-31', (23, 13), (27, 13))
        self.add_line('gear-32', (27, 13), (27, 6))
        self.add_contour('gear', 'gear-1', 'gear-2', 'gear-3', 'gear-4', 'gear-5', 'gear-6', 'gear-7', 'gear-8', 'gear-9', 'gear-10', 'gear-11', 'gear-12', 'gear-13', 'gear-14', 'gear-15', 'gear-16', 'gear-17', 'gear-18', 'gear-19', 'gear-20', 'gear-21', 'gear-22', 'gear-23', 'gear-24', 'gear-25', 'gear-26', 'gear-27', 'gear-28', 'gear-29', 'gear-30', 'gear-31', 'gear-32', closed=True)
