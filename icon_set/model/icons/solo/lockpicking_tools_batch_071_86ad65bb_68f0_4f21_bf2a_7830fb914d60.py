"""05-lockpicking-tool-set--86ad65bb-68f0-4f21-bf2a-7830fb914d60
Plan: Three independent picks with a repeated 8-unit-wide capsule handle and 16-unit spacing. Centerline extremes (4,8)-(44,40).
Construction: No useful Lucide match found.
Reduction: Secondary prong omitted to keep separated pick tips readable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86ad65bb-68f0-4f21-bf2a-7830fb914d60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tools loackpick 1_86ad65bb-68f0-4f21-bf2a-7830fb914d60.svg'
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


class Batch071Icon05(Solo48):
    icon_id = 'lockpicking-tools-batch-071'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('lockpicking', 'tools')

    def build(self):
        for i,x in enumerate((8,24,40)):
            _path(self,f'handle-{i}',(x-4,28),[((x,24),4,4,True),((x+4,28),4,4,True),((x+4,36),),((x-4,36),4,4,True),((x-4,28),)],True)
            if i==0: self.add_polyline(f'pick-{i}',(x,24),(x,8),(x+6,8))
            elif i==1: self.add_polyline(f'pick-{i}',(x,24),(x,16),(x+4,12),(x,8))
            else: self.add_polyline(f'pick-{i}',(x,24),(x,12),(x+4,8))
            self.relate('connect',f'handle-{i}',f'pick-{i}')
