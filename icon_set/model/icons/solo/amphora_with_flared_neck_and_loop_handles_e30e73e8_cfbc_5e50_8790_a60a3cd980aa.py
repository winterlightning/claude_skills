from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e30e73e8-cfbc-5e50-8790-a60a3cd980aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/culture/batch-01/vase_e30e73e8-cfbc-5e50-8790-a60a3cd980aa.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'amphora-with-flared-neck-and-loop-handles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('amphora', 'vase', 'urn', 'ceramic', 'handles', 'pottery', 'vessel', 'culture')

    def build(self):
        # Plan: mirrored bulbous body with flared open neck and loop handles; foot closes contour.
        # Centerline envelope: (8,4)-(40,44). Reference: Lucide amphora: mirrored neck, body curves and attached handles.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        self.add_line('rim',(12,4),(36,4))
        path('neck-left',(12,4),(16,12),(16,20));path('neck-right',(36,4),(32,12),(32,20))
        for n in ('neck-left','neck-right'):join('rim',n)
        self.add_bezier('body-left',(16,20),((16,28),(12,28),(12,32)),((12,38),(20,40),(18,44)))
        self.add_bezier('body-right',(32,20),((32,28),(36,28),(36,32)),((36,38),(28,40),(30,44)))
        self.add_line('base',(18,44),(30,44))
        for side in ('left','right'):join('body-'+side,'neck-'+side);join('body-'+side,'base')
        path('handle-left',(16,12),(8,12),(8,20),(16,20))
        path('handle-right',(32,12),(40,12),(40,20),(32,20))
        for side in ('left','right'):join('handle-'+side,'neck-'+side);join('handle-'+side,'body-'+side)
