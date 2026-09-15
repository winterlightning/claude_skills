"""A rounded rectangular speech bubble with a tail at its lower left. Its top edge breaks near the left, where a left-pointing arrowhead turns the outline back toward the upper-left corner."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4bea84d2-e574-5f4d-ab3c-3cd97efde30d'
SOURCE_PATH = 'pictographic-primitives/messages/reply to message_4bea84d2-e574-5f4d-ab3c-3cd97efde30d.svg'
AUTHOR = 'gpt-6'

class MessageIcon(Solo48):
    icon_id = 'reply-message-bubble-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/messages'
    aliases = ()
    keywords = ('reply', 'message', 'speech-bubble', 'arrow', 'respond', 'chat', 'conversation')

    def build(self):
        # Lucide original and atomic-debug references: message-square, reply.
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
        # HRECT_L extremes (4,8)-(44,40): rounded bubble perimeter with an integrated reply arrow.
        # The two right radius-8 arcs join tangentially at (44,24); arrow tip is a shared node.
        tip=(24,16)
        path('outline',(12,16),[('A',(4,24),radius,radius,False),('L',(4,40)),('L',(16,32)),('L',(36,32)),('A',(44,24),radius,radius,False),('A',(36,16),radius,radius,False),('L',tip)])
        wing = 8
        self.add_polyline('reply-head',(tip[0]+wing,tip[1]-wing),tip,(tip[0]+wing,tip[1]+wing))
        self.relate('connect','outline','reply-head')
