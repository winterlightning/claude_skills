"""Six grape regions form a tapered bunch below a pointed leaf; shared junctions preserve the clustered arrangement.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: grape: repeated rounded fruit regions and tapered bunch
Omissions: Small curling stem omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3d395084-0155-47c6-a5ce-c8b1349a3045'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/muscatel_3d395084-0155-47c6-a5ce-c8b1349a3045.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='grape-bunch-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('grape', 'bunch', 'leaf')
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

        path('bunch',(8,22),[('C',(19,21),(8,14),(17,13)),('C',(24,14),(19,17),(20,14)),('C',(29,21),(28,14),(29,17)),('C',(40,22),(31,13),(40,14)),('C',(36,32),(40,27),(39,30)),('C',(30,36),(37,36),(34,38)),('C',(24,44),(30,42),(28,44)),('C',(18,36),(20,44),(18,42)),('C',(12,32),(14,38),(11,36)),('C',(8,22),(9,30),(8,27))],True)
        path('leaf',(24,14),[('C',(40,4),(24,6),(32,4)),('C',(24,14),(40,11),(32,14))],True);join('leaf','bunch')
        path('top-seams',(19,21),[('C',(18,28),(20,24),(20,26)),('C',(30,28),(21,33),(27,33)),('C',(29,21),(28,26),(28,24))]);join('top-seams','bunch')
        path('lower-seam',(12,32),[('C',(18,28),(12,29),(15,28)),('C',(18,36),(20,31),(20,34))]);join('lower-seam','bunch');join('lower-seam','top-seams')
        path('right-seam',(36,32),[('C',(30,28),(36,29),(33,28)),('C',(30,36),(28,31),(28,34))]);join('right-seam','bunch');join('right-seam','top-seams')
