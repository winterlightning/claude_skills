"""Stylized single musical note with hooked bowl and broad rightward flag; continuous outline. Centerline8,4–40,44.
Lucide construction reference: music-2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e5e7f969-d092-4932-8d8d-f11924b8f98d'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/tiktok logo 1_e5e7f969-d092-4932-8d8d-f11924b8f98d.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/logos/tiktok logo 1_e5e7f969-d092-4932-8d8d-f11924b8f98d.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/tiktok logo 1_e5e7f969-d092-4932-8d8d-f11924b8f98d.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='tiktok-musical-note-logo-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('tiktok', 'musical', 'note', 'logo')
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

        circle('bowl',16,32,10)
        path('stem',(26,32),[('L',(26,6)),('B',(26,12),(34,18),(42,18))]);self.relate('connect','bowl','stem')
