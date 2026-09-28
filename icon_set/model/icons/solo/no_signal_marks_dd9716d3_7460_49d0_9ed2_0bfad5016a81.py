"""Four short horizontal strokes form an evenly spaced row. All four marks have the same height and length, creating a flat signal indicator with no raised bars."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd9716d3-7460-49d0-9ed2-0bfad5016a81'
SOURCE_PATH = 'pictographic-primitives/mobile/signal no_dd9716d3-7460-49d0-9ed2-0bfad5016a81.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'no-signal-marks'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('signal', 'none', 'bars', 'reception', 'cellular', 'network', 'disconnected')

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
        # CIRCLE radial envelope: endpoint distance 20 from (24,24), plus stroke radius 2.
        # Four equal length-4 marks, constant twelve-unit step; no vertical detail is invented.
        for i,x in enumerate((4,16,28,40)):
            self.add_line(f'empty-{i}',(x,24),(x+4,24))
