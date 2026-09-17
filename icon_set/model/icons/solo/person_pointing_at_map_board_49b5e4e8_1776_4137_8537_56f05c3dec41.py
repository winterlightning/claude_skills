'person-pointing-at-map-board: Make the arm point visibly to a winding route on a freestanding board, with a complete upright person. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49b5e4e8-1776-4137-8537-56f05c3dec41'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking map_49b5e4e8-1776-4137-8537-56f05c3dec41.svg'
AUTHOR = 'gpt-6'

class PersonPointingAtMapBoard(Solo48):
    icon_id = 'person-pointing-at-map-board'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('map', 'trekking', 'route', 'board', 'briefing', 'person', 'guide', 'planning', 'outdoors-batch-03')

    def build(self):
        # Symbol plan: Make the arm point visibly to a winding route on a freestanding board, with a complete upright person.

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
        path('head',(2,19),[('A',(10,19),4,4,True),('A',(2,19),4,4,True)],True)
        line('torso',(6,31),(6,37));poly('legs',(2,44),(6,37),(10,44));join('torso','legs')
        poly('arm',(6,31),(14,31),(22,24));join('arm','torso')
        poly('board',(22,4),(46,4),(46,36),(22,36),(22,24),(22,4));join('arm','board')
        line('stand',(34,36),(34,44));join('stand','board')
        path('route',(31,27),[('C',(37,13),(42,24),(28,18))])
        self.mark_human_figure('guide',head='head',torso='torso',torso_junction='start')
