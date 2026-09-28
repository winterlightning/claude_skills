"""Bad-stroke revision. Lucide paperclip: one continuous wire with smooth nested return bends.
Omissions: No identity-bearing features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5473937d-c579-47bd-9ac8-1ed8c210eb47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-paperclip-batch-021-13/20260924T093003Z-thuan-mac/reference/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-paperclip-batch-021-13'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('attached', 'file')
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

        # A single wire, with diagonals separated by shared 12-unit sum offsets.
        path('wire',(42,30),[('L',(34,38)),('C',(24,42),(31,41),(28,42)),('C',(6,28),(14,42),(6,36)),('C',(10,20),(6,25),(8,22)),('L',(22,8)),('C',(30,6),(24,6),(27,6)),('C',(42,18),(37,6),(42,11)),('C',(38,22),(42,20),(40,20)),('L',(28,32)),('C',(20,24),(24,36),(16,28)),('L',(30,14))])
