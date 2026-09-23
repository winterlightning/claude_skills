"""Square speech panel with lower-left tail and outlined medical cross.
Construction: Tail direction and outlined cross retained; no omissions.
Lucide construction reference: message-circle-plus; coherent arcs and independent enclosed content.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1'
SOURCE_PATH = 'icon_set/work/todo-references/chat medical cross left_5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chat-medical-cross-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('chat', 'medical', 'cross', 'left')

    def build(self):
        # Rounded speech enclosure, lower-left tail, and outlined medical cross.
        self.add_line('top', (10,6), (38,6))
        self.add_arc('tr', (38,6), (42,10), radius_x=4)
        self.add_line('right', (42,10), (42,34))
        self.add_arc('br', (42,34), (38,38), radius_x=4)
        tail = [(38,38),(18,38),(14,42),(14,38),(10,38)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1): self.add_line(f'tail-{i}',a,b)
        self.add_arc('bl', (10,38), (6,34), radius_x=4)
        self.add_line('left', (6,34), (6,10))
        self.add_arc('tl', (6,10), (10,6), radius_x=4)
        self.add_contour('bubble', 'top','tr','right','br', 'tail-1','tail-2','tail-3','tail-4','bl','left','tl', closed=True)
        cx, cy, outer, stem = 24, 22, 7, 4
        pts = [(-stem,-outer),(stem,-outer),(stem,-stem),(outer,-stem),(outer,stem),(stem,stem),(stem,outer),(-stem,outer),(-stem,stem),(-outer,stem),(-outer,-stem),(-stem,-stem)]
        self.add_polyline('medical-cross', *((cx+x,cy+y) for x,y in pts), closed=True)

