"""11-orchestral-kettle-drum-with-mallet--e741ba87-f0cf-4f42-86e9-31edb31ab75b
Plan: An elliptical rim sits over a circular bowl split at exact integer attachment nodes (13,34), (22,37), (31,34). Three legs share the lower baseline; a separate angled mallet sits above. Centerline extremes (6,6)-(42,42).
Construction: Lucide drum: oval skin over a curved body.
Reduction: Tuning hardware removed; mallet floats above the drum to preserve clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e741ba87-f0cf-4f42-86e9-31edb31ab75b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/timpani_e741ba87-f0cf-4f42-86e9-31edb31ab75b.svg'
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


class Batch071Icon11(Solo48):
    icon_id = 'timpani-and-mallet-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('timpani', 'and', 'mallet')

    def build(self):
        _path(self,'rim',(7,22),[((37,22),15,4,True),((7,22),15,4,True)],True)
        _path(self,'bowl',(7,22),[((13,34),15,15,False),((22,37),15,15,False),((31,34),15,15,False),((37,22),15,15,False)])
        self.relate('connect','rim','bowl')
        self.add_line('leg-left',(13,34),(6,42)); self.add_line('leg-right',(31,34),(38,42))
        self.add_line('leg-center',(22,37),(22,42))
        for n in ('left','right','center'): self.relate('connect',f'leg-{n}','bowl')
        _circle(self,'mallet-head',39,9,3)
        self.add_line('mallet-shaft',(36,9),(24,6))
        self.relate('connect','mallet-head','mallet-shaft')
