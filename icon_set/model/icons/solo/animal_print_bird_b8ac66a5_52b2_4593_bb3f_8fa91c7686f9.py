'animal-print-bird: Replace ambiguous droplets with two staggered three-toed bird tracks. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8ac66a5-52b2-4593-bb3f-8fa91c7686f9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/animal print bird_b8ac66a5-52b2-4593-bb3f-8fa91c7686f9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AnimalPrintBird(Solo48):
    icon_id = 'animal-print-bird'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('animal', 'print', 'bird', '_uncategorized')

    def build(self):
        # Symbol plan: Replace ambiguous droplets with two staggered three-toed bird tracks.

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
        poly('upper-track',(6,8),(14,18),(14,6))
        line('upper-right',(14,18),(22,8));line('upper-heel',(14,18),(12,24))
        join('upper-track','upper-right');join('upper-track','upper-heel')
        poly('lower-track',(26,26),(34,36),(34,24))
        line('lower-right',(34,36),(42,26));line('lower-heel',(34,36),(32,42))
        join('lower-track','lower-right');join('lower-track','lower-heel')
