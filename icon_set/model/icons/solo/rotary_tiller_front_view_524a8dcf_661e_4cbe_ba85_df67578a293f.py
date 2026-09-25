"""Rotary Tiller Cultivator.
Plan: Mirrored tiller with wide handlebars, control box, two wheels and twin rotor blades. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Wheel thickness and extra control seams omitted; bilateral machine structure retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '524a8dcf-661e-4cbe-ba85-df67578a293f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/rottary tiller_524a8dcf-661e-4cbe-ba85-df67578a293f.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'rotary-tiller-front-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('rotary', 'tiller', 'cultivator')

    def build(self):

        self.add_polyline('control',(18,6),(30,6),(30,14),(24,14),(18,14),(18,6))
        self.add_polyline('handles',(6,16),(6,6),(18,6))
        self.add_polyline('handles-right',(30,6),(42,6),(42,16))
        for n in ('handles','handles-right'):self.relate('connect','control',n)
        self.add_polyline('body',(16,30),(16,22),(24,14),(32,22),(32,30));self.relate('connect','body','control')
        for i,x in enumerate((6,42)):self.add_line(f'wheel-{i}',(x,26),(x,36))
        self.add_polyline('rotor',(14,38),(18,38),(30,38),(34,38))
        for i,x in enumerate((18,30)):
            self.add_line(f'blade-{i}',(x,38),(x-3,42));self.relate('connect','rotor',f'blade-{i}')
