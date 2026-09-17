"""Sliced Delicata Squash Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98f36230-6f30-598e-8483-72d9fb9ed7bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/delicata squash slice_98f36230-6f30-598e-8483-72d9fb9ed7bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sliced-delicata-squash'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('sliced', 'delicata', 'squash')

    def build(self):
        # Plan: Lengthwise squash with broad bottom, narrower neck and two vertically linked cavities. Lower chamber retained as an unsplit oval to avoid crowding. No useful exact Lucide match.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('squash',(24,4),[('C',(36,14),(31,4),(36,8)),('C',(35,22),(36,18),(34,18)),('C',(40,32),(37,26),(40,28)),('C',(24,44),(40,40),(32,44)),('C',(8,32),(16,44),(8,40)),('C',(13,22),(8,28),(11,26)),('C',(12,14),(14,18),(12,18)),('C',(24,4),(12,8),(17,4))],True)
        path('upper-cavity',(24,13),[('A',(24,17),2,2,True),('A',(24,13),2,2,True)],True)
        path('lower-cavity',(24,25),[('A',(24,35),5,5,True),('A',(24,25),5,5,True)],True)
        line('axis',(24,17),(24,25));join('axis','upper-cavity');join('axis','lower-cavity')
