"""Audience under broad cinema screen. Reduce five busts to three foreground heads and a shared shoulder row; inner-screen figures omitted because two human rows cannot retain head/body clearance at48. Human ref user.svg: head radius3, bottom32, shoulder top40, exact4 ink gap. Centerline4,8–44,40.
Lucide construction reference: human_ref/user.svg; monitor.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b2ae8639-be76-49c2-be2d-6826d421c781'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/movies/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/movies/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='audience-watching-people-on-screen-solo-b017'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "movies"
    aliases=()
    keywords=('audience', 'watching', 'people', 'on', 'screen')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        path('screen',(4,17),[('L',(4,11)),('A',3,3,True,(7,8)),('L',(41,8)),('A',3,3,True,(44,11)),('L',(44,17))])
        for x in (10,24,38):circle('head'+str(x),x,27,3)
        path('shoulders',(4,40),[('B',(6,38),(8,38),(10,38)),('B',(13,38),(15,39),(17,40)),('B',(19,38),(21,38),(24,38)),('B',(27,38),(29,38),(31,40)),('B',(33,39),(35,38),(38,38)),('B',(40,38),(42,38),(44,40))])
