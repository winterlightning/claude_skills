"""armored-hero-with-pointed-helmet: independent batch-086 SOLO48 result.
Plan: Pointed helmet around a circular lower jaw, with eye dots and rounded shoulders. Jaw bottom y=32, shoulder top y=36: exact zero ink gap.
Reference construction: human_ref/user.svg.
Reduction: Reduced armor seams and neck detail; retained the pointed helmet, circular jaw, eyes and broad rounded shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed5c437b-f1b7-5deb-8e7e-d0d95f2f6077'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/megaman zero_ed5c437b-f1b7-5deb-8e7e-d0d95f2f6077.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/megaman zero_ed5c437b-f1b7-5deb-8e7e-d0d95f2f6077.svg'

class Drawing(Solo48):
    icon_id = 'armored-hero-with-pointed-helmet-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('armored', 'hero', 'with', 'pointed', 'helmet')

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


        path('helmet-head',(8,4),[('L',(24,12)),('L',(40,4)),('L',(40,20)),('L',(36,20)),('A',(24,32),12,12,True),('A',(12,20),12,12,True),('L',(8,20)),('L',(8,4))],True)
        for x in (20,28):dot(f'eye-{x}',(x,19))
        path('shoulders',(8,44),[('A',(24,36),16,8,True),('A',(40,44),16,8,True)])
        join('helmet-head','shoulders')
