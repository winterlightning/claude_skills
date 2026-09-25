"""Two workflow columns, three identical circular nodes and detached cross endpoint. Shared radius6; exact cardinal stem attachments, symmetric cross with central junction.
Lucide git-pull-request-closed: repeated circular nodes, stems and cross.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '387cccb6-81ba-437c-8e8c-5ee228aa94de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'workflow-connections-with-cross-endpoint-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('workflow', 'connections', 'with', 'cross', 'endpoint')

    def build(self):

        def circle(name, x, y, r):
            points=((x-r,y),(x,y-r),(x+r,y),(x,y+r))
            members=[]
            for i in range(4):
                member=name+'-'+str(i)
                self.add_arc(member,points[i],points[(i+1)%4],radius_x=r)
                members.append(member)
            self.add_contour(name,*members,closed=True)

        for n,x,y in [('upper-left',12,12),('lower-left',12,36),('lower-right',36,36)]: circle(n,x,y,6)
        self.add_line('left-stem',(12,18),(12,30))
        for n in ('upper-left','lower-left'): self.relate('connect','left-stem',n)
        self.add_line('right-stem',(36,24),(36,30))
        self.relate('connect','right-stem','lower-right')
        self.add_polyline('cross-one',(30,6),(36,12),(42,18))
        self.add_polyline('cross-two',(30,18),(36,12),(42,6))
        self.relate('connect','cross-one','cross-two')
