"""An upright SIM card has rounded lower corners and a clipped upper-right corner. A rounded rectangular contact area fills its lower half, with a small bent divider forming an upper-right contact section."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '30de259f-047f-5f24-9b36-ee0181354ff8'
SOURCE_PATH = 'pictographic-primitives/mobile/sim card_30de259f-047f-5f24-9b36-ee0181354ff8.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'sim-card-simple-contacts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
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
        # Contact pad owns two top/bottom rows and a bent upper-right division.
        self.add_polyline('pad',(15,17),(24,17),(33,17),(33,25),(33,33),(15,33),closed=True)
        self.add_polyline('division',(24,17),(24,25),(33,25))
        self.relate('connect','pad','division')
