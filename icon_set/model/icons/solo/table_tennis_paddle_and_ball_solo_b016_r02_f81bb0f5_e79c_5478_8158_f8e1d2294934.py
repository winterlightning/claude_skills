"""Revision for bad-stroke feedback. Lucide coffee informed tangent contour transitions; no useful exact paddle match.
Omissions: Rubber seam omitted to preserve paddle face opening; outlined handle and ball retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f81bb0f5-e79c-5478-8158-f8e1d2294934'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'table-tennis-paddle-and-ball-solo-b016-r02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/toys'
    aliases = ()
    keywords = ('toys', 'ping', 'pong')
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

        # Diagonal paddle: large rounded blade, neck, and capsule-ended handle.
        path('paddle',(18,24),[('C',(12,12),(10,22),(8,18)),('C',(26,6),(16,6),(22,6)),('C',(38,18),(34,6),(38,12)),('C',(24,28),(38,26),(32,28)),('L',(12,42)),('A',(6,36),6,6,True),('L',(18,24))],True)
        circle('ball',39,39,3)
