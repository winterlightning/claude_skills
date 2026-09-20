"""Selection handles.

Construction reference: scan.
Retains all four selection handles and their open holes.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'b3e89b9b-9e2a-4dfb-a61c-7a848b37675a'
SOURCE_PATH = 'pictographic-primitives/container/square block_b3e89b9b-9e2a-4dfb-a61c-7a848b37675a.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'selection-handles-solo-b3e89b9b'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('selection-handles',)
    keywords = ('selection', 'handles')

    def build(self):
        # Four matching 8-unit handles; frame joins their edge midpoints.
        for x in (6,34):
            for y in (6,34):
                box(self,f'handle-{x}-{y}',x,y,x+8,y+8,2,nodes=((x+4,y),(x+4,y+8),(x,y+4),(x+8,y+4)))
        for name,a,b,h1,h2 in (
            ('top',(14,10),(34,10),'handle-6-6','handle-34-6'),
            ('bottom',(14,38),(34,38),'handle-6-34','handle-34-34'),
            ('left',(10,14),(10,34),'handle-6-6','handle-6-34'),
            ('right',(38,14),(38,34),'handle-34-6','handle-34-34')):
            self.add_line(name,a,b)
            self.relate('connect',name,h1)
            self.relate('connect',name,h2)
