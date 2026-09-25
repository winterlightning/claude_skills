"""Modern Two Seater Sofa.

Two-seat sofa with divided back and seat cushions, rounded arms and slanted legs. Centerline extremes (4,8)-(44,40). Lucide sofa informs a centered cushion division and attached arms. Mirror all geometry; simplify cushion piping to one continuous center seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3c61dab-0cce-5739-8130-47bf63a9b52b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/sofa double modern_d3c61dab-0cce-5739-8130-47bf63a9b52b.svg'
AUTHOR = 'gpt-6'

class ModernTwoSeatSofaSplitCushions(Solo48):
    icon_id = 'modern-two-seat-sofa-split-cushions'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('modern', 'two', 'seater', 'sofa')

    def build(self):
        # Symbol plan: Two-seat sofa with divided back and seat cushions, rounded arms and slanted legs. Centerline extremes (4,8)-(44,40). Lucide sofa informs a centered cushion division and attached arms. Mirror all geometry; simplify cushion piping to one continuous center seam.

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

        path('back',(12,20),[('L',(12,12)),('A',(16,8),4,4,True),('L',(24,8)),('L',(32,8)),('A',(36,12),4,4,True),('L',(36,20))])
        path('frame',(12,26),[('L',(12,20)),('A',(4,20),4,4,False),('L',(4,30)),('A',(8,34),4,4,False),('L',(12,34)),('L',(24,34)),('L',(36,34)),('L',(40,34)),('A',(44,30),4,4,False),('L',(44,20)),('A',(36,20),4,4,False),('L',(36,26)),('L',(24,26)),('L',(12,26))],True);join('back','frame')
        self.add_polyline('seam',(24,8),(24,26),(24,34));join('seam','back');join('seam','frame')
        for n,a,b in [('left',(12,34),(10,40)),('right',(36,34),(38,40))]:line(n,a,b);join(n,'frame')
