"""Two Long Biscuits.

Two repeated upright capsule biscuits with radius-six ends. Centerline extremes (6,6)-(42,42). Omit twin grooves: the width cannot support them with required clearance. No useful local Lucide biscuit match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41eb4d71-9a8e-5daf-8163-d05363fb7a8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear biscuits_41eb4d71-9a8e-5daf-8163-d05363fb7a8c.svg'
AUTHOR = 'gpt-6'

class TwoLongBiscuits(Solo48):
    icon_id = 'two-long-biscuits'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'long', 'biscuits')

    def build(self):
        # Symbol plan: Two repeated upright capsule biscuits with radius-six ends. Centerline extremes (6,6)-(42,42). Omit twin grooves: the width cannot support them with required clearance. No useful local Lucide biscuit match.

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

        for i,x in enumerate((12,36)):
            path(f'biscuit-{i}',(x-6,12),[('A',(x+6,12),6,6,True),('L',(x+6,36)),('A',(x-6,36),6,6,True),('L',(x-6,12))],True)
