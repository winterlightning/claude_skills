"""02-human-chest-and-shoulders--ddb63472-2688-488c-978b-5b250d2f3dcd
Plan: Mirrored neck, shoulder quarter circles, open arm and waist strokes. Extremes (6,6)-(42,42).
Construction: Human user.svg and full_body_ref.png.
Reduction: Chest muscle detail omitted; preserved continuous neck, broad shoulders and cropped arms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddb63472-2688-488c-978b-5b250d2f3dcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/torso_ddb63472-2688-488c-978b-5b250d2f3dcd.svg'
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


class Batch071Icon02(Solo48):
    icon_id = 'human-upper-torso-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('human', 'upper', 'torso')

    def build(self):

        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            _path(self,f'outer-{side}',p(6,6),[(p(6,10),),(p(10,14),4,4,side<0),(p(18,22),8,8,side>0),(p(18,42),)])
            self.add_line(f'inner-arm-{side}',p(9,25),p(9,42))
