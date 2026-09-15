"""A rounded rectangular speech bubble with an empty interior and a short pointed tail dropping from the left part of its lower edge."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ec44a85-5b3f-5f95-b630-3349aed9481f'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square_3ec44a85-5b3f-5f95-b630-3349aed9481f.svg'
AUTHOR = 'gpt-6'

class MessageIcon(Solo48):
    icon_id = 'square-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/messages'
    aliases = ()
    keywords = ('speech-bubble', 'message', 'chat', 'comment', 'conversation', 'talk', 'empty')

    def build(self):
        # Lucide original and atomic-debug references: message-square.
        # Contours own continuous strokes; corner radii and attachment points are shared.
        def path(name,start,commands,closed=False):
            here,members=start,[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L':self.add_line(ident,here,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end
                members.append(ident)
            self.add_contour(name,*members,closed=closed)
        radius = 8
        # HRECT_L extremes (4,8)-(44,40). Radius-8 upper and right corners, broad left tail.
        # A standalone message noun: no hosted glyph or composition anchor.
        path('bubble',(12,8),[('L',(36,8)),('A',(44,16),radius,radius,True),('L',(44,24)),('A',(36,32),radius,radius,True),('L',(16,32)),('L',(4,40)),('L',(4,16)),('A',(12,8),radius,radius,True)],True)
