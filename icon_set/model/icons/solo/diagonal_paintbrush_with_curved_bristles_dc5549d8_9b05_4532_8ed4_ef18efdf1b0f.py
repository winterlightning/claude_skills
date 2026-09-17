from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc5549d8-9b05-4532-8ed4-ef18efdf1b0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-paintbrush-with-curved-bristles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('brush', 'paintbrush', 'bristles', 'handle', 'art', 'artist', 'painting', 'tool', 'sub icon')

    def build(self):
        # Plan: long rounded diagonal handle flows into a curved pointed bristle tuft.
        # Centerline extremes: (6,6)-(42,42). Construction: Lucide paintbrush: rounded handle and smooth coherent bristles.
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


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('a0a41169-49c3-4086-a686-b84d4a7eeb92', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_a0a41169-49c3-4086-a686-b84d4a7eeb92.svg')]
