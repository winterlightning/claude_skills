"""Three hollow rounded bars rise successively from left to right on a shared baseline. One short horizontal mark follows the tallest bar at the right end of the signal display."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5cf163d0-ea07-49c6-b6de-99176209dee6'
SOURCE_PATH = 'pictographic-primitives/mobile/signal medium_5cf163d0-ea07-49c6-b6de-99176209dee6.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'medium-signal-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('signal', 'medium', 'bars', 'reception', 'cellular', 'network', 'strength')

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
        # HRECT_L extremes (4,8)-(44,40): three growing bars, one empty slot.
        for i,(x,top) in enumerate(((4,24),(16,16),(28,8))):
            self.add_line(f'active-{i}',(x,top),(x,40))
        self.add_line('empty',(40,40),(44,40))
