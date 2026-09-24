"""A sole-facing foot with rounded toe lobes receives three evenly spaced acupuncture needles with circular heads. Extrema 8,4,40,44.
Construction: footprints: rounded toe/heel contour; human reference reviewed, no head/body gap applies
Reduction: Smallest toe divisions reduced to three clear lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f03cca0a-0e3a-4528-a0f0-17a4b8398df9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/04-f03cca0a-0e3a-4528-a0f0-17a4b8398df9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='foot-three-acupuncture-needles'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('foot', 'three', 'acupuncture', 'needles')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('foot',(24,40),[('A',(20,44),4,4,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,9)),('A',(18,9),5,5,True),('A',(24,9),3,3,True),('A',(30,9),3,3,True)])
        for i,(a,y) in enumerate([((20,20),16),((22,28),28),((24,40),40)]):
            line('needle-'+str(i),a,(36,y));circle('head-'+str(i),38,y,2);join('needle-'+str(i),'head-'+str(i))
        join('needle-2','foot')
