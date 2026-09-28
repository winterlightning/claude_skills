"""Laced Winter Boot.

Winter boot with broad cuff, tall shaft, rounded right-facing toe and layered sole. Centerline extremes (6,6)-(42,42). Lucide sport-shoe informs upper/sole separation. Reduce shaft seam details to one short attached mark to preserve open space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99d4550a-249a-486f-8be5-ffcab913ef6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/winter boots_99d4550a-249a-486f-8be5-ffcab913ef6c.svg'
AUTHOR = 'gpt-6'

class WinterBootWideCuff(Solo48):
    icon_id = 'winter-boot-wide-cuff'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    categories = ('primitives', 'footwear')
    aliases = ()
    keywords = ('laced', 'winter', 'boot')

    def build(self):
        # Symbol plan: Winter boot with broad cuff, tall shaft, rounded right-facing toe and layered sole. Centerline extremes (6,6)-(42,42). Lucide sport-shoe informs upper/sole separation. Reduce shaft seam details to one short attached mark to preserve open space.

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

        path('boot',(6,6),[('L',(24,6)),('L',(24,14)),('L',(24,22)),('C',(34,26),(24,25),(28,26)),('C',(42,34),(42,26),(42,30)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,34)),('L',(6,14)),('L',(6,6))],True)
        line('cuff',(6,14),(24,14));join('cuff','boot')
        line('sole',(6,34),(42,34));join('sole','boot')
        line('seam',(24,22),(19,22));join('seam','boot')
