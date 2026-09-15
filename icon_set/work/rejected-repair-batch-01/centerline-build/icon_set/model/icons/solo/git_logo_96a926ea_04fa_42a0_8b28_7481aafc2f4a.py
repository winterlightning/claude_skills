"""A diamond contains a forked branch with three nodes; collapse the node rings to dots and retain the upper-left attachment; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '96a926ea-04fa-42a0-8b28-7481aafc2f4a'
SOURCE_PATH = 'pictographic-primitives/logos/git logo_96a926ea-04fa-42a0-8b28-7481aafc2f4a.svg'
AUTHOR = 'gpt-6'

class GitLogo(Solo48):
    icon_id = 'git-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('git', 'version-control', 'branch', 'logo', 'brand', 'developer', 'source')

    def build(self):
        # Plan: A diamond contains a forked branch with three nodes; collapse the node rings to dots and retain the upper-left attachment; extremes (6,6)-(42,42).
        # Construction reference: Lucide git-branch original and atomic-debug: branch topology and node attachments.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        poly('diamond',(24,6),(42,24),(24,42),(6,24),(15,15),closed=True)
        poly('trunk',(15,15),(24,24),(24,32));line('branch',(24,24),(32,24));join('trunk','diamond');join('branch','trunk')
        for i,p in enumerate(((24,24),(24,32),(32,24))):
         self.add_dot(f'node-{i}',p);join(f'node-{i}','trunk' if i<2 else 'branch')
         if i==0:join(f'node-{i}','branch')
