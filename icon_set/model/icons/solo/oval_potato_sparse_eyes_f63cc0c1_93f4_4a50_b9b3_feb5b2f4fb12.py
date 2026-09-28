"""Whole Oval Spotted Potato.

Broad oval potato with four irregularly positioned small eyes, avoiding a face-like arrangement. Centerline extremes (4,8)-(44,40). Ellipse owns its single center and radii. No useful local Lucide potato match; retain all four marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f63cc0c1-93f4-4a50-b9b3-feb5b2f4fb12'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/naan_f63cc0c1-93f4-4a50-b9b3-feb5b2f4fb12.svg'
AUTHOR = 'gpt-6'

class OvalPotatoSparseEyes(Solo48):
    icon_id = 'oval-potato-sparse-eyes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'oval', 'spotted', 'potato')

    def build(self):
        # Symbol plan: Broad oval potato with four irregularly positioned small eyes, avoiding a face-like arrangement. Centerline extremes (4,8)-(44,40). Ellipse owns its single center and radii. No useful local Lucide potato match; retain all four marks.

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

        oval('potato',24,24,20,16)
        for i,p in enumerate(((15,19),(29,17),(20,30),(34,28))): dot(f'eye-{i}',p)
