"""Bad-stroke revision. Lucide pipette: rounded bulb, crossbar and tapered nozzle.
Omissions: Crossbar overhang shortened to keep separate teardrop readable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5eccea6a-8969-5c4b-a202-3accdc0f67c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color drop pick_5eccea6a-8969-5c4b-a202-3accdc0f67c2.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-eyedropper-beside-liquid-drop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('color', 'drop', 'pick')
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

        # One angled pipette outline and a separate teardrop at lower right.
        path('pipette',(22,14),[('L',(28,8)),('C',(32,6),(30,6),(31,6)),('C',(38,12),(35,6),(38,9)),('C',(36,16),(38,14),(37,15)),('L',(30,22)),('L',(18,34)),('C',(10,38),(16,36),(12,34)),('L',(6,38)),('L',(6,34)),('C',(10,26),(10,30),(8,28)),('L',(22,14))],True)
        poly('flange',(21,13),(22,14),(30,22),(31,23));join('flange','pipette')
        path('drop',(36,30),[('C',(42,38),(38,33),(42,35)),('A',(36,42),6,4,True),('A',(30,38),6,4,True),('C',(36,30),(30,35),(34,33))],True)
