"""Whole Butternut Squash.

Symmetric butternut squash with a narrow neck, broad lower bulb and short stem. Centerline extremes (10,4)-(38,44). Lucide apple informs the simple attached stem; all neck and bulb transitions share smooth tangents. No surface details omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5251c84f-8f1c-56b7-b3cf-3cdb79f49418'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/butternutsquash_5251c84f-8f1c-56b7-b3cf-3cdb79f49418.svg'
AUTHOR = 'gpt-6'

class ButternutSquashNarrowNeck(Solo48):
    icon_id = 'butternut-squash-narrow-neck'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('whole', 'butternut', 'squash')

    def build(self):
        # Symbol plan: Symmetric butternut squash with a narrow neck, broad lower bulb and short stem. Centerline extremes (10,4)-(38,44). Lucide apple informs the simple attached stem; all neck and bulb transitions share smooth tangents. No surface details omitted.

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

        bilateral('body',(24,10),[('C',(32,18),(30,10),(32,12)),('C',(32,24),(32,20),(32,22)),('C',(38,34),(32,28),(38,28)),('C',(24,44),(38,42),(32,44))])
        line('stem',(24,4),(24,10));join('stem','body')
