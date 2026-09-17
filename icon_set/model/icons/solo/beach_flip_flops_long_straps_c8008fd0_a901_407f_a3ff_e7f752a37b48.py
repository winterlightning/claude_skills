"""Pair of Beach Flip Flops.

Pair of beach flip-flops with long slanted V straps and tapered lower soles. Centerline extremes (4,8)-(44,40). One sole and strap definition repeated at x offsets 0 and 24. Lucide footprints informs independent paired soles. Retain toe posts; lengthen straps relative to the other pairs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8008fd0-a901-407f-a3ff-e7f752a37b48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/flip flops_c8008fd0-a901-407f-a3ff-e7f752a37b48.svg'
AUTHOR = 'gpt-6'

class BeachFlipFlopsLongStraps(Solo48):
    icon_id = 'beach-flip-flops-long-straps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('pair', 'of', 'beach', 'flip', 'flops')

    def build(self):
        # Symbol plan: Pair of beach flip-flops with long slanted V straps and tapered lower soles. Centerline extremes (4,8)-(44,40). One sole and strap definition repeated at x offsets 0 and 24. Lucide footprints informs independent paired soles. Retain toe posts; lengthen straps relative to the other pairs.

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

        for i,x in enumerate((4,28)):
            path(f'sole-{i}',(x+8,8),[('C',(x+16,18),(x+14,8),(x+16,12)),('L',(x+16,28)),('C',(x+8,40),(x+16,37),(x+14,40)),('C',(x,28),(x+2,40),(x,37)),('L',(x,18)),('C',(x+8,8),(x,12),(x+2,8))],True)
            self.add_polyline(f'strap-{i}',(x,28),(x+8,20),(x+16,28));join(f'strap-{i}',f'sole-{i}')
            line(f'post-{i}',(x+8,18),(x+8,20));join(f'post-{i}',f'strap-{i}')
