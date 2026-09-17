"""Clothing Rack with Hanger.

Clothing rack with two posts, two rails and one suspended hanger. Centerline extremes (6,6)-(42,42). No useful local Lucide rack match. Hanger owns wide triangular shoulders; reduce the tight curved hook to a suspended neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a653f4e0-a9c5-58a4-a9d5-49a20ca85d84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dressing hanging rack_a653f4e0-a9c5-58a4-a9d5-49a20ca85d84.svg'
AUTHOR = 'gpt-6'

class ClothesRackSingleHanger(Solo48):
    icon_id = 'clothes-rack-single-hanger'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('clothing', 'rack', 'with', 'hanger')

    def build(self):
        # Symbol plan: Clothing rack with two posts, two rails and one suspended hanger. Centerline extremes (6,6)-(42,42). No useful local Lucide rack match. Hanger owns wide triangular shoulders; reduce the tight curved hook to a suspended neck.

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

        for x in (6,42):self.add_polyline(f'post-{x}',(x,6),(x,10),(x,38),(x,42))
        self.add_polyline('top',(6,10),(24,10),(42,10));line('bottom',(6,38),(42,38))
        for x in (6,42):join('top',f'post-{x}');join('bottom',f'post-{x}')
        line('hook',(24,10),(24,20));join('hook','top')
        self.add_polyline('hanger',(24,20),(34,29),(14,29),closed=True);join('hook','hanger')
