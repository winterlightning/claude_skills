"""Boot and Sewing Thread Spool.

Cobbler boot beside a separate upright thread spool. Centerline extremes (4,8)-(44,40). Boot has a broad cuff and curved left-facing toe; spool has two flanges and a single diagonal winding. No useful local Lucide scene match. Reduce two thread bands to one.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfbd280c-2436-42a3-81b4-a75064b8c37f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/clothes design thread boots_bfbd280c-2436-42a3-81b4-a75064b8c37f.svg'
AUTHOR = 'gpt-6'

class BootBesideSewingThreadSpool(Solo48):
    icon_id = 'boot-beside-sewing-thread-spool'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    categories = ('primitives', 'footwear')
    aliases = ()
    keywords = ('boot', 'and', 'sewing', 'thread', 'spool')

    def build(self):
        # Symbol plan: Cobbler boot beside a separate upright thread spool. Centerline extremes (4,8)-(44,40). Boot has a broad cuff and curved left-facing toe; spool has two flanges and a single diagonal winding. No useful local Lucide scene match. Reduce two thread bands to one.

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

        path('boot',(12,8),[('L',(26,8)),('L',(26,16)),('L',(26,32)),('L',(26,40)),('L',(12,40)),('C',(4,32),(7,40),(4,37)),('C',(12,24),(4,27),(7,24)),('L',(16,24)),('L',(16,16)),('L',(12,16)),('L',(12,8))],True)
        line('cuff',(16,16),(26,16));join('cuff','boot')
        path('spool',(34,20),[('L',(44,20)),('L',(44,28)),('L',(44,40)),('L',(34,40)),('L',(34,32)),('L',(34,20))],True)
        line('thread',(34,32),(44,28));join('thread','spool')
