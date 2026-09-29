"""Restored opposing cuffs, a crossing thumb, interlocking hands and a house roof above.
Plan and comparison: The handshake was reduced to an X above a bowl-shaped outline.
Construction reference: handshake: crossing thumb and rounded finger joints; reference supplies house roof
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='490f19a8-c170-4914-bea1-18cbfb479033'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__real-estate-deal-shake/20260929T043142Z-thuan-mac/reference/real estate deal shake_490f19a8-c170-4914-bea1-18cbfb479033.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='real-estate-deal-shake'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Roof stands separately over two hands; their meeting seam identifies a handshake.
        self.add_polyline('roof',(4,19),(24,4),(44,19))
        self.box('cuff-left',5,25,11,38,1)
        self.box('cuff-right',37,25,43,38,1)
        self.path('left-hand',(11,28),[('L',(18,25)),('L',(23,26))])
        self.path('right-hand',(37,28),[('L',(29,24)),('A',(24,25),5,5,False),('L',(19,29)),('A',(24,31),4,4,False),('L',(27,29)),('L',(34,36)),('A',(30,40),3,3,True),('L',(26,36))])
        self.path('fingers',(11,36),[('L',(21,44)),('A',(25,42),3,3,False),('A',(30,40),3,3,False)])
        self.relate('connect','left-hand','cuff-left'); self.relate('connect','right-hand','cuff-right'); self.relate('connect','fingers','cuff-left'); self.relate('connect','right-hand','fingers')

Drawing.exception = {'reason': 'Interlocking hands necessarily meet and retain compact cuff/finger openings beneath the roof. The crossing thumb and the cuffs remain distinct at native size. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6e76a3fff8547739a5b2350c38c5d623cb9564be39600258a460cdc184e4064f'}
