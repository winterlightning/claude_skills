"""Traditional Teapot with Lid.

Plan: Round teapot with domed lid, knob, curled left spout and broad right handle. Bounds (4,8)-(44,40). Lid reduced to an arched shoulder to keep knob separate.
Construction reference: Lucide coffee: handle and coherent body. Intentional left/right asymmetry preserves spout and handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8287521a-3079-4a79-bfd5-354b8067a810'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/tea pot_8287521a-3079-4a79-bfd5-354b8067a810.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-teapot-with-curved-spout-and-domed-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('traditional', 'teapot', 'with', 'lid')

    def build(self):
        path(self,'pot',(12,24),('A',10,8,True,(22,16)),('A',10,8,True,(32,24)),('L',(32,36)),('A',4,4,True,(28,40)),('L',(16,40)),('A',4,4,True,(12,36)),('L',(12,32)),('L',(12,24)),closed=True)
        path(self,'spout',(12,32),('A',8,8,True,(4,24)),('L',(4,20)))
        path(self,'handle',(32,24),('A',12,6,True,(44,30)),('A',12,6,True,(32,36)))
        self.add_dot('knob',(22,8))
        contacts(self)
