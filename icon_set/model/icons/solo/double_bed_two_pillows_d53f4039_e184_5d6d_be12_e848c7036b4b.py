"""Double Bed with Pillows.

Double bed with rounded headboard, two pillows, broad blanket front and two short feet. Centerline extremes (4,8)-(44,40). Lucide bed-double informs frame hierarchy. Two raised pillow tops remain visible above the blanket; remove the doubled headboard border.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd53f4039-e184-5d6d-be12-e848c7036b4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/bed double_d53f4039-e184-5d6d-be12-e848c7036b4b.svg'
AUTHOR = 'gpt-6'

class DoubleBedTwoPillows(Solo48):
    icon_id = 'double-bed-two-pillows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('double', 'bed', 'with', 'pillows')

    def build(self):
        # Symbol plan: Double bed with rounded headboard, two pillows, broad blanket front and two short feet. Centerline extremes (4,8)-(44,40). Lucide bed-double informs frame hierarchy. Two raised pillow tops remain visible above the blanket; remove the doubled headboard border.

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

        path('headboard',(4,26),[('L',(4,16)),('A',(12,8),8,8,True),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,26))])
        self.add_polyline('blanket',(4,40),(4,34),(4,26),(12,26),(20,26),(28,26),(36,26),(44,26),(44,34),(44,40));join('blanket','headboard')
        line('footboard',(4,34),(44,34));join('footboard','blanket')
        for i,x in enumerate((12,28)):
            path(f'pillow-{i}',(x,26),[('L',(x,18)),('L',(x+8,18)),('L',(x+8,26))]);join(f'pillow-{i}','blanket')
