"""Bad-stroke revision. Shared human_ref/user.svg and full_body_ref.png for simplified human curves; supplied profile retains its own anatomy.
Omissions: Two minimal orbit marks replace the denser source star series.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e4163be-eaca-4061-a449-298bdb7d7f9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/head dizziness_7e4163be-eaca-4061-a449-298bdb7d7f9a.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'dizzy-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('head', 'dizziness')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Left-facing head meets a shallow open orbit; a plus and a round spark sit above.
        path('orbit',(6,14),[('C',(14,20),(6,17),(10,19)),('C',(24,22),(17,21),(20,22)),('C',(34,20),(28,22),(31,21)),('C',(42,14),(38,19),(42,17))])
        path('face',(14,20),[('L',(8,30)),('L',(14,30)),('L',(14,34)),('A',(20,40),6,6,False),('L',(22,40)),('L',(22,42))])
        path('back',(34,20),[('C',(32,36),(38,26),(38,32)),('L',(32,42))])
        join('face','orbit');join('back','orbit')
        poly('spark-h',(14,8),(16,8),(18,8));poly('spark-v',(16,6),(16,8),(16,10));join('spark-h','spark-v')
        circle('spark-circle',32,8,2)
