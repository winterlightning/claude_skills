from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2841f97c-3470-4026-a287-d82828da5d59'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/book library shelf_2841f97c-3470-4026-a287-d82828da5d59.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'row-of-four-library-books'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('row', 'of', 'four', 'library', 'books')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: SQUARE extremes6,6 to42,42; four equal open-top spines with round feet and two shared band heights.
        for i in range(4):
            x=6+10*i
            ys=[6,16,30,39]
            members=[]
            for j in range(3):
                name=f'book-{i}-left-{j}'; self.add_line(name,(x,ys[j]),(x,ys[j+1])); members.append(name)
            name=f'book-{i}-foot'; self.add_arc(name,(x,39),(x+6,39),radius_x=3,sweep=False); members.append(name)
            for j in reversed(range(3)):
                name=f'book-{i}-right-{j}'; self.add_line(name,(x+6,ys[j+1]),(x+6,ys[j])); members.append(name)
            self.add_contour(f'book-{i}',*members)
            for j,y in enumerate((16,30)):
                self.add_line(f'book-{i}-band-{j}',(x,y),(x+6,y))
                self.relate('connect',f'book-{i}',f'book-{i}-band-{j}')
