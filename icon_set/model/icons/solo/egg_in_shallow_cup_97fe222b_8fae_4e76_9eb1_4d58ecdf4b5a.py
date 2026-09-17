"""Egg in Egg Cup."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97fe222b-8fae-4e76-9eb1-4d58ecdf4b5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/egg_97fe222b-8fae-4e76-9eb1-4d58ecdf4b5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'egg-in-shallow-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('egg', 'egg cup', 'breakfast', 'cup', 'boiled egg', 'food', 'tableware')

    def build(self):
        # Plan: Upright pointed egg on shallow cup. Lucide egg mirrored curves; rear rim omitted and front rim simplified to a straight chord. Shared egg/cup endpoints. Envelope (8,4)-(40,44).
        self.add_bezier('egg',(8,28),((8,17),(18,4),(24,4)),((30,4),(40,17),(40,28)))
        self.add_line('rim',(8,28),(40,28))
        self.add_bezier('cup',(40,28),((40,39),(33,44),(24,44)),((15,44),(8,39),(8,28)))
        for a,b in (('egg','rim'),('egg','cup'),('rim','cup')):self.relate('connect',a,b)
