"""Movie Director Chair.

Director chair with rectangular canvas back, shallow seat and X-crossed folding legs. Centerline extremes (8,4)-(40,44). No close Lucide director-chair match. Preserve the X as two true crossing supports; simplify the small arms to the projecting seat ends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '098da1cc-b8cd-54ab-ba1f-abace85a71c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair director_098da1cc-b8cd-54ab-ba1f-abace85a71c9.svg'
AUTHOR = 'gpt-6'

class DirectorChairCanvasCrossedLegs(Solo48):
    icon_id = 'director-chair-canvas-crossed-legs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('movie', 'director', 'chair')

    def build(self):
        # Symbol plan: Director chair with rectangular canvas back, shallow seat and X-crossed folding legs. Centerline extremes (8,4)-(40,44). No close Lucide director-chair match. Preserve the X as two true crossing supports; simplify the small arms to the projecting seat ends.

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

        self.add_polyline('back',(12,4),(36,4),(36,12),(12,12),closed=True)
        for x in (12,36):line(f'post-{x}',(x,12),(x,24));join(f'post-{x}','back')
        self.add_polyline('seat',(8,24),(12,24),(36,24),(40,24))
        for x in (12,36):join(f'post-{x}','seat')
        self.add_polyline('leg-a',(12,24),(24,34),(36,44));self.add_polyline('leg-b',(36,24),(24,34),(12,44));join('leg-a','leg-b');join('leg-a','seat');join('leg-b','seat')
