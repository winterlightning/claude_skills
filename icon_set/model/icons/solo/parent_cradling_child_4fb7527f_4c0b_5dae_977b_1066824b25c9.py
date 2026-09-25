"""Parent Carrying Child.
Plan: Adult at right cradles a child at left; flared garment and broad supporting arm. Extrema (8,4)-(40,44).
Reference: human_ref/full_body_ref.png: circular heads and flared garment; asymmetric carried-child pose from source.
Reduction: Fine interior detail omitted to preserve negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fb7527f-4c0b-5dae-977b-1066824b25c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/family/parent carry kids babies_4fb7527f-4c0b-5dae-977b-1066824b25c9.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'parent-cradling-child'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "family"
    aliases = ()
    keywords = ('parent', 'carrying', 'child')

    def build(self):

        for name,x,y,r in (('adult',28,8,4),('child',11,23,3)):
            self.add_arc(name+'-head-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-head-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name+'-head',name+'-head-a',name+'-head-b',closed=True)
        self.add_polyline('adult-torso',(28,20),(40,44),(28,44))
        self.add_line('child-torso',(11,34),(11,38))
        self.add_bezier('cradle',(11,38),((28,38),(28,30),(28,20)))
        self.relate('connect','child-torso','cradle')
        self.relate('connect','adult-torso','cradle')
        self.mark_human_figure('adult',head='adult-head',torso='adult-torso-1',torso_junction='start')
        self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
