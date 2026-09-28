"""Modern Three Drawer Dresser.

Modern three-drawer dresser with two straight legs. Centerline extremes (6,6)-(42,42). No close local Lucide dresser match. Equal-height full-width drawers share divider geometry; omit short pulls to preserve the three clear rows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d30827e-25ea-51a2-8499-29e48d158173'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dresser drawers_4d30827e-25ea-51a2-8499-29e48d158173.svg'
AUTHOR = 'gpt-6'

class ModernDresserThreeDrawersTwoLegs(Solo48):
    icon_id = 'modern-dresser-three-drawers-two-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('modern', 'three', 'drawer', 'dresser')

    def build(self):
        # Symbol plan: Modern three-drawer dresser with two straight legs. Centerline extremes (6,6)-(42,42). No close local Lucide dresser match. Equal-height full-width drawers share divider geometry; omit short pulls to preserve the three clear rows.

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

        path('case',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,16)),('L',(42,26)),('L',(42,32)),('A',(38,36),4,4,True),('L',(34,36)),('L',(14,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,26)),('L',(6,16)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        for y in (16,26):line(f'divider-{y}',(6,y),(42,y));join(f'divider-{y}','case')
        for x in (14,34):line(f'leg-{x}',(x,36),(x,42));join(f'leg-{x}','case')
