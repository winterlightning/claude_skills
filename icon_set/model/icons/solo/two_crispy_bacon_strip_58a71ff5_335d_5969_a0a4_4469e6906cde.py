"""Two Crispy Bacon Strips.

Two identical wavy strip outlines spaced by a 24-unit horizontal repeat. Centerline extremes (6,6)-(42,42). Omit fat stripes because each strip cannot contain another 8-unit clearance band; no useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58a71ff5-335d-5969-a0a4-4469e6906cde'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/meat bacon_58a71ff5-335d-5969-a0a4-4469e6906cde.svg'
AUTHOR = 'gpt-6'

class TwoCrispyBaconStrip(Solo48):
    icon_id = 'two-crispy-bacon-strip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('two', 'crispy', 'bacon', 'strips')

    def build(self):
        # Symbol plan: Two identical wavy strip outlines spaced by a 24-unit horizontal repeat. Centerline extremes (6,6)-(42,42). Omit fat stripes because each strip cannot contain another 8-unit clearance band; no useful local Lucide match.

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

        for i,x in enumerate((6,30)):
            path(f'bacon-{i}',(x+2,6),[('L',(x+12,6)),('C',(x+10,15),(x+12,9),(x+10,12)),('C',(x+12,24),(x+10,18),(x+12,21)),('C',(x+10,33),(x+12,27),(x+10,30)),('C',(x+12,42),(x+10,36),(x+12,39)),('L',(x+2,42)),('C',(x,33),(x+2,39),(x,36)),('C',(x+2,24),(x,30),(x+2,27)),('C',(x,15),(x+2,21),(x,18)),('C',(x+2,6),(x,12),(x+2,9))],True)
