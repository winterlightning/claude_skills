"""Continuous head, short neck and sloping shoulders with a smooth crown.
Symbol plan: shared parameters and coherent contours.
Construction: human_ref/user.svg and user-round: circular head and coherent shoulders.
Omissions: Tiny ripples in the source head edge removed at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='01aff74c-6e7d-4c53-9e84-005da220b852'
SOURCE_PATH='pictographic-primitives/symbol/sub square_01aff74c-6e7d-4c53-9e84-005da220b852.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-silhouette-wavy'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('person', 'silhouette', 'wavy')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Shared x24 axis and radius10 crown; intentional neck is part of the source silhouette.
        self.path('silhouette',(6,42),[('A',(8,38),5,5,True),('L',(20,29)),('L',(20,26)),('A',(14,17),10,10,True),('L',(14,16)),('A',(34,16),10,10,True),('L',(34,17)),('A',(28,26),10,10,True),('L',(28,29)),('L',(40,38)),('A',(42,42),5,5,True)])
