"""The capital letters VPN stand together in one horizontal row. The V has a pointed lower junction, the P has a rounded upper bowl, and the N joins two uprights with a diagonal."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '018187c4-2d3b-507e-8e89-7dff566e58a3'
SOURCE_PATH = 'pictographic-primitives/mobile/vpn on_018187c4-2d3b-507e-8e89-7dff566e58a3.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'vpn-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('vpn', 'text', 'network', 'connection', 'privacy', 'letters', 'tunnel')

    def build(self):
        # Lucide construction references: none.
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
        # HRECT_L extremes (4,8)-(44,40): three eight-unit-wide letters separated by eight.
        self.add_polyline('v',(4,8),(8,40),(12,8))
        path('p-bowl',(20,24),[('L',(20,8)),('L',(24,8)),('A',(28,12),4,4,True),('L',(28,20)),('A',(24,24),4,4,True),('L',(20,24))],True)
        self.add_line('p-stem',(20,24),(20,40))
        self.relate('connect','p-bowl','p-stem')
        self.add_polyline('n',(36,40),(36,8),(44,40),(44,8))
