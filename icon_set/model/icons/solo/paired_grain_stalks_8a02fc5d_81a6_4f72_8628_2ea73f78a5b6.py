'Two staggered upright wheat stalks have paired upward grain branches. SQUARE preserves a broad paired silhouette. Shared stalk definition and 13-unit branch rhythm, intentionally staggered heights. Source supplies the paired arrangement; Lucide wheat supplies repeating grains along an axial stem. Open grain strokes replace densely overlapping leaf loops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a02fc5d-81a6-4f72-8628-2ea73f78a5b6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bread wheat_8a02fc5d-81a6-4f72-8628-2ea73f78a5b6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'paired-grain-stalks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Two Stalks of Wheat',)
    keywords = ('two', 'stalks', 'of', 'wheat')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        for name,x,top,levels in [('left',13,6,(22,35)),('right',35,14,(29,42))]:
            points=[top,*levels]
            for j,(a,b) in enumerate(zip(points,points[1:])):
                self.add_line(f'{name}-stem-{j}',(x,a),(x,b))
            if levels[-1]<42:
                self.add_line(f'{name}-tail',(x,levels[-1]),(x,42))
                self.relate('connect',f'{name}-tail',f'{name}-stem-1')
            self.relate('connect',f'{name}-stem-0',f'{name}-stem-1')
            for j,y in enumerate(levels):
                self.add_polyline(f'{name}-grains-{j}',(x-7,y-8),(x,y),(x+7,y-8))
                self.relate('connect',f'{name}-grains-{j}',f'{name}-stem-{j}')
                if j==0:self.relate('connect',f'{name}-grains-{j}',f'{name}-stem-1')
                if j==1 and y<42:self.relate('connect',f'{name}-grains-{j}',f'{name}-tail')
