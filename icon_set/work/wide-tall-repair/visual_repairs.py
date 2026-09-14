from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
def fix(id,fn,note):
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('visual_repaired'):return
 fn(x['record']);x['visual_repaired']=True;x['manual_note']=x.get('manual_note','')+' '+note;q=check(f,x);print(id,q['status'],q['internal_spacing']['status'],q['errors']+q['warnings'],q['internal_spacing'].get('findings'),flush=True)
if __name__=='__main__':
 def hexbeads(r):
  reset(r);circle(r,'bead-left',10,10,4);circle(r,'bead-right',38,10,4);line(r,'wire-left',(10,14),(24,26));line(r,'wire-right',(38,14),(24,26));poly(r,'stone',[(24,26),(33,32),(33,36),(24,42),(15,36),(15,32)],True)
  for a,b in [('bead-left','wire-left'),('bead-right','wire-right'),('wire-left','wire-right'),('wire-left','stone'),('wire-right','stone')]:rel(r,a,b)
 fix('beaded-necklace-with-hexagon-stone',hexbeads,'Visual review restored two readable hollow beads; the remaining bead pairs were omitted.')
 def buds(r):
  remove(r,['top']);circle(r,'top',22,8,4);by(r,'stem')['end']=[22,12];by(r,'twig-1').update(start=[8,14],end=[22,22]);by(r,'twig-2').update(start=[22,22],end=[36,14]);by(r,'left').update(start=[8,14],end=[8,14]);by(r,'right').update(start=[36,14],end=[36,14]);rel(r,'top','stem')
 fix('bud-branch-in-pitcher',buds,'Visual review restored one clear circular bud above two simple twigs.')
 def lamb(r):
  reset(r)
  arc(r,'fleece-top',(12,12),(36,12),12,6);arc(r,'fleece-right',(36,12),(36,36),6,12);arc(r,'fleece-bottom',(36,36),(12,36),12,6);arc(r,'fleece-left',(12,36),(12,12),6,12);contour(r,'fleece','fleece-top','fleece-right','fleece-bottom','fleece-left',closed=True)
  arc(r,'face-top',(18,22),(30,22),6,7);poly(r,'ear-right',[(30,22),(33,26),(30,26)]);arc(r,'jaw-right',(30,26),(24,33),6,7);arc(r,'jaw-left',(24,33),(18,26),6,7);poly(r,'ear-left',[(18,26),(15,26),(18,22)]);contour(r,'face','face-top','ear-right-0','ear-right-1','jaw-right','jaw-left','ear-left-0','ear-left-1',closed=True);r['contours']=[c for c in r['contours'] if c['contour_id'] not in ['ear-left','ear-right']]
  line(r,'leg-left',(12,36),(10,40));line(r,'leg-right',(36,36),(38,40));rel(r,'fleece','leg-left');rel(r,'fleece','leg-right')
 for id in ['fluffy-lamb-front','woolly-lamb-front']:fix(id,lamb,'Visual review restored an elongated sheep face and paired ears inside four broad fleece lobes.')
 def links(r):
  reset(r);poly(r,'lower',[(12,30),(15,33),(18,36),(12,42),(6,36)],True);poly(r,'middle',[(24,18),(27,21),(30,24),(24,30),(21,27),(18,24)],True);poly(r,'upper',[(36,6),(42,12),(36,18),(33,15),(30,12)],True);line(r,'join-lower',(15,33),(21,27));line(r,'join-upper',(27,21),(33,15))
  for a,b in [('lower','join-lower'),('middle','join-lower'),('middle','join-upper'),('upper','join-upper')]:rel(r,a,b)
 fix('rhombus-chain-links',links,'Visual review rebuilt all three equal links from a shared six-unit radius and twelve-unit diagonal step.')
 def monkey(r):
  src=json.loads((W/'candidates/monkey-head.json').read_text())['record']
  for k in ['primitives','contours','relationships','keyshape']:r[k]=src[k]
 fix('monkey-face',monkey,'Used the inspected monkey-head construction to restore the broad muzzle and paired eyes instead of a small circular face panel.')
