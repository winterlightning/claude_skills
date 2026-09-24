"""Crowned chess queen with rounded crown tips, narrow stem and rounded broad pedestal. Retain the crown silhouette and rounded base; omit the tiny top loop and collar to preserve spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ec83c77-fb81-4fbb-9d48-20b45ebca8b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='crowned-chess-queen-batch-013-05'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/batch-subjects"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Crowned chess queen with rounded crown tips, narrow stem and rounded broad pedestal. Retain the crown silhouette and rounded base; omit the tiny top loop and collar to preserve spacing.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        path('crown',(16,20),[('L',(8,9)),('C',(13,6),(8,5),(10,3)),('L',(18,10)),('L',(24,4)),('L',(30,10)),('L',(35,6)),('C',(40,9),(38,3),(40,5)),('L',(32,20)),('L',(28,20)),('L',(20,20)),('L',(16,20))],True)
        self.add_polyline('stem',(20,20),(20,28),(16,36),(32,36),(28,28),(28,20));join('stem','crown')
        path('base',(16,36),[('L',(12,36)),('A',(8,40),4,4,False),('L',(8,44)),('L',(40,44)),('L',(40,40)),('A',(36,36),4,4,False),('L',(32,36))]);join('stem','base')
