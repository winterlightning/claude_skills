"""Finger touches a smartphone with a single tap arc. Lucide smartphone supplies equal-radius corners and hand supplies round fingertip. Reference diagonal pointing pose retained; secondary tap ring omitted for clearance.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5462084-18e8-4a32-940d-898d288894e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/34-f5462084-18e8-4a32-940d-898d288894e7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='finger-touching-smartphone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('finger', 'touching', 'smartphone')
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

        path('phone',(38,14),[('L',(38,10)),('A',(34,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(17,42))])
        path('hand',(42,42),[('L',(42,36)),('C',(38,30),(42,33),(40,32)),('L',(34,26)),('C',(27,25),(32,24),(29,25)),('C',(24,28),(25,25),(24,26)),('C',(26,32),(24,30),(25,31)),('L',(36,42))])
        path('tap',(16,26),[('A',(26,16),10,10,True)])
