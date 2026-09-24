"""Revision for bad-stroke feedback. Lucide gauge: coherent arch and a single straight diagonal pointer.
Omissions: No scale ticks or numerals exist in source; retained crossing tick.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d3425c4-0090-4fdf-b40b-9f93695f8ca8'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'curved-gauge-indicator-solo-b017'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/everyday'
    aliases = ()
    keywords = ('adjustable',)
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

        # Shared arch and pointer attachment; duplicate source, distinct claimed ID.
        path('arch',(4,38),[('C',(24,10),(4,22),(12,10)),('C',(40,22),(32,10),(37,15)),('C',(44,38),(43,29),(44,33))])
        poly('pointer',(32,28),(40,22),(44,19))
        join('arch','pointer')
