"""freeCodeCamp flame enclosed by curved parentheses.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape HRECT_L; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: None; asymmetric outer flame and inner return retained.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='88e5f419-7545-4a1a-86c8-dc50363f1c62'
SOURCE_PATH='icon_set/work/todo-references/freecodecamp logo_88e5f419-7545-4a1a-86c8-dc50363f1c62.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='freecodecamp-logo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('freecodecamp', 'logo')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, w, h, r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}';ids.append(eid)
            if i%2:self.add_arc(eid,pts[i],pts[(i+1)%8],radius_x=r)
            else:self.add_line(eid,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):

        self.add_arc('left-parenthesis',(8,12),(4,26),radius_x=4,radius_y=14,sweep=False)
        self.add_arc('left-bottom',(4,26),(8,40),radius_x=4,radius_y=14,sweep=False)
        self.add_contour('left-bracket','left-parenthesis','left-bottom')
        self.add_arc('right-parenthesis',(40,12),(44,26),radius_x=4,radius_y=14)
        self.add_arc('right-bottom',(44,26),(40,40),radius_x=4,radius_y=14)
        self.add_contour('right-bracket','right-parenthesis','right-bottom')
        self.add_bezier('flame',(20,40),((9,31),(28,23),(22,8)),((32,15),(26,24),(29,27)),((31,29),(32,25),(33,24)),((37,34),(31,40),(28,40)),((31,35),(25,34),(26,28)),((21,33),(19,36),(20,40)))
        self.add_contour('flame-outline','flame',closed=True)

