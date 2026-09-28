"""Four Drawer Storage Dresser.

Dresser with two small top drawers over two full-width drawers and two feet. Centerline extremes (6,6)-(42,42). No close local Lucide dresser match; shared dividers preserve four drawers. Omit pulls because three rows leave no clear band for them.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d1cb219-2fef-53ef-9b52-775dca1b1330'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dresser drawers_7d1cb219-2fef-53ef-9b52-775dca1b1330.svg'
AUTHOR = 'gpt-6'

class DresserFourDrawers(Solo48):
    icon_id = 'dresser-four-drawers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('four', 'drawer', 'storage', 'dresser')

    def build(self):
        # Symbol plan: Dresser with two small top drawers over two full-width drawers and two feet. Centerline extremes (6,6)-(42,42). No close local Lucide dresser match; shared dividers preserve four drawers. Omit pulls because three rows leave no clear band for them.

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

        path('case',(24,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,16)),('L',(42,26)),('L',(42,32)),('A',(38,36),4,4,True),('L',(34,36)),('L',(14,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,26)),('L',(6,16)),('L',(6,10)),('A',(10,6),4,4,True),('L',(24,6))],True)
        self.add_polyline('upper-row',(6,16),(24,16),(42,16));line('lower-row',(6,26),(42,26));line('top-split',(24,6),(24,16))
        for n in ('upper-row','lower-row','top-split'):join(n,'case')
        join('top-split','upper-row')
        for x in (14,34):line(f'foot-{x}',(x,36),(x,42));join(f'foot-{x}','case')
