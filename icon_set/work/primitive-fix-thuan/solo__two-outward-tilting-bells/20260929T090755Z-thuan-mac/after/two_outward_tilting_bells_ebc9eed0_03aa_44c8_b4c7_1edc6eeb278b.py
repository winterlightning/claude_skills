from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ebc9eed0-03aa-44c8-b4c7-1edc6eeb278b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-outward-tilting-bells/20260929T090755Z-thuan-mac/reference/christmas bells 1_ebc9eed0-03aa-44c8-b4c7-1edc6eeb278b.svg'
AUTHOR = "gpt-6"
# Plan: Angle two bell bodies away from their shared crown; use slanted rims and curved clappers.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: bell.

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
    icon_id = 'two-outward-tilting-bells'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'Preserve outward-tilted bells with curved clappers and their shared crown; compact central opening and tilted envelope are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9f2a4fb03cab3dc49eb49c5f9494d7b56ad8651cd0e531dc2f5342e75094dcfc'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'left', 'M 24 15 C 23 7 15 6 11 12 C 8 17 11 22 4 29 L 23 35 C 20 29 20 25 23 19 C 24 17 24 16 24 15 Z')
        _draw(self, 'right', 'M 24 15 C 25 7 33 6 37 12 C 40 17 37 22 44 29 L 25 35 C 28 29 28 25 25 19 C 24 17 24 16 24 15 Z')
        _draw(self, 'clapper-left', 'M 10 31 C 8 38 14 42 17 34')
        _draw(self, 'clapper-right', 'M 38 31 C 40 38 34 42 31 34')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
