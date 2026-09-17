"""Hanging Tea Kettle over Fire.

Kettle hanging from a top hook over a three-point fire. Centerline extremes (8,4)-(40,44). Lucide flame informs restrained fire tips; no kettle match. Attach the suspension directly to the rounded pot, omitting its doubled handle; simplify the flame to one open three-point contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '393cfd34-b632-5baa-972a-08dafd496c7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/asian interior boiler_393cfd34-b632-5baa-972a-08dafd496c7f.svg'
AUTHOR = 'gpt-6'

class KettleHangingOverFire(Solo48):
    icon_id = 'kettle-hanging-over-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('hanging', 'tea', 'kettle', 'over', 'fire')

    def build(self):
        # Symbol plan: Kettle hanging from a top hook over a three-point fire. Centerline extremes (8,4)-(40,44). Lucide flame informs restrained fire tips; no kettle match. Attach the suspension directly to the rounded pot, omitting its doubled handle; simplify the flame to one open three-point contour.

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

        line('hook',(24,4),(24,12))
        path('kettle',(24,12),[('C',(32,16),(29,12),(32,14)),('L',(40,12)),('L',(38,24)),('C',(24,30),(36,30),(31,30)),('C',(8,22),(13,30),(8,28)),('C',(24,12),(8,16),(14,12))],True);join('hook','kettle')
        self.add_polyline('fire',(10,44),(12,38),(18,44),(24,38),(30,44),(36,38),(38,44))
