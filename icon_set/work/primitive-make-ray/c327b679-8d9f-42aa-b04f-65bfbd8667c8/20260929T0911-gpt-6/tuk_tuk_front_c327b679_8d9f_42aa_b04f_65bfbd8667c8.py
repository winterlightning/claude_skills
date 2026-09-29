from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'c327b679-8d9f-42aa-b04f-65bfbd8667c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tuk-tuk-front/20260929T090755Z-thuan-mac/reference/tuk tuk 1_c327b679-8d9f-42aa-b04f-65bfbd8667c8.svg'
AUTHOR = "gpt-6"
# Plan: Restore the tapered roof, wide windshield, two headlights and three visible tires.
# Keyshape: VRECT_L; preserve reference arrangement.
# Construction reference: truck.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'tuk-tuk-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'roof', 'M 12 15 L 15 6 A 3 3 1 18 4 L 30 4 A 3 3 1 33 6 L 36 15')
        _draw(self, 'body', 'M 12 15 L 36 15 L 36 33 C 36 36 34 37 29 37 M 19 37 C 14 37 12 36 12 33 L 12 15')
        _draw(self, 'windshield', 'M 12 23 L 36 23')
        _draw(self, 'left-lamp', 'M 16 29 A 2 2 1 20 29 A 2 2 1 16 29 Z')
        _draw(self, 'right-lamp', 'M 28 29 A 2 2 1 32 29 A 2 2 1 28 29 Z')
        _draw(self, 'tire', 'M 24 35 L 24 35 A 3 3 1 27 38 L 27 41 A 3 3 1 24 44 L 24 44 A 3 3 1 21 41 L 21 38 A 3 3 1 24 35 Z')
        _draw(self, 'left-wheel', 'M 12 29 L 8 29 L 8 41 A 3 3 0 14 41 L 14 37')
        _draw(self, 'right-wheel', 'M 36 29 L 40 29 L 40 41 A 3 3 1 34 41 L 34 37')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
