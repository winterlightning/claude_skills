"""Wind Gusts: Two horizontal wind strokes extend from the left and curl into rounded hooks at the right. The upper hook turns upward and the shorter lower hook turns downward.

Construction: Two horizontal gusts have tangent semicircular hooks curling in opposite vertical directions.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22ebeb63-e3c2-4cdd-a779-46135c16e412'
SOURCE_PATH = 'pictographic-primitives/state/wind_22ebeb63-e3c2-4cdd-a779-46135c16e412.svg'
AUTHOR = 'gpt-6'


class WindGustsSub(Sub32):
    icon_id = 'wind-gusts-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('wind', 'gusts', 'horizontal', 'strokes', 'extend', 'left', 'curl', 'rounded')

    def build(self):
        self.add_arc("upper-hook",(18,8),(30,8),radius_x=6)
        self.add_arc("upper-return",(30,8),(24,14),radius_x=6)
        self.add_line("upper-run",(24,14),(2,14))
        self.add_contour("upper","upper-hook","upper-return","upper-run")
        self.add_line("lower-run",(2,22),(16,22))
        self.add_arc("lower-hook",(16,22),(16,30),radius_x=4)
        self.add_arc("lower-return",(16,30),(12,26),radius_x=4)
        self.add_contour("lower","lower-run","lower-hook","lower-return")
