"""Drone at upper left and operator at lower right. Shared rotor dimensions and horizontal capsule. Human full_body_ref.png: head center(36,26), r4, actual torso(36,38) leaves exact 4 ink gap. Lucide drone informs repeated arms. Cropped operator has curved arms meeting a controller.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81881632-71b6-459a-8cf2-c7d98ac7c325'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/play drone_81881632-71b6-459a-8cf2-c7d98ac7c325.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-operating-drone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('person', 'operating', 'drone')
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

        path('drone',(12,14),[('L',(22,14)),('A',(22,22),4,4,True),('L',(12,22)),('A',(12,14),4,4,True)],True)
        for side,x in [('left',12),('right',22)]:
            line(side+'-boom',(x,6),(x,14));join(side+'-boom','drone')
        poly('rotor-left',(6,6),(12,6),(14,6));poly('rotor-right',(22,6),(26,6),(30,6))
        join('rotor-left','left-boom');join('rotor-right','right-boom')
        line('camera',(17,22),(17,25));join('camera','drone')
        circle('head',36,26,4)
        line('torso',(36,38),(36,42))
        path('arms',(28,42),[('C',(36,38),(28,38),(32,38)),('C',(42,42),(40,38),(42,38))])
        join('torso','arms')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
