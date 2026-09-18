"""Trial previews retain provenance without claiming validated composition."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from icon_set.scripts.combination_catalog import write_catalog

class ContainerSoloTrialsTest(unittest.TestCase):
    def test_current_trial_is_separate_and_changed_inputs_hide_it(self):
        with TemporaryDirectory() as folder:
            root=Path(folder);gallery=root/'dist/gallery';gallery.mkdir(parents=True)
            data=root/'icon_set/data';data.mkdir(parents=True)
            asset=root/'icon_set/assets/container-solo-trials/pair.svg';asset.parent.mkdir(parents=True);asset.write_text('<svg/>')
            row={'id':'pair','main_id':'main-ref','sub_id':'sub-ref','concept':'Example'}
            (root/'combination_data.json').write_text(json.dumps({'container':[row]}))
            main={'key':'container/host','icon_id':'host','family':'container','preview_url':'host.svg','svg_sha256':'main-hash'}
            sub={'key':'solo/subject','icon_id':'subject','family':'solo','preview_url':'sub.svg','svg_sha256':'sub-hash'}
            primitives={'rows':[{'uuid':'main-ref','generated':[main]},{'uuid':'sub-ref','generated':[sub]}]}
            trial={'main_source_id':'main-ref','sub_source_id':'sub-ref','main_key':main['key'],'sub_key':sub['key'],'main_sha256':'main-hash','sub_sha256':'sub-hash','svg_file':'pair.svg','svg_sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'status':'review-fit','placement':{'stroke':4}}
            (data/'container-solo-trials.json').write_text(json.dumps({'results':{'pair':trial}}))
            def result():return write_catalog(gallery,primitives,[main,sub],root)['rows'][0]
            r=result();self.assertEqual(r['generated'],[]);self.assertFalse(r['trial_preview']['native_sub32']);self.assertTrue((gallery/r['trial_preview']['preview_url']).is_file())
            sub['svg_sha256']='edited';r=result();self.assertEqual(r['trial_status'],'stale');self.assertNotIn('trial_preview',r)
            sub['svg_sha256']='sub-hash';main['svg_sha256']='edited';self.assertEqual(result()['trial_status'],'stale')
            main['svg_sha256']='main-hash';asset.write_text('<svg>edited</svg>');self.assertEqual(result()['trial_status'],'stale')
            asset.unlink();self.assertEqual(result()['trial_status'],'stale')
