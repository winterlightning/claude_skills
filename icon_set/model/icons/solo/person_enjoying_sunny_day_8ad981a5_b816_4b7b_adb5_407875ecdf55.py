'person-enjoying-sunny-day: Show a relaxed person with raised open arms under a round sun with rays, removing the ambiguous cloud fragment. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ad981a5-b816-4b7b-adb5-407875ecdf55'
SOURCE_PATH = 'pictographic-primitives/nature/virtual environment day_8ad981a5-b816-4b7b-adb5-407875ecdf55.svg'
AUTHOR = 'gpt-6'

class PersonEnjoyingSunnyDay(Solo48):
    icon_id = 'person-enjoying-sunny-day'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('person', 'sun', 'cloud', 'day', 'weather', 'outdoors', 'environment', 'relax')

    def build(self):
        # Symbol plan: Show a relaxed person with raised open arms under a round sun with rays, removing the ambiguous cloud fragment.

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
        path('head',(14,22),[('A',(22,22),4,4,True),('A',(14,22),4,4,True)],True)
        line('torso',(18,34),(18,39));poly('arms',(4,30),(8,34),(18,34),(28,34),(32,30));join('arms','torso')
        poly('legs',(12,44),(18,39),(24,44));join('legs','torso')
        circle('sun',36,10,4)
        for n,a,b in [('up',(36,2),(36,4)),('right',(42,10),(44,10)),('down',(36,16),(36,18)),('left',(28,10),(30,10))]:line('ray-'+n,a,b);join('ray-'+n,'sun')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
