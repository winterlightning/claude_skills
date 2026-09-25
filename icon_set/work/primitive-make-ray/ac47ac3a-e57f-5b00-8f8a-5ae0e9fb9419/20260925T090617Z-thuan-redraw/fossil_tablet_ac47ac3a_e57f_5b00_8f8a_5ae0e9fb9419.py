"""Restore the complete angular pterosaur skeleton with head, spine, spread limbs and tail inside a rounded stone tablet.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: none (bone inspected; no useful skeleton match). Original reference establishes full subject and arrangement.
Keyshape SQUARE; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fossil-tablet/20260925T090617Z-thuan-mac/reference/dinosaur pteranodon fossil_ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fossil-tablet'
    keyshape=Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('fossil', 'tablet')
    def build(self):

        self.box('tablet',6,6,42,42,6)
        # Spine owns all branch nodes; deliberate asymmetry follows fossil pose.
        self.add_polyline('spine',(22,13),(18,19),(23,25),(28,29),(30,37))
        self.add_line('beak',(14,19),(18,19));self.relate('connect','beak','spine')
        self.add_polyline('upper-wing',(23,25),(30,21),(29,16),(34,14));self.relate('connect','upper-wing','spine')
        self.add_polyline('left-wing',(28,29),(21,32),(15,29),(13,36));self.relate('connect','left-wing','spine')
        self.add_polyline('right-leg',(30,37),(35,30),(38,32));self.relate('connect','right-leg','spine')
        self.add_line('tail',(30,37),(25,37));self.relate('connect','tail','spine');self.relate('connect','tail','right-leg')


    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


