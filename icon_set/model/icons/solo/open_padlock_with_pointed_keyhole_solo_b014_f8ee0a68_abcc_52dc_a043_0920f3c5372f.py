"""Open padlock with rounded body, arched shackle and tiny circular keyhole/slot. Simplify the pointed keyhole treatment to a circular opening and short slot to retain a clean hole. Ink box (6,2)-(42,46).
 Tiny slot omitted to leave a clean circular keyhole with nine units to the body edge.
Lucide construction reference: lock-keyhole-open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8ee0a68-abcc-52dc-a043-0920f3c5372f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/lock unlock_f8ee0a68-abcc-52dc-a043-0920f3c5372f.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock unlock_f8ee0a68-abcc-52dc-a043-0920f3c5372f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/lock unlock_f8ee0a68-abcc-52dc-a043-0920f3c5372f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-padlock-with-pointed-keyhole-solo-b014'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('open', 'padlock', 'with', 'pointed', 'keyhole')
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

        path('body',(8+3,22),[('L',(14,22)),('L',(34,22)),('L',(37,22)),('A',3,3,True,(40,25)),('L',(40,41)),('A',3,3,True,(37,44)),('L',(11,44)),('A',3,3,True,(8,41)),('L',(8,25)),('A',3,3,True,(11,22))],True)
        path('shackle',(14,22),[('L',(14,14)),('A',10,10,True,(34,14))])
        self.relate('connect','body','shackle')
        circle('keyhole',24,33,2)
