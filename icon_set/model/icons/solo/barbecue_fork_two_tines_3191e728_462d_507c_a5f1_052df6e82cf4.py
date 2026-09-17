"""Two Pronged Barbecue Fork.

Diagonal fork with wide rounded grip, shaft, and open U-shaped two-tine head. Lucide utensils informs the open fork head and centered shaft; source diagonal is intentional. Centerline extremes (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3191e728-462d-507c-a5f1-052df6e82cf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue stick_3191e728-462d-507c-a5f1-052df6e82cf4.svg'
AUTHOR = 'gpt-6'

class BarbecueForkTwoTines(Solo48):
    icon_id = 'barbecue-fork-two-tines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'pronged', 'barbecue', 'fork')

    def build(self):
        # Symbol plan: Diagonal fork with wide rounded grip, shaft, and open U-shaped two-tine head. Lucide utensils informs the open fork head and centered shaft; source diagonal is intentional. Centerline extremes (6,6)-(42,42).

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

        path('grip',(8,32),[('L',(15,25)),('L',(19,29)),('L',(23,33)),('L',(16,40)),('C',(12,42),(15,41),(14,42)),('C',(6,36),(8,42),(6,40)),('C',(8,32),(6,34),(7,33))],True)
        line('shaft',(19,29),(28,20));join('grip','shaft')
        path('tines',(34,6),[('L',(26,14)),('C',(28,20),(23,17),(25,20)),('C',(34,18),(30,22),(32,20)),('L',(42,10))])
        join('shaft','tines')
