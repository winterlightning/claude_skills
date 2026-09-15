"""A tall arched robot head holds a wide visor band with a zigzag pulse line, above a small trapezoid mouth.

Plan: Symmetric domed head, pulse visor and mouth on axis x24.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: bot: rounded head and minimal facial strokes.
Simplification: Visor boundary and trapezoid mouth reduce to pulse and mouth strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7004b716-3a3b-4f2a-8272-02ce97782981'
SOURCE_PATH = 'pictographic-primitives/logos/hubot logo_7004b716-3a3b-4f2a-8272-02ce97782981.svg'
AUTHOR = 'gpt-6'


class HubotLogo(Solo48):
    icon_id = 'hubot-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('hubot', 'github', 'robot', 'chatbot', 'logo', 'brand', 'automation')

    def build(self):
        self.add_line('left',(8,44),(8,20))
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_line('right',(40,20),(40,44))
        self.add_contour('head','left','dome','right')
        self.add_polyline('pulse',(17,24),(22,20),(26,28),(31,24))
        self.add_line('mouth',(19,38),(29,38))
