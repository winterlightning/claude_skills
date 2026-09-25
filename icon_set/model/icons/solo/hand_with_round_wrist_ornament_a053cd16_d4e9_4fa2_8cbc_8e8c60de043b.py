"""Upright hand with four rounded fingers, side thumb and round wrist ornament. Lucide hand informs equal-radius fingertips. Shared finger widths; smooth continuous palm sides. Wrist band attaches at circular ornament extrema.
Keyshape HRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a053cd16-d4e9-4fa2-8cbc-8e8c60de043b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bracelet with hand_a053cd16-d4e9-4fa2-8cbc-8e8c60de043b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-with-round-wrist-ornament'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('hand', 'with', 'round', 'wrist', 'ornament')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('hand',(12,40),[('L',(12,34)),('C',(4,26),(12,30),(4,30)),('L',(4,24)),('A',(12,24),4,4,True),('L',(12,14)),('A',(20,14),4,4,True),('L',(20,12)),('A',(28,12),4,4,True),('L',(28,14)),('A',(36,14),4,4,True),('L',(36,18)),('A',(44,18),4,4,True),('L',(44,26)),('C',(36,34),(44,30),(36,30)),('L',(36,40))])
        circle('ornament',24,36,3);line('bracelet-left',(12,36),(21,36));line('bracelet-right',(27,36),(36,36))
        for a,b in [('ornament','bracelet-left'),('ornament','bracelet-right'),('bracelet-left','hand'),('bracelet-right','hand')]:join(a,b)
