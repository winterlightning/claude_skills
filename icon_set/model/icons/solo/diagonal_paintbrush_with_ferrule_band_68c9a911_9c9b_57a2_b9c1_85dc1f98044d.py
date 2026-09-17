from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68c9a911-9c9b-57a2-b9c1-85dc1f98044d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color brush_68c9a911-9c9b-57a2-b9c1-85dc1f98044d.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'diagonal-paintbrush-with-ferrule-band'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('brush', 'paintbrush', 'paint', 'artist', 'handle', 'bristles', 'ferrule', 'tool')

    def build(self):
        # Plan: diagonal brush with shared handle width, broad curved tuft and two ferrule edges.
        # Centerline extremes: (6,6)-(42,42). Construction: Lucide paintbrush: coherent curved bristles and rounded handle.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        self.add_line('handle-upper',(20,22),(36,6))
        self.add_arc('handle-tip',(36,6),(42,12),radius_x=6)
        self.add_line('handle-lower',(42,12),(26,28))
        self.add_bezier('bristles-lower',(26,28),((32,38),(22,42),(6,42)))
        self.add_bezier('bristles-upper',(6,42),((14,34),(10,18),(20,22)))
        self.add_contour('outline','handle-upper','handle-tip','handle-lower','bristles-lower','bristles-upper',closed=True)
        self.add_line('joint',(20,22),(26,28));join('joint','outline')

        self.add_line('ferrule',(28,14),(34,20));join('ferrule','outline')
