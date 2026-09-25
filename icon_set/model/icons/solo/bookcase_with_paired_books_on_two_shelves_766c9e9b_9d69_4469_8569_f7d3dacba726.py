'A tall rectangular bookcase contains two shelf compartments, each holding a pair of upright books on the left. The books have plain rectangular spines, and the right sides of both shelves remain empty.\nPlan: Two shelf compartments with two rectangular book spines each; all shelf contacts real.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '766c9e9b-9d69-4469-8569-f7d3dacba726'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shelves_766c9e9b-9d69-4469-8569-f7d3dacba726.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bookcase-with-paired-books-on-two-shelves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bookcase', 'with', 'paired', 'books', 'on', 'two', 'shelves')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        poly('case',(8,4),(40,4),(40,24),(40,44),(8,44),(8,24),(8,4))
        line('shelf',(8,24),(40,24));join('shelf','case')
        for j,(x,y) in enumerate([(8,12),(24,12),(8,32),(24,32)]):
         poly(f'book-{j}',(x,y+12),(x,y),(x+8,y),(x+8,y+12));join(f'book-{j}','case')
         if y==12:join(f'book-{j}','shelf')
