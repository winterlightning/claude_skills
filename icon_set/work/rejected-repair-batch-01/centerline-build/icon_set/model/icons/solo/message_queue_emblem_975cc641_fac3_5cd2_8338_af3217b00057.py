"""A circular queue loop connects to a pinched central message block. Edge ring nodes become simple junctions; pinched message silhouette is retained. Lucide workflow informs explicit node connections.
Fresh SOLO48 geometry. Keyshape CIRCLE; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '975cc641-fac3-5cd2-8338-af3217b00057'
SOURCE_PATH = 'pictographic-primitives/programing/amazon simple queue service_975cc641-fac3-5cd2-8338-af3217b00057.svg'
AUTHOR = 'gpt-6'

class MessageQueueEmblem(Solo48):
    icon_id = 'message-queue-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/programming"
    aliases = ()
    keywords = ('queue', 'message', 'service', 'emblem', 'circle', 'nodes', 'messaging', 'cloud')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        circle('queue-loop',24,24,20)
        self.add_polyline('message',(18,18),(24,20),(30,18),(28,24),(30,30),(24,28),(18,30),(20,24),closed=True)
        self.add_line('input',(4,24),(20,24))
        self.add_line('output',(28,24),(44,24))
        for line in ('input','output'):
            self.relate('connect',line,'queue-loop')
            self.relate('connect',line,'message')
