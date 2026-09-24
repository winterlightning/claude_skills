"""Revision for bad-stroke feedback. Lucide cat: paired pointed ears, rounded cheeks, small separate eyes.
Omissions: Simplified mouth to one broad smile; no whiskers in source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90005858-b0d4-51de-9d62-a9c0ec953e68'
SOURCE_PATH = 'pictographic-primitives/video-games/cute cat_90005858-b0d4-51de-9d62-a9c0ec953e68.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'cute-cat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('cute', 'cat')
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

        # Mirror ear and cheek construction about x=24; bounds 6,6 to 42,42.
        path('head',(18,14),[('L',(8,6)),('A',(6,8),2,2,False),('L',(8,22)),('C',(24,42),(4,38),(10,42)),('C',(40,22),(38,42),(44,38)),('L',(42,8)),('A',(40,6),2,2,False),('L',(30,14)),('L',(18,14))],True)
        for x in (16,32): self.add_dot('eye-'+str(x),(x,23))
        path('smile',(20,31),[('A',(28,31),5,5,False)])
