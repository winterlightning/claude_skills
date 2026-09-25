"""One short hollow vertical bar stands at the left of the signal display. Three separate horizontal strokes continue to its right along the same baseline, filling the remaining signal positions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82b05f42-01d8-4a41-8a4f-7a7e457484aa'
SOURCE_PATH = 'pictographic-primitives/mobile/signal very low_82b05f42-01d8-4a41-8a4f-7a7e457484aa.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'very-low-signal-bars'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('signal', 'very-low', 'bars', 'reception', 'cellular', 'network', 'strength')

    def build(self):
        # Lucide construction references: signal.
        # Typed contours keep shared radii and continuous joins together.
        def path(name,start,commands,closed=False):
            here, members = start, []
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L':
                    self.add_line(ident,here,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(ident)
                here=end
            self.add_contour(name,*members,closed=closed)
        # CIRCLE radial envelope: (8,12) and (44,24) are exactly radius 20 from center.
        # A short active rectangle and three empty positions retain the low-level silhouette.
        self.add_polyline('active',(8,12),(16,12),(16,24),(8,24),closed=True)
        for i,x in enumerate((24,34,44)):
            self.add_dot(f'empty-{i}',(x,24))
