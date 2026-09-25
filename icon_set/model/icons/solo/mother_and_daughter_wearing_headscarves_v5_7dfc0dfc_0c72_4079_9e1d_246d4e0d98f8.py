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
    icon_id = 'mother-and-daughter-wearing-headscarves-v5'
    variant_of = 'mother-and-daughter-wearing-headscarves-v2'
    variant_label = 'Rounded hoods with scarf wraps'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('mother', 'daughter', 'headscarf', 'hijab', 'family')
    def build(self):
        # Rounded face-framing hoods; distinct curved cloth hems and an arm reaching toward the child.

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
        path('mother-hood',(2,46),[('L',(2,16)),('C',(14,2),(2,8),(7,2))])
        line('hood-top',(14,2),(18,2))
        path('hood-right',(18,2),[('C',(30,16),(25,2),(30,8)),('L',(30,20))])
        join('mother-hood','hood-top');join('hood-top','hood-right')
        circle('mother-face',16,15,5)
        path('daughter-hood',(30,20),[('L',(34,20)),('C',(46,33),(41,20),(46,26)),('L',(46,40)),('L',(46,46))])
        circle('daughter-face',33,34,4)
        path('mother-wrap',(2,30),[('C',(20,36),(8,35),(15,36))])
        poly('daughter-left',(20,36),(20,40),(20,46))
        path('daughter-wrap',(20,40),[('C',(31,46),(23,44),(27,46))])
        line('wrap-bottom',(31,46),(35,46))
        path('wrap-right',(35,46),[('C',(46,40),(40,46),(43,44))])
        join('daughter-wrap','wrap-bottom');join('wrap-bottom','wrap-right')
        path('mother-arm',(2,44),[('C',(20,40),(11,47),(17,46))])
        join('hood-right','daughter-hood');join('mother-wrap','mother-hood');join('mother-wrap','daughter-left');join('daughter-wrap','daughter-left');join('wrap-right','daughter-hood');join('mother-arm','mother-hood');join('mother-arm','daughter-left');join('mother-arm','daughter-wrap')
        path('scarf-divider',(30,20),[('C',(20,36),(23.25,27),(20,27))])
        join('scarf-divider','hood-right');join('scarf-divider','daughter-hood');join('scarf-divider','mother-wrap');join('scarf-divider','daughter-left')
