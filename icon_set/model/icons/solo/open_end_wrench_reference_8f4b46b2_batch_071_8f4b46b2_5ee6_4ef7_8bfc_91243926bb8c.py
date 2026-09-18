"""07-mechanical-repair-wrench-tool--8f4b46b2-5ee6-4ef7-8bfc-91243926bb8c
Plan: Diagonal open jaw joined to a broad round-ended handle. Extremes (6,6)-(42,42).
Construction: Lucide wrench: continuous jaw and handle contour.
Reduction: Handle hole omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f4b46b2-5ee6-4ef7-8bfc-91243926bb8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tool_8f4b46b2-5ee6-4ef7-8bfc-91243926bb8c.svg'
AUTHOR = 'gpt-6'

def _path(icon, name, start, steps, closed=False):
    members=[]
    for i, step in enumerate(steps):
        end=step[0]; member=f'{name}-{i}'
        if len(step)==1: icon.add_line(member,start,end)
        else: icon.add_arc(member,start,end,radius_x=step[1],radius_y=step[2],sweep=step[3])
        members.append(member); start=end
    icon.add_contour(name,*members,closed=closed)


def _circle(icon,name,x,y,r):
    _path(icon,name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)


class Batch071Icon07(Solo48):
    icon_id = 'open-end-wrench-reference-8f4b46b2-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('open', 'end', 'wrench', 'reference', '8f4b46b2')

    def build(self):
        _path(self,'outline',(30,6),[((18,18),12,12,False),((18,22),),((8,32),),((6,36),5,5,False),((12,42),6,6,False),((16,40),5,5,False),((28,28),),((42,14),14,14,False),((32,19),),((26,15),),((30,6),)],True)
