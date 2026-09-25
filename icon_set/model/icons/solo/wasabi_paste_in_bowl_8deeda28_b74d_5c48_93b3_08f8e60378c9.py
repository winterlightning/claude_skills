"""Wasabi Paste in Small Bowl.

Shallow bowl and a folded paste mound with one expressive peak. Centerline extremes (4,8)-(44,40). Source physical serving relationship is intrinsic, not an icon hosted by a frame. No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8deeda28-b74d-5c48-93b3-08f8e60378c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/wasabi paste_8deeda28-b74d-5c48-93b3-08f8e60378c9.svg'
AUTHOR = 'gpt-6'

class WasabiPasteInBowl(Solo48):
    icon_id = 'wasabi-paste-in-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('wasabi', 'paste', 'in', 'small', 'bowl')

    def build(self):
        # Symbol plan: Shallow bowl and a folded paste mound with one expressive peak. Centerline extremes (4,8)-(44,40). Source physical serving relationship is intrinsic, not an icon hosted by a frame. No useful local Lucide match.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        path('bowl',(4,28),[('L',(9,28)),('L',(39,28)),('L',(44,28)),('C',(32,40),(44,35),(40,40)),('L',(16,40)),('C',(4,28),(8,40),(4,35))],True)
        path('paste',(9,28),[('C',(22,8),(10,18),(28,19)),('C',(32,19),(32,10),(35,15)),('C',(39,28),(36,20),(39,24))]);join('paste','bowl')
