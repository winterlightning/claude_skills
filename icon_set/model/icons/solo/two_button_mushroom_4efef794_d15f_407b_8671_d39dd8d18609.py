"""Two Button Mushrooms.

Two repeated domed caps and short stems, axis of each x=12/36; centerline extremes (4,10)-(44,38). Stagger the pair diagonally to preserve broad caps and short stems. Drop overlap; no useful Lucide mushroom match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4efef794-d15f-407b-8671-d39dd8d18609'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom white button_4efef794-d15f-407b-8671-d39dd8d18609.svg'
AUTHOR = 'gpt-6'

class TwoButtonMushroom(Solo48):
    icon_id = 'two-button-mushroom'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('two', 'button', 'mushrooms')

    def build(self):
        # Symbol plan: Two repeated domed caps and short stems, axis of each x=12/36; centerline extremes (4,10)-(44,38). Stagger the pair diagonally to preserve broad caps and short stems. Drop overlap; no useful Lucide mushroom match.

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
            n=f'mushroom-{i}'
            y=20+i*8
            path(n,(x-8,y),[('A',(x+8,y),8,10,True),('L',(x+4,y)),('L',(x+4,y+6)),('A',(x-4,y+6),4,4,True),('L',(x-4,y)),('L',(x-8,y))],True)
            line(n+'-rim',(x-4,y),(x+4,y));join(n,n+'-rim')
