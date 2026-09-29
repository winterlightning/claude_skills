"""Standalone primitive-make-ray revisions; exact source identities retained per input."""
from pathlib import Path
import json
import sys
import datetime

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = 'per-input: see specs and emitted module'
SOURCE_PATH = 'per-input: claimed reference path'

SPECS = {
'low-crescent-with-two-sparkles': dict(
    keyshape='SQUARE',
    before='The current crescent is blunt and hooked, and two crosses replace the original four-point sparkles.',
    change='Restored the diagonal crescent silhouette and two pointed four-point sparkles; smooth continuous moon curves replace the hooked bottom.',
    refs='Lucide moon and sparkles: coherent crescent contour and four-point sparkle construction. Intentional upper-right sparkle arrangement follows the original.',
    plan='One crescent contour and two four-point sparkle instances with shared axes. Ink extremes (4,4)-(44,44).',
    body="""
        curve('outer-a',(17,8),(10,10),(6,19),(6,28))
        curve('outer-b',(6,28),(6,37),(14,42),(23,42))
        curve('outer-c',(23,42),(31,42),(37,37),(39,31))
        curve('inner-a',(39,31),(31,37),(21,33),(16,27))
        curve('inner-b',(16,27),(11,21),(12,14),(17,8))
        self.add_contour('crescent','outer-a','outer-b','outer-c','inner-a','inner-b',closed=True)
        for name,x,y,r in [('large',35,13,7),('small',25,25,5)]:
            # Shared point order and inward-curving sides preserve four equal rays.
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            ids=[]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                part=f'{name}-{j}'
                self.add_arc(part,a,b,radius_x=r,sweep=False)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)
"""),
'reflective-safety-vest':dict(
    keyshape='VRECT_L',
    before='The current vest has abrupt stepped armholes and heavy corners instead of the original curved sleeveless outline.',
    change='Rebuilt mirrored curved armholes, rounded shoulders and hem, a centered V neck and seam, and two evenly spaced reflective-band edges.',
    refs='Lucide shirt: rounded garment contours and intrinsic neckline. The original establishes the sleeveless armholes and reflective strip.',
    plan='A symmetric vest outline owns shoulder radius, curved armholes, central seam and two band edges; x symmetry axis 24. Ink extremes (6,2)-(42,46).',
    body="""
        path('outline',(16,4),[
            ('L',(24,20)),('L',(32,4)),('L',(34,4)),
            ('A',(38,8),4,True),('L',(38,12)),
            ('C',(40,22),(38,17),(39,20)),
            ('L',(40,28)),('L',(40,36)),('L',(40,40)),
            ('A',(36,44),4,True),('L',(24,44)),('L',(12,44)),
            ('A',(8,40),4,True),('L',(8,36)),('L',(8,28)),('L',(8,22)),
            ('C',(10,12),(9,20),(10,17)),('L',(10,8)),
            ('A',(14,4),4,True),('L',(16,4))],True)
        self.add_polyline('seam',(24,20),(24,28),(24,36),(24,44))
        self.relate('connect','outline','seam')
        for j,y in enumerate((28,36)):
            name=f'band-{j}'
            self.add_polyline(name,(8,y),(24,y),(40,y))
            self.relate('connect',name,'outline')
            self.relate('connect',name,'seam')
"""),
'refresh-token-loop':dict(
    keyshape='SQUARE',
    before='The current inner loop is joined to the coin and the outer loop ends in an uneven short bend; the reference has two clean concentric open loops and a separate token.',
    change='Rebuilt concentric three-quarter circles and detached the circular token, restoring the open lower-right sector.',
    refs='Lucide rotate-cw: continuous circular sweep; source keeps two loops without an arrow. Deliberate open lower-right sector accommodates the separate coin.',
    plan='Two concentric circles centered at (21,21) with radii 15 and 8, open in the lower-right quadrant; token centered (35,35), radius 7. Ink extremes (4,4)-(44,44).',
    body="""
        for name,r in [('outer',15),('inner',8)]:
            x=y=21
            path(name,(x+r,y),[('A',(x,y-r),r,False),('A',(x-r,y),r,False),('A',(x,y+r),r,False)])
        circle('token',35,35,7)
"""),
'running-track-curve-arrow':dict(
    keyshape='SQUARE',
    before='The current direction arrow collapses into a thick triangular wedge; the track and arrow lack the clean open strokes of the original.',
    change='Used two concentric semicircular track lanes with tangent straights and a balanced open arrowhead with a visible shaft.',
    refs='Lucide undo-2: a semicircular turn with tangent straight sections and an open chevron arrowhead. The source sets the rightward direction.',
    plan='Two lane contours share center (24,24) and radii 18 and 10; separate right-facing arrow centered at y28. Ink extremes (4,4)-(44,44).',
    body="""
        for name,r,end in [('outer',18,42),('inner',10,25)]:
            path(name,(42,24-r),[('L',(24,24-r)),('A',(24,24+r),r,False),('L',(end,24+r))])
        self.add_polyline('arrowhead',(34,21),(42,28),(34,35))
        self.add_line('shaft',(31,28),(42,28))
        self.relate('connect','arrowhead','shaft')
"""),
'saving-bull':dict(
    keyshape='HRECT_L',
    before='The current animal faces the wrong way and has a flat angular body and stick legs; it loses the reference bull\'s lowered head, arched back and broad planted legs.',
    change='Restored a left-facing lowered head with a curved horn, arched back, outlined planted legs and a rising financial arrow.',
    refs='Lucide piggy-bank: continuous animal outline with integrated legs. No exact local bull match; the original owns the horn, lowered head and arched back. Intentional natural asymmetry.',
    plan='One coherent body contour with integrated foreleg and hindleg; separate curved horn and rising trend arrow. Ink extremes (2,6)-(46,42).',
    body="""
        path('body',(8,25),[
            ('C',(21,18),(13,21),(16,16)),
            ('C',(36,24),(27,18),(30,23)),
            ('A',(42,30),6,True),('L',(41,35)),('L',(39,40)),
            ('L',(33,40)),('L',(35,33)),('L',(24,33)),
            ('L',(19,40)),('L',(13,40)),('L',(17,32)),
            ('C',(12,29),(18,28),(14,26)),
            ('C',(8,36),(10,31),(11,36)),
            ('C',(4,31),(5,36),(4,34)),('L',(8,25))],True)
        curve('horn',(8,25),(8,21),(4,19),(4,17))
        self.relate('connect','horn','body')
        self.add_line('tail',(42,30),(44,38))
        self.relate('connect','tail','body')
        self.add_line('trend',(29,18),(42,8))
        self.add_polyline('arrow',(34,8),(42,8),(42,16))
        self.relate('connect','trend','arrow')
"""),
}

HELPERS = '''
        def curve(name,start,c1,c2,end):
            self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start
            ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L': self.add_line(part,point,end)
                elif kind=='A': self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                elif kind=='C': curve(part,point,args[0],args[1],end)
                ids.append(part)
                point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
'''

def author(icon_id, attempt='01'):
    spec=SPECS[icon_id]
    fix=ROOT/'icon_set/work/primitive-fix-thuan'/('solo__'+icon_id)/'20260928T175139Z-thuan-mac'
    ref=next((fix/'reference').glob('*.svg')).relative_to(ROOT)
    uid=ref.stem[-36:]
    concept=ref.stem[:-37]
    out=ROOT/'icon_set/work/primitive-make-ray'/uid/('20260928-thuan-mac-fix-'+attempt)
    out.mkdir(parents=True,exist_ok=False)
    meta=dict(concept=concept,source_uuid=uid,reference_path=str(ref),icon_id=icon_id,author=AUTHOR,
              feedback='Bad stroke drawn',comparison=spec['before'],changes=spec['change'],construction_reference=spec['refs'],plan=spec['plan'])
    (out/(icon_id+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
    (out/'review-before.md').write_text(spec['before']+'\n\nFeedback: Bad stroke drawn\n\n'+spec['change']+'\n')
    name=icon_id.replace('-','_')+'_'+uid.replace('-','_')+'.py'
    source=f'''"""{spec['plan']}\n{spec['refs']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{spec['keyshape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(icon_id.split('-'))!r}

    def build(self):
'''+HELPERS+spec['body']
    (out/name).write_text(source)
    return out

if __name__=='__main__':
    paths=[str(author(k)) for k in SPECS]
    (Path(__file__).parent/'runs.json').write_text(json.dumps(paths,indent=2)+'\n')
    print('\n'.join(paths))
