"""An upright memory card has a clipped upper-right corner and a small notch in its left edge. Three narrow vertical contact marks run down the upper face, with the right mark longer than the other two."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e2b62cc9-8f2f-4479-9033-728317bf6a36'
SOURCE_PATH = 'pictographic-primitives/mobile/sim card_e2b62cc9-8f2f-4479-9033-728317bf6a36.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'notched-memory-card'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('memory', 'card', 'contacts', 'storage', 'chip', 'notch', 'electronics')

    def build(self):
        # Lucide construction references: card-sim, memory-stick.
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
        # SQUARE extremes (6,6)-(42,42): one clipped card with an eight-unit notch.
        path('card',(10,6),[('L',(34,6)),('L',(42,14)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,34)),('L',(14,34)),('L',(14,26)),('L',(6,26)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.add_line('contact-left',(24,15),(24,23))
        self.add_line('contact-right',(33,18),(33,32))
