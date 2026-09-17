"""Modern Kitchen Cabinets.

Kitchen with three upper cabinets, three lower cabinets and a middle faucet. Centerline extremes (6,6)-(42,42). No useful local Lucide kitchen match. Equal cabinet widths share one repeat; remove tiny pulls and extra worktop fixtures.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35a0408b-63d7-4c05-9a0e-792e0acdb119'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/kitchen storage_35a0408b-63d7-4c05-9a0e-792e0acdb119.svg'
AUTHOR = 'gpt-6'

class ModernKitchenUpperLowerCabinets(Solo48):
    icon_id = 'modern-kitchen-upper-lower-cabinets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('modern', 'kitchen', 'cabinets')

    def build(self):
        # Symbol plan: Kitchen with three upper cabinets, three lower cabinets and a middle faucet. Centerline extremes (6,6)-(42,42). No useful local Lucide kitchen match. Equal cabinet widths share one repeat; remove tiny pulls and extra worktop fixtures.

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

        for n,t,b in [('upper',6,14),('lower',30,42)]:
            self.add_polyline(n,(6,t),(18,t),(24,t),(30,t),(42,t),(42,b),(30,b),(18,b),(6,b),closed=True)
            for x in (18,30):line(f'{n}-divider-{x}',(x,t),(x,b));join(f'{n}-divider-{x}',n)
        path('faucet',(24,30),[('L',(24,26)),('A',(28,22),4,4,True),('L',(32,22))]);join('faucet','lower')
