"""Fresh reconstruction of phone vertical from the supplied reference.
Construction references: Lucide phone. Symbol plan recorded in build().
Profile SOLO48, keyshape VRECT_M; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c77144a9-35d2-4377-bddd-6845d3a0bbad'
SOURCE_PATH = 'pictographic-primitives/other/phone vertical_c77144a9-35d2-4377-bddd-6845d3a0bbad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-telephone-handset'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('phone', 'vertical')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(n+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def box(self,n,l,t,r,b,k=4,top=(),bottom=()):
        p=[(l+k,t),*[(x,t) for x in sorted(top)],(r-k,t),(r,t+k),(r,b-k),(r-k,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,(a,z) in enumerate(zip(p,p[1:]+p[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if a[0]!=z[0] and a[1]!=z[1]:self.add_arc(name,a,z,radius_x=k)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Bowed outer back and slanted terminal faces; upper/lower halves mirror about y24.
        self.add_bezier('back',(28,4),((15,4),(10,14),(10,24)),((10,34),(15,44),(28,44)))
        self.add_line('bottom',(28,44),(34,44))
        self.add_bezier('lower-tip',(34,44),((37,44),(38,43),(38,40)))
        self.add_bezier('lower-slant',(38,40),((38,38),(37,36),(36,34)))
        self.add_bezier('lower-return',(36,34),((35,32),(34,32),(30,32)))
        self.add_line('lower-grip',(30,32),(26,32))
        self.add_bezier('grip',(26,32),((22,32),(22,28),(22,24)),((22,20),(22,16),(26,16)))
        self.add_line('upper-grip',(26,16),(30,16))
        self.add_bezier('upper-return',(30,16),((34,16),(35,16),(36,14)))
        self.add_bezier('upper-slant',(36,14),((37,12),(38,10),(38,8)))
        self.add_bezier('upper-tip',(38,8),((38,5),(37,4),(34,4)))
        self.add_line('top',(34,4),(28,4))
        self.add_contour('receiver','back','bottom','lower-tip','lower-slant','lower-return','lower-grip','grip','upper-grip','upper-return','upper-slant','upper-tip','top',closed=True)
