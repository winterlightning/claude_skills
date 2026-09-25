"""Broad three-lobed cloud with level base and tall middle dome. Side lobes share radius10, central crown mirrored about24. Centerline4,8–44,40.
Construction reference: cloud.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a1e16064-3ada-48c1-977b-93e026ae68e7'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/microsoft onedrive logo_a1e16064-3ada-48c1-977b-93e026ae68e7.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/logos/microsoft onedrive logo_a1e16064-3ada-48c1-977b-93e026ae68e7.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/microsoft onedrive logo_a1e16064-3ada-48c1-977b-93e026ae68e7.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='three-lobed-cloud-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases=()
    keywords=('three', 'lobed', 'cloud')
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

        path('cloud',(14,40),[('A',10,10,True,(4,30)),('A',10,10,True,(14,20)),('B',(14,12),(18,8),(24,8)),('B',(30,8),(34,12),(34,20)),('A',10,10,True,(44,30)),('A',10,10,True,(34,40)),('L',(14,40))],True)
