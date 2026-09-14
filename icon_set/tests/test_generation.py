"""Candidate isolation, explicit publishing, and rollback without calling a paid model."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from icon_set.scripts.generation import GenerationManager

class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.manager=GenerationManager(self.root,self.root/'dist',self.root/'data/jobs')
        (self.root/'icon_set/model/icons/sub').mkdir(parents=True)
        self.old=self.root/'icon_set/model/icons/sub/old.py';self.old.write_text('# original')
        self.row=dict(id='a'*32,status='running',mode='generate',name='Mark',prompt='A small mark',family='sub',model='',source=None)
        self.manager.write(self.row)

    def snapshot(self,destination):
        import shutil
        shutil.copytree(self.root/'icon_set',destination/'icon_set')
        from icon_set.scripts.generation import digest
        return {'icon_set/model/icons/sub/old.py':digest(self.old)}

    def agent(self,args,cwd,log):
        (cwd/'icon_set/model/icons/sub/new_mark.py').write_text('# candidate')
        (cwd/'candidate.json').write_text(json.dumps(dict(path='icon_set/model/icons/sub/new_mark.py',family='sub',icon_id='new-mark')))

    def build(self,workspace,family,log,dist=None,icon=None):
        gallery=workspace/'icon_set/dist/gallery';gallery.mkdir(parents=True,exist_ok=True)
        (gallery/'icons.json').write_text(json.dumps({'icons':[{'icon_id':'new-mark','key':'sub/new-mark','family':'sub','preview_url':'../sub32/new-mark.svg','python_source':{'path':'icon_set/model/icons/sub/new_mark.py'}}]}))
        svg=workspace/'icon_set/dist/sub32/new-mark.svg';svg.parent.mkdir(exist_ok=True);svg.write_text('<svg/>')

    def candidate(self):
        with patch.object(self.manager,'snapshot',self.snapshot),patch.object(self.manager,'command',self.agent),patch.object(self.manager,'build',self.build):
            self.manager.run(self.row)
        row=self.manager.read(self.row['id']);self.assertEqual(row['status'],'candidate',row)
        self.assertFalse((self.root/row['path']).exists())
        return row

    def test_candidate_can_be_discarded_without_touching_library(self):
        row=self.candidate();self.manager.decide(row['id'],False)
        self.assertFalse((self.manager.folder(row['id'])/'workspace').exists())
        self.assertEqual(self.old.read_text(),'# original')
        self.assertEqual(self.manager.read(row['id'])['status'],'discarded')

    def test_accept_publishes_only_new_file(self):
        row=self.candidate()
        with patch.object(self.manager,'build') as build:
            self.manager.accept(row)
        self.assertEqual((self.root/row['path']).read_text(),'# candidate')
        self.assertEqual(self.old.read_text(),'# original')
        self.assertEqual(self.manager.read(row['id'])['status'],'accepted');build.assert_called_once()

    def test_failed_build_rolls_back_and_collision_never_overwrites(self):
        row=self.candidate()
        with patch.object(self.manager,'build',side_effect=ValueError('invalid geometry')):
            self.manager.accept(row)
        target=self.root/row['path'];self.assertFalse(target.exists())
        target.write_text('# another accepted icon')
        self.manager.accept(row)
        self.assertEqual(target.read_text(),'# another accepted icon')
        self.assertEqual(self.manager.read(row['id'])['status'],'candidate')

    def test_agent_editing_existing_file_is_rejected(self):
        def bad(*args):
            self.agent(*args)
            (args[1]/'icon_set/model/icons/sub/old.py').write_text('# modified')
        with patch.object(self.manager,'snapshot',self.snapshot),patch.object(self.manager,'command',bad):
            self.manager.run(self.row)
        self.assertEqual(self.manager.read(self.row['id'])['status'],'failed')
        self.assertEqual(self.old.read_text(),'# original')

    def test_reference_images_reach_the_agent_workspace_and_prompt(self):
        from icon_set.scripts.reference_images import ReferenceStore
        store=ReferenceStore(self.root/'data/refs');self.manager.references=store
        png=store.save('Shape.png',b'\x89PNG\r\n\x1a\n'+b'\x00'*16)
        svg=store.save('outline.svg',b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="20" height="10"/></svg>')
        calls=[]
        def agent(args,cwd,log):
            calls.append(args);self.agent(args,cwd,log)
        with self.assertRaises(ValueError):
            self.manager.start({'mode':'generate','name':'x','prompt':'x','family':'sub','reference_images':['f'*64]},{})
        row=dict(self.row,reference_images=[png,svg])
        with patch.object(self.manager,'snapshot',self.snapshot),patch.object(self.manager,'command',agent),patch.object(self.manager,'build',self.build):
            self.manager.run(row)
        self.assertEqual(self.manager.read(row['id'])['status'],'candidate')
        workspace=self.manager.folder(row['id'])/'workspace'
        self.assertEqual((workspace/'reference-images/01-shape.png').read_bytes(),store.path(png['id']).read_bytes())
        self.assertTrue((workspace/'reference-images/02-outline.svg').is_file())
        request=json.loads((self.manager.folder(row['id'])/'prompt.txt').read_text().rsplit('(JSON)',1)[1])
        self.assertEqual([item['path'] for item in request['reference_images']],['reference-images/01-shape.png','reference-images/02-outline.svg'])
        self.assertEqual(request['reference_images'][1]['preview_png'],'reference-images/02-outline.preview.png')
        self.assertTrue((workspace/'reference-images/02-outline.preview.png').read_bytes().startswith(b'\x89PNG'))
        self.assertEqual(calls[0][5:],[str(workspace/'reference-images/01-shape.png'),str(workspace/'reference-images/02-outline.preview.png')])

    def test_invalid_request_and_job_paths(self):
        with self.assertRaises(ValueError):self.manager.folder('../escape')
        with self.assertRaises(ValueError):self.manager.start({'mode':'generate','name':'x','prompt':'x','family':'bad'}, {})
        with self.assertRaises(ValueError):self.manager.start({'mode':'fix','name':'x','prompt':'x','family':'sub','icon':'missing'}, {})
