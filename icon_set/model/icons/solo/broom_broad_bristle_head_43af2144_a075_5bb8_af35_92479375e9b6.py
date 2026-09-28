"""Cleaning Broom Brush.

Upright cleaning broom with long handle, rounded broad collar and flared separated bristle ends. Centerline extremes (8,4)-(40,44). No useful local broom match. Reduce fine pointed bristles to four clear divisions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43af2144-a075-5bb8-af35-92479375e9b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/floor mop dry_43af2144-a075-5bb8-af35-92479375e9b6.svg'
AUTHOR = 'gpt-6'

class BroomBroadBristleHead(Solo48):
    icon_id = 'broom-broad-bristle-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('cleaning', 'broom', 'brush')

    def build(self):
        # Symbol plan: Upright cleaning broom with long handle, rounded broad collar and flared separated bristle ends. Centerline extremes (8,4)-(40,44). No useful local broom match. Reduce fine pointed bristles to four clear divisions.

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

        line('handle',(24,4),(24,20))
        bilateral('head',(24,20),[('C',(34,28),(31,20),(34,23)),('L',(40,44))],False);join('handle','head')
        line('collar',(14,28),(34,28));join('collar','head')
        for i,x in enumerate((20,28)):line(f'bristle-{i}',(x,36),(x,44))
