"""Round reservoir narrows smoothly into an open lower outlet; paired ureters join its shoulders.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: No useful exact Lucide match; original bladder contour governs anatomy.
Omissions: None; upper tubes remain intentionally open.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa2f0590-bd03-4d41-8846-978c972a01fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bladder_aa2f0590-bd03-4d41-8846-978c972a01fe.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bladder-with-connecting-tubes'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('bladder', 'with', 'connecting', 'tubes')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('bladder',(20,44),[('L',(20,39)),('C',(15,32),(20,35),(18,34)),('C',(8,22),(10,29),(8,26)),('C',(12,16),(8,19),(9,17)),('C',(24,12),(15,13),(20,12)),('C',(36,16),(28,12),(33,13)),('C',(40,22),(39,17),(40,19)),('C',(33,32),(40,26),(38,29)),('C',(28,39),(30,34),(28,35)),('L',(28,44))])
        path('left-ureter',(8,4),[('C',(12,16),(8,10),(8,14))]);join('left-ureter','bladder')
        path('right-ureter',(40,4),[('C',(36,16),(40,10),(40,14))]);join('right-ureter','bladder')
