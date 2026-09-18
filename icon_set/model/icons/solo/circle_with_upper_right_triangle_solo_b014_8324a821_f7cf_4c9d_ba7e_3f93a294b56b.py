"""Large lower-left circle and detached upper-right outlined pointer, preserving the rendered source rather than inventing a Mars shaft. Circle radius12; triangular pointer has a clear interior. Ink box (4,4)-(44,44).
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8324a821-f7cf-4c9d-ba7e-3f93a294b56b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'circle-with-upper-right-triangle-solo-b014'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/controls"
    aliases = ()
    keywords = ('circle', 'with', 'upper', 'right', 'triangle')
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

        circle('circle',18,30,12)
        self.add_polyline('pointer',(24,6),(42,6),(42,24),closed=True)
