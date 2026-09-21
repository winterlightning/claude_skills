'A tied shoelace forms two broad rounded loops above a central crossing. Two long ends descend outward, with another pair of crossing lace segments visible just below the bow.\nPlan: Shoelace bow with two loops and long tails. Remove the secondary under-knot crossing to keep the central tie legible.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb4deb22-4745-40e3-8d3a-e339e6d20f90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shoelace_fb4deb22-4745-40e3-8d3a-e339e6d20f90.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tied-shoelace-bow-with-crossed-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tied', 'shoelace', 'bow', 'with', 'crossed', 'ends')

    # Repair: Loop tops reach exact y=6 and use circular outer turns, preserving a single central knot.
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

        path('left-loop',(24,22),[('C',(12,6),(20,16),(17,6)),('A',(6,12),6,6,False),('C',(24,22),(6,22),(16,22))],True)
        path('right-loop',(24,22),[('C',(36,6),(28,16),(31,6)),('A',(42,12),6,6,True),('C',(24,22),(42,22),(32,22))],True)
        path('left-tail',(24,22),[('C',(6,42),(17,28),(9,33))]);path('right-tail',(24,22),[('C',(42,42),(31,28),(39,33))])
        for a,b in [('left-loop','right-loop'),('left-loop','left-tail'),('left-loop','right-tail'),('right-loop','left-tail'),('right-loop','right-tail'),('left-tail','right-tail')]:join(a,b)
