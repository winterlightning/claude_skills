"""Classic Table Lamp.

Table lamp with tapered shade, central stem and shallow rounded base. Centerline extremes (8,4)-(40,44). Lucide lamp informs three attached shapes and rounded corners. Mirror the shade; retain the outlined base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5cdbe01-e2ae-5da4-a2bc-c8e4793ac02f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/console lamp.png_f5cdbe01-e2ae-5da4-a2bc-c8e4793ac02f.svg'
AUTHOR = 'gpt-6'

class TableLampTaperedShade(Solo48):
    icon_id = 'table-lamp-tapered-shade'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('classic', 'table', 'lamp')

    def build(self):
        # Symbol plan: Table lamp with tapered shade, central stem and shallow rounded base. Centerline extremes (8,4)-(40,44). Lucide lamp informs three attached shapes and rounded corners. Mirror the shade; retain the outlined base.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
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

        bilateral('shade',(24,4),[('L',(30,4)),('C',(33,7),(32,4),(32,4)),('L',(40,24)),('C',(36,28),(40,27),(39,28)),('L',(24,28))])
        line('stem',(24,28),(24,36));join('stem','shade')
        path('base',(24,36),[('L',(30,36)),('A',(34,40),4,4,True),('L',(34,44)),('L',(14,44)),('L',(14,40)),('A',(18,36),4,4,True),('L',(24,36))],True);join('stem','base')
