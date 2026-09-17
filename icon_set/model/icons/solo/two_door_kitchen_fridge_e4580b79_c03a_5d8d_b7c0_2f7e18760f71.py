"""Two Door Kitchen Refrigerator.

Upright rounded refrigerator split into two doors, paired left handles. Lucide refrigerator informs rounded housing and door split. Centerline extremes (8,4)-(40,44); preserve short feet in the second source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4580b79-c03a-5d8d-b7c0-2f7e18760f71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/appliances fridge_e4580b79-c03a-5d8d-b7c0-2f7e18760f71.svg'
AUTHOR = 'gpt-6'

class TwoDoorKitchenFridge(Solo48):
    icon_id = 'two-door-kitchen-fridge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'door', 'kitchen', 'refrigerator')

    def build(self):
        # Symbol plan: Upright rounded refrigerator split into two doors, paired left handles. Lucide refrigerator informs rounded housing and door split. Centerline extremes (8,4)-(40,44); preserve short feet in the second source.

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

        bottom=44
        path('housing',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,23)),('L',(40,bottom-4)),('A',(36,bottom),4,4,True),('L',(12,bottom)),('A',(8,bottom-4),4,4,True),('L',(8,23)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        line('divider',(8,23),(40,23));join('housing','divider')
        line('upper-handle',(18,13),(18,14))
        line('lower-handle',(18,32),(18,35))
