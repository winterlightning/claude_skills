"""Password Characters: Two X-shaped password marks appear beside a short low underscore, arranged horizontally from left to right. Generate this component alone; exclude Capsule Frame.

Construction: Two small X marks are followed by a lower underscore, preserving all three source characters.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b9ace82f-9c93-4337-ac44-7380ce0657f4'
SOURCE_PATH = 'pictographic-primitives/state/password_b9ace82f-9c93-4337-ac44-7380ce0657f4.svg'
AUTHOR = 'gpt-6'


class PasswordCharacters(Sub32):
    icon_id = 'password-characters'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('password', 'characters', 'x', 'shaped', 'marks', 'appear', 'beside', 'short')

    def build(self):
        for i,x in enumerate((2,14)):
            self.add_line(f'down-{i}',(x,10),(x+6,16))
            self.add_line(f'up-{i}',(x,16),(x+6,10))
            self.relate('connect',f'down-{i}',f'up-{i}')
        self.add_line('underscore',(26,22),(30,22))
