"""Square Smart Watch: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = '9f86506b-13e1-43a2-99f9-4709e9b04ba0'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_9f86506b-13e1-43a2-99f9-4709e9b04ba0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'square-smart-watch-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('Square Smart Watch',)
    keywords = ('square', 'smart', 'watch')
    def build(self):
        # Same inspected face and straps as source 01277467: reuse one design.
        from .square_smartwatch_device_solo_01277467_c196_5c69_bba7_5182a13ec0bd import Drawing as FrontWatch
        FrontWatch.build(self)
