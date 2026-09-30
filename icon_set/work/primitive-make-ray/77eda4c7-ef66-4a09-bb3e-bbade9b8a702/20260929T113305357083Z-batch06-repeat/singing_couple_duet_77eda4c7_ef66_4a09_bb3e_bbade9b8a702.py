"""The rejected duet replaced both differently dressed singers with identical stick figures. Restored a skirt on the right singer while retaining the left trousered figure and a central musical note. Reduced two notes to one for spacing.
Plan: Human full_body_ref.png: circular heads and exact 4-unit detached head gap; Lucide music-2: note head, stem and flag. Keyshape HRECT_L; shared contour nodes and dimensions.
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

        for name,x in [('left',9),('right',39)]:
         circle(name+'-head',x,15,3)
         line(name+'-torso',(x,26),(x,32))
         poly(name+'-arms',(x-5,29),(x,26),(x+5,29));join(name+'-arms',name+'-torso')
         if name=='left':poly(name+'-legs',(x-4,40),(x,32),(x+4,40));join(name+'-legs',name+'-torso')
         else:
          poly('skirt',(34,38),(39,28),(44,38),(34,38));join('skirt','right-torso')
          line('leg-left',(36,38),(36,40));line('leg-right',(42,38),(42,40));join('leg-left','skirt');join('leg-right','skirt')
         self.mark_human_figure(name,head=name+'-head',torso=name+'-torso',torso_junction='start')
        circle('note',23,18,2);poly('stem',(25,18),(25,8),(29,10));join('stem','note')
