"""Wrapped Candy Sweet.

Horizontally wrapped candy with a broad central sweet and two triangular flared ends. Centerline extremes (4,10)-(44,38). Mirrored wrapper wings share the central body seam endpoints. Lucide candy informs integrated wrapper topology; omit decorative stripes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65190295-301f-48c4-9b55-daa2e73e7886'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/candy_65190295-301f-48c4-9b55-daa2e73e7886.svg'
AUTHOR = 'gpt-6'

class WrappedCandyPointedEnds(Solo48):
    icon_id = 'wrapped-candy-pointed-ends'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('wrapped', 'candy', 'sweet')

    def build(self):
        # Symbol plan: Horizontally wrapped candy with a broad central sweet and two triangular flared ends. Centerline extremes (4,10)-(44,38). Mirrored wrapper wings share the central body seam endpoints. Lucide candy informs integrated wrapper topology; omit decorative stripes.

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

        path('wrapper',(14,18),[('C',(24,10),(15,12),(19,10)),('C',(34,18),(29,10),(33,12)),('L',(44,10)),('L',(44,38)),('L',(34,30)),('C',(24,38),(33,36),(29,38)),('C',(14,30),(19,38),(15,36)),('L',(4,38)),('L',(4,10)),('L',(14,18))],True)
        for x in (14,34): line(f'seam-{x}',(x,18),(x,30));join(f'seam-{x}','wrapper')
