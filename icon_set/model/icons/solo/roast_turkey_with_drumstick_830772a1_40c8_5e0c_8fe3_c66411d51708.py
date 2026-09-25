"""Whole Roasted Turkey.

Whole roast turkey with a foreground drumstick and a projecting bone tip. Centerline extremes (4,8)-(44,40). Lucide drumstick informs the bulb and rounded bone tip; source placement and natural overlap retained. Omit tiny joint creases.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '830772a1-40c8-5e0c-8fe3-c66411d51708'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/turkey_830772a1-40c8-5e0c-8fe3-c66411d51708.svg'
AUTHOR = 'gpt-6'

class RoastTurkeyWithDrumstick(Solo48):
    icon_id = 'roast-turkey-with-drumstick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'roasted', 'turkey')

    def build(self):
        # Symbol plan: Whole roast turkey with a foreground drumstick and a projecting bone tip. Centerline extremes (4,8)-(44,40). Lucide drumstick informs the bulb and rounded bone tip; source placement and natural overlap retained. Omit tiny joint creases.

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
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(32,18),[('C',(22,12),(29,14),(26,12)),('C',(4,32),(12,12),(4,23)),('C',(12,40),(4,38),(8,40)),('L',(30,40)),('C',(40,32),(37,40),(40,38)),('C',(38,20),(40,28),(39,23))])
        path('drumstick',(32,18),[('C',(34,10),(31,14),(31,10)),('C',(38,8),(35,8),(37,8)),('C',(40,12),(40,8),(40,10)),('C',(44,15),(42,12),(44,12)),('C',(38,20),(44,19),(42,20)),('C',(26,30),(36,26),(34,30)),('C',(18,25),(21,30),(18,29)),('C',(32,18),(18,20),(27,19))],True)
        join('body','drumstick')
