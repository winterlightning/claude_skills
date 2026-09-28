"""Three hollow rounded signal bars increase in height from left to right. A long straight baseline sits separately beneath the entire group, spanning beyond the bars at both ends."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '392880c4-0c53-4ee9-afa4-2a1497184c09'
SOURCE_PATH = 'pictographic-primitives/mobile/signal strong_392880c4-0c53-4ee9-afa4-2a1497184c09.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'strong-signal-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('signal', 'strong', 'bars', 'reception', 'cellular', 'network', 'strength')

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
        # HRECT_L extremes (4,8)-(44,40): repeated width-8 bars, shared y=32 bottom.
        for i,(x,top) in enumerate(((4,24),(20,16),(36,8))):
            self.add_polyline(f'bar-{i}',(x,top),(x+8,top),(x+8,32),(x,32),closed=True)
        self.add_line('baseline',(4,40),(44,40))
