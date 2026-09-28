"""Revision for bad-stroke feedback. Lucide coffee: tangent bowl corners and a rounded external handle.
Omissions: Steam absent in source; no omissions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f748c868-065c-4348-8b9f-0e60c63d3e9f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cup-1/20260924T092136Z-thuan-mac/reference/cup 1_f748c868-065c-4348-8b9f-0e60c63d3e9f.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'cup-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('cup', '1')
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

        # Body owns bottom radius 10; handle uses an 8-unit semicircle.
        path('body',(6,6),[('L',(32,6)),('L',(32,14)),('L',(32,30)),('L',(32,32)),('A',(22,42),10,10,True),('L',(16,42)),('A',(6,32),10,10,True),('L',(6,6))],True)
        path('handle',(32,14),[('L',(34,14)),('A',(42,22),8,8,True),('A',(34,30),8,8,True),('L',(32,30))])
        join('body','handle')
