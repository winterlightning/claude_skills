"""A person gestures toward a pair of musical notes.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Outlined torso reduced to the shared human line vocabulary; both notes retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8fed7998-a482-495d-a5a5-6b6237429d87'
SOURCE_PATH='icon_set/work/todo-references/music making_8fed7998-a482-495d-a5a5-6b6237429d87.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='music-making'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('music', 'making')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.circle('head',16,12,6)
        self.add_line('torso',(16,26),(16,42))
        self.add_bezier('left-shoulder',(6,42),((6,30),(6,26),(16,26)))
        self.add_polyline('arm',(16,26),(26,32),(42,32))
        self.relate('connect','torso','left-shoulder');self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.circle('note-left',32,18,2);self.circle('note-right',40,16,2)
        self.add_polyline('beam',(34,18),(34,8),(42,6),(42,16))
        self.relate('connect','beam','note-left');self.relate('connect','beam','note-right')

# Final visible bounds: (4, 4, 44, 44)
# Construction: Shared human references supplied round heads, broad shoulders and coherent pose construction. Analytical head/body spacing is recorded in the visual review. Lucide music supplied paired notehead/stem construction.
# Final reductions: Outlined torso reduced to the shared human line vocabulary; both notes retained.
# Visual review: Gesture and two notes remain identifiable. Head center(16,12), radius6 ends at18; torso begins(16,26), so26-18-4=4 visible ink gap. Head aligns with torso axis. Human figure flag is recorded.
