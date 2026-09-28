"""A rounded rectangular speech bubble with a tail at its lower left, its outline broken into two arrows: a downward arrow on the left side and an upward arrow on the right, circling the bubble anticlockwise."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e75641a-fc1e-57a5-be43-63afa022d2b8'
SOURCE_PATH = 'pictographic-primitives/messages/discussion converstion_7e75641a-fc1e-57a5-be43-63afa022d2b8.svg'
AUTHOR = 'gpt-6'

class MessageIcon(Solo48):
    icon_id = 'speech-bubble-cycle-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/messages'
    aliases = ()
    keywords = ('conversation', 'discussion', 'speech-bubble', 'arrows', 'exchange', 'chat', 'message')

    def build(self):
        # Lucide original and atomic-debug references: message-square, refresh-ccw.
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
        # HRECT_L extremes (4,8)-(44,40): two open perimeter strokes and two attached arrowheads.
        # Down on the left, up on the right. Arrow tips are shared contour endpoints.
        down_tip,up_tip=(12,28),(36,16)
        path('upper-outline',(32,8),[('L',(20,8)),('A',(12,16),radius,radius,False),('L',down_tip)])
        path('lower-outline',(12,38),[('L',(12,40)),('L',(24,36)),('L',(28,36)),('A',(36,28),radius,radius,False),('L',up_tip)])
        wing = 8
        self.add_polyline('down-head',(down_tip[0]-wing,down_tip[1]-wing),down_tip,(down_tip[0]+wing,down_tip[1]-wing))
        self.add_polyline('up-head',(up_tip[0]-wing,up_tip[1]+wing),up_tip,(up_tip[0]+wing,up_tip[1]+wing))
        self.relate('connect','upper-outline','down-head')
        self.relate('connect','lower-outline','up-head')
