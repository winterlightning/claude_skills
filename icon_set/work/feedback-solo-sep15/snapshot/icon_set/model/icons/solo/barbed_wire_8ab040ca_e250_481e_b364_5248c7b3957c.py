"""A wire has repeated crossed barbs. No useful local Lucide match; use equal repeated crossings. Reduce three barbs to two, retaining visible spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ab040ca-e250-481e-b364-5248c7b3957c'
SOURCE_PATH = 'pictographic-primitives/protection/protest barb wire_8ab040ca-e250-481e-b364-5248c7b3957c.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'barbed-wire'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('barbed wire', 'fence', 'wire', 'barrier', 'border', 'prison', 'protest', 'security')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Wire owns two repeated crossed barbs; every contact shares its node.
        self.add_polyline('wire',(4,24),(14,24),(34,24),(44,24))
        for i,x in enumerate((14,34)):
            for j,dx in enumerate((-6,6)):
                name=f'barb-{i}-{j}'
                self.add_polyline(name,(x+dx,8),(x,24),(x-dx,40))
                self.relate('connect',name,'wire')
            self.relate('connect',f'barb-{i}-0',f'barb-{i}-1')
