"""Pair of Summer Flip Flops.

Matching summer flip-flops with rounded rectangular soles and level V straps. Centerline extremes (4,8)-(44,40). One translated repeat owns all sole and strap geometry. Lucide footprints informs paired sole spacing. Squarer ends distinguish this pair from the round-toed version.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e77d0df7-fe4c-42de-adfc-3562c2a011f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/flip flops_e77d0df7-fe4c-42de-adfc-3562c2a011f5.svg'
AUTHOR = 'gpt-6'

class SummerFlipFlopsParallelStraps(Solo48):
    icon_id = 'summer-flip-flops-parallel-straps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('pair', 'of', 'summer', 'flip', 'flops')

    def build(self):
        # Symbol plan: Matching summer flip-flops with rounded rectangular soles and level V straps. Centerline extremes (4,8)-(44,40). One translated repeat owns all sole and strap geometry. Lucide footprints informs paired sole spacing. Squarer ends distinguish this pair from the round-toed version.

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
            path(f'sole-{i}',(x+6,8),[('L',(x+10,8)),('A',(x+16,14),6,6,True),('L',(x+16,26)),('L',(x+16,34)),('A',(x+10,40),6,6,True),('L',(x+6,40)),('A',(x,34),6,6,True),('L',(x,26)),('L',(x,14)),('A',(x+6,8),6,6,True)],True)
            self.add_polyline(f'strap-{i}',(x,26),(x+8,20),(x+16,26));join(f'strap-{i}',f'sole-{i}')
            line(f'post-{i}',(x+8,18),(x+8,20));join(f'post-{i}',f'strap-{i}')
