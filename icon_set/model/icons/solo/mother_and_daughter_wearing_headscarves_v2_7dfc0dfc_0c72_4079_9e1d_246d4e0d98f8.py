"""A taller mother behind her daughter; circular face openings and a curved scarf drape.
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
    icon_id = 'mother-and-daughter-wearing-headscarves-v2'
    variant_of = 'mother-and-daughter-wearing-headscarves'
    variant_label = 'Layered scarf portraits'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/family'
    aliases = ()
    keywords = ('mother', 'daughter', 'headscarf', 'hijab', 'family')
    def build(self):
        # Symbol plan: A taller mother behind her daughter; circular face openings and a curved scarf drape.

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
        path('mother-hood',(2,46),[('L',(2,17)),('A',(16,3),14,14,True),('A',(30,17),14,14,True),('C',(33,24),(30,21),(30,24))])
        circle('mother-face',16,17,5)
        path('daughter-hood',(20,46),[('L',(20,37)),('A',(33,24),13,13,True),('A',(46,37),13,13,True),('L',(46,46))])
        circle('daughter-face',33,37,4)
        path('mother-drape',(2,32),[('C',(20,37),(8,38),(15,39))])
        join('mother-hood','daughter-hood');join('mother-drape','mother-hood');join('mother-drape','daughter-hood')
