"""portrait-with-bob-hair-and-pendant-collar: independent batch-086 SOLO48 result.
Plan: Circular face inside a semicircular bob, broad paired shoulder arcs and one centered pendant. Circular face bottom 27, shoulders top 31: exact zero ink gap.
Reference construction: human_ref/user.svg.
Reduction: Omitted tiny facial mark and reduced the three necklace ornaments to one pendant, preserving the bob and broad collar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '982bdc1e-36e5-4108-b7e3-97ae6b741259'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/magneto_982bdc1e-36e5-4108-b7e3-97ae6b741259.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/magneto_982bdc1e-36e5-4108-b7e3-97ae6b741259.svg'

class Drawing(Solo48):
    icon_id = 'portrait-with-bob-hair-and-pendant-collar-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('portrait', 'with', 'bob', 'hair', 'and', 'pendant', 'collar')

    human_construction = "bust"

    def build(self):
        # Exact envelope comes from Keyshape.VRECT_L.bounds_for(self.profile).

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{j}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)


        path('bob',(8,24),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,24))])
        oval('face',24,20,7,7)
        path('shoulders',(8,40),[('A',(24,31),16,9,True),('A',(40,40),16,9,True)])
        dot('pendant',(24,44))
        join('face','shoulders')
