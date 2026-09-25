"""An upright SIM card has a clipped upper-right corner and a rounded rectangular contact area in its lower half. Several horizontal and vertical divisions create an asymmetrical grid of contact pads."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb6cd85a-0a60-5c24-a1f8-ce3716f05ed1'
SOURCE_PATH = 'pictographic-primitives/mobile/sim card_cb6cd85a-0a60-5c24-a1f8-ce3716f05ed1.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'sim-card-contact-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('sim', 'card', 'chip', 'contacts', 'cellular', 'mobile', 'network')

    def build(self):
        # Lucide construction references: card-sim.
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
        # SQUARE extremes (6,6)-(42,42); shared radius-4 corners, clipped upper right.
        path('card',(10,6),[('L',(34,6)),('L',(42,14)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        # Four-pad contact grid: common row, staggered vertical sections with 8+ widths.
        self.add_polyline('pad',(15,17),(23,17),(33,17),(33,25),(33,33),(25,33),(15,33),(15,25),closed=True)
        self.add_polyline('row',(15,25),(23,25),(25,25),(33,25))
        self.add_line('upper-column',(23,17),(23,25))
        self.add_line('lower-column',(25,25),(25,33))
        for member in ('row','upper-column','lower-column'):
            self.relate('connect','pad',member)
        self.relate('connect','row','upper-column')
        self.relate('connect','row','lower-column')
