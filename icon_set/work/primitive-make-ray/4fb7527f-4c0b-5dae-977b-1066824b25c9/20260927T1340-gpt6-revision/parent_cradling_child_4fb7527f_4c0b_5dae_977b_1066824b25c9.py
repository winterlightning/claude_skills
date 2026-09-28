"""Parent Carrying Child.
Plan: Adult at right cradles a child at left; flared garment and broad supporting arm. Extrema (8,4)-(40,44).
Reference: human_ref/full_body_ref.png: circular heads and flared garment; asymmetric carried-child pose from source.
Reduction: Fine interior detail omitted to preserve negative space.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4fb7527f-4c0b-5dae-977b-1066824b25c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__parent-cradling-child/20260927T133654Z-thuan-mac-1/reference/parent carry kids babies_4fb7527f-4c0b-5dae-977b-1066824b25c9.svg'
AUTHOR = "gpt-6"

class Batch27Icon(Solo48):
    icon_id = 'parent-cradling-child'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "family"
    categories = ("primitives", "family")
    aliases = ()
    keywords = ('parent', 'carrying', 'child')

    def build(self):
        # Adult and child keep the reference's size contrast. The long curved
        # arm reaches the child's shoulders, making the carrying action clear.
        for name,x,y,r in (('adult',29,9,5),('child',12,23,4)):
            self.add_arc(name+'-head-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-head-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name+'-head',name+'-head-a',name+'-head-b',closed=True)
        self.add_bezier('adult-back',(29,22),((35,25),(38,35),(40,44)))
        self.add_line('adult-hem',(40,44),(28,44))
        self.add_bezier('support-arm',(29,22),((25,29),(20,39),(12,37)))
        self.add_line('child-torso-upper',(12,35),(12,37))
        self.add_line('child-torso-lower',(12,37),(12,41))
        self.add_line('child-leg',(12,41),(8,44))
        self.relate('connect','adult-back','support-arm')
        self.relate('connect','adult-back','adult-hem')
        self.relate('connect','support-arm','child-torso-upper')
        self.relate('connect','support-arm','child-torso-lower')
        self.relate('connect','child-torso-upper','child-torso-lower')
        self.relate('connect','child-torso-lower','child-leg')
        self.mark_human_figure('adult',head='adult-head',torso='adult-back',torso_junction='start')
        self.mark_human_figure('child',head='child-head',torso='child-torso-upper',torso_junction='start')
