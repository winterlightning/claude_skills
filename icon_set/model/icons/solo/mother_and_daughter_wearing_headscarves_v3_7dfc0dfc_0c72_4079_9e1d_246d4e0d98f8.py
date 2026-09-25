"""Two larger circular faces with scarves draping from the temples; mother taller at left, daughter at right.
Human reference: icon_set/references/human_ref/user.svg.
Natural mother/child grouping; circles are face openings in continuous garments,
not detached stick-figure heads. Deliberate height asymmetry carries age difference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim mom daughter_7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mother-and-daughter-wearing-headscarves-v3'
    variant_of = 'mother-and-daughter-wearing-headscarves'
    variant_label = 'Draped triangular scarves'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('mother', 'daughter', 'headscarf', 'hijab', 'family')
    def build(self):
        # Symbol plan: Two larger circular faces with scarves draping from the temples; mother taller at left, daughter at right.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        circle('mother-face',14,14,8)
        path('mother-scarf',(6,14),[('C',(2,32),(6,22),(2,25)),('C',(14,38),(4,36),(9,38)),('C',(28,36),(20,38),(24,38))])
        path('mother-right',(22,14),[('C',(30,28),(23,20),(28,24))])
        circle('daughter-face',36,28,6)
        path('daughter-scarf',(30,28),[('L',(28,36)),('L',(26,44)),('C',(36,46),(29,45),(33,46)),('C',(46,44),(40,46),(43,45)),('L',(42,28))])
        join('mother-face','mother-scarf');join('mother-face','mother-right');join('mother-scarf','daughter-scarf');join('mother-right','daughter-face');join('mother-right','daughter-scarf');join('daughter-face','daughter-scarf')
