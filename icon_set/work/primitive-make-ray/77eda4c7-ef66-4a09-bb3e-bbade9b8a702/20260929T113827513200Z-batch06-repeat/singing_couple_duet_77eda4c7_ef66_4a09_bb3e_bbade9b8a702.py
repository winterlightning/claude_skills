"""The rejected duet used two identical stick figures. Restored the right singer in a dress and the left singer in trousers with a central musical note. Both heads have an exact four-unit ink gap to their bodies; reduced two notes to one.
Plan: Human full_body_ref.png: circular heads and exact 4-unit detached head gap; Lucide music-2: note head and stem. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='77eda4c7-ef66-4a09-bb3e-bbade9b8a702'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__singing-couple-duet/20260929T112716Z-thuan-mac/reference/concert couple duet_77eda4c7-ef66-4a09-bb3e-bbade9b8a702.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='singing-couple-duet'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        circle('left-head',9,15,3)
        line('left-torso',(9,26),(9,32));poly('left-arms',(4,29),(9,26),(14,29));join('left-arms','left-torso')
        poly('left-legs',(5,40),(9,32),(13,40));join('left-legs','left-torso')
        self.mark_human_figure('left',head='left-head',torso='left-torso',torso_junction='start')
        circle('right-head',36,11,3)
        poly('dress',(36,22),(44,36),(40,36),(32,36),(28,36),(36,22))
        line('right-leg-left',(32,36),(32,40));line('right-leg-right',(40,36),(40,40));join('right-leg-left','dress');join('right-leg-right','dress')
        circle('note',23,18,2);line('stem',(25,18),(25,8));join('stem','note')
