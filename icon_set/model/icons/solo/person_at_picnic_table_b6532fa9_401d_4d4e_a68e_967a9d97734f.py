'person-at-picnic-table: Separate the bent seated torso and forearm from the tabletop, with a clear bench and splayed table legs. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6532fa9-401d-4d4e-a68e-967a9d97734f'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors bench sit_b6532fa9-401d-4d4e-a68e-967a9d97734f.svg'
AUTHOR = 'gpt-6'


class PersonAtPicnicTable(Solo48):
    icon_id = 'person-at-picnic-table'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('picnic', 'bench', 'table', 'sitting', 'person', 'park', 'rest', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Symbol plan: Separate the bent seated torso and forearm from the tabletop, with a clear bench and splayed table legs.

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
        circle('head',12,8,4)
        poly('body',(12,20),(12,24),(8,34),(18,34),(20,44))
        poly('arm',(12,20),(20,24),(28,24));join('arm','body')
        line('table',(28,24),(44,24));poly('table-legs',(30,44),(36,24),(44,44));join('table','arm');join('table','table-legs')
        line('bench',(4,34),(8,34));line('bench-leg',(6,34),(4,44));join('bench','body');join('bench','bench-leg')
        self.mark_human_figure('seated-person',head='head',torso='body-1',torso_junction='start')
