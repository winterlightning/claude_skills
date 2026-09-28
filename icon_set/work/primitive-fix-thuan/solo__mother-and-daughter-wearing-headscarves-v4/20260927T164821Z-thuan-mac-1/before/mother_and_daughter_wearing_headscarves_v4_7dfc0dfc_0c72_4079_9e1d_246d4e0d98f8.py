"""Mother and daughter closer together, with broad face openings, short shoulder scarves and open bust outlines.
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
    icon_id = 'mother-and-daughter-wearing-headscarves-v4'
    variant_of = 'mother-and-daughter-wearing-headscarves'
    variant_label = 'Close shoulder portraits'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('mother', 'daughter', 'headscarf', 'hijab', 'family')
    def build(self):
        # Symbol plan: Mother and daughter closer together, with broad face openings, short shoulder scarves and open bust outlines.

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
        circle('daughter-face',34,24,6)
        path('mother-drape',(6,14),[('C',(2,32),(6,22),(2,25)),('C',(14,38),(5,36),(9,38)),('C',(24,34),(18,38),(22,36))])
        path('mother-right',(22,14),[('C',(28,24),(23,19),(27,20))])
        path('daughter-drape',(28,24),[('L',(24,34)),('C',(34,40),(26,38),(30,40)),('C',(44,34),(38,40),(42,38)),('L',(40,24))])
        line('mother-body',(2,32),(2,46));line('daughter-body',(44,34),(46,46))
        join('mother-face','mother-drape');join('mother-face','mother-right');join('mother-right','daughter-face');join('mother-right','daughter-drape');join('daughter-face','daughter-drape');join('mother-drape','daughter-drape');join('mother-body','mother-drape');join('daughter-body','daughter-drape')
