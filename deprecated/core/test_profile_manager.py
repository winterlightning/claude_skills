#!/usr/bin/env python3
"""Profile management persistence, API boundaries, and live configuration tests."""
from __future__ import annotations

from copy import deepcopy
import http.client
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import threading
import unittest
from unittest.mock import patch

import profile_manager as manager


class ProfileFixture:
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        for folder in ("core", "frontend/js", "frontend/css", "docs/icons", "docs/sub-icons", "docs/container-icons"):
            (self.root / folder).mkdir(parents=True)
        self.configuration = manager.validated_configuration(json.loads((manager.ROOT / "core/icon_profiles.json").read_text()))
        self.store = manager.ProfileStore(self.root)
        self.store.configuration_path.write_bytes(manager.json_bytes(self.configuration))
        for path, content in manager.configuration_assets(self.configuration, self.root).items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        self.initial = self.store.read()

    def candidate(self):
        source = deepcopy(self.configuration)
        source["profiles"]["badge"] = {
            "label": "Badge", "canvas": 40, "strokeWidth": 3,
            "keyshapes": [{"name": "badge-square", "orientation": "square", "shape": "rect", "width": 32, "height": 32}],
        }
        return source

    def snapshot(self):
        paths = [self.store.configuration_path, *manager.configuration_assets(self.configuration, self.root)]
        return {path: path.read_bytes() for path in paths}


class ProfileStoreTests(ProfileFixture, unittest.TestCase):
    def test_save_persists_json_and_mirrors_with_recoverable_backup(self):
        old = self.snapshot()
        untouched = self.root / "rework/historical.svg"
        untouched.parent.mkdir()
        untouched.write_text("historical icon, do not migrate")
        result = self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(result["resolvedProfiles"]["badge"]["designCanvas"], 40)
        self.assertEqual(result["resolvedProfiles"]["badge"]["shipCanvas"], 40)
        self.assertEqual(json.loads(self.store.configuration_path.read_text())["profiles"]["badge"]["strokeWidth"], 3)
        self.assertIn("`badge`", (self.root / "docs/shared/icon-profiles.md").read_text())
        self.assertFalse((self.root / "frontend/js/icon-profiles.js").exists())
        self.assertTrue(all(path == "core/icon_profiles.json" or path.startswith("docs/") for path in result["savedPaths"]))
        backup = self.root / result["backupDirectory"]
        self.assertEqual((backup / "core/icon_profiles.json").read_bytes(), old[self.store.configuration_path])
        self.assertEqual(untouched.read_text(), "historical icon, do not migrate")
        self.assertNotEqual(result["revision"], self.initial["revision"])
        self.assertEqual(result["revision"], self.store.read()["revision"])

    def test_noop_save_does_not_create_a_backup(self):
        result = self.store.save(self.configuration, self.initial["revision"])
        self.assertEqual(result["savedPaths"], [])
        self.assertIsNone(result["backupDirectory"])
        self.assertFalse((self.root / "work/profile-config-backups").exists())

    def test_invalid_configuration_and_generation_failure_do_not_write(self):
        old = self.snapshot()
        invalid = self.candidate()
        invalid["profiles"]["badge"]["canvas"] = 0
        with self.assertRaises(ValueError):
            self.store.save(invalid, self.initial["revision"])
        with patch.object(manager, "configuration_assets", side_effect=OSError("generation failed")):
            with self.assertRaisesRegex(OSError, "generation failed"):
                self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(old, self.snapshot())
        self.assertFalse((self.root / "work/profile-config-backups").exists())

    def test_stale_client_cannot_overwrite_a_new_save(self):
        result = self.store.save(self.candidate(), self.initial["revision"])
        with self.assertRaises(manager.RevisionConflict):
            self.store.save(self.configuration, self.initial["revision"])
        self.assertEqual(result["configuration"], self.store.read()["configuration"])

    def test_external_edit_during_backup_is_preserved(self):
        external = deepcopy(self.configuration)
        external["profiles"]["normal"]["label"] = "Externally edited"
        real_write = self.store.atomic_write
        changed = False

        def concurrent_write(path, content, **kwargs):
            nonlocal changed
            real_write(path, content, **kwargs)
            if not changed and "profile-config-backups" in path.parts:
                changed = True
                self.store.configuration_path.write_bytes(manager.json_bytes(external))

        with patch.object(self.store, "atomic_write", side_effect=concurrent_write):
            with self.assertRaises(manager.RevisionConflict):
                self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(json.loads(self.store.configuration_path.read_text()), external)

    def test_partial_save_failure_rolls_back_prior_files(self):
        old = self.snapshot()
        real_write = self.store.atomic_write
        failed = False

        def fail_once(path, content, **kwargs):
            nonlocal failed
            if path == self.root / "docs/shared/icon-profiles.md" and not failed:
                failed = True
                raise OSError("simulated write failure")
            return real_write(path, content, **kwargs)

        with patch.object(self.store, "atomic_write", side_effect=fail_once):
            with self.assertRaisesRegex(OSError, "simulated write failure"):
                self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(old, self.snapshot())
        self.assertTrue(list((self.root / "work/profile-config-backups").glob("*/manifest.json")))

    def test_external_edit_while_replacement_is_staged_is_not_overwritten(self):
        previous = self.store.configuration_path.read_bytes()
        external = manager.json_bytes({**self.configuration, "external-test-marker": True})
        real_fsync = manager.os.fsync

        def edit_during_fsync(descriptor):
            real_fsync(descriptor)
            self.store.configuration_path.write_bytes(external)

        with patch.object(manager.os, "fsync", side_effect=edit_during_fsync):
            with self.assertRaises(manager.RevisionConflict):
                self.store.atomic_write(self.store.configuration_path, manager.json_bytes(self.candidate()), expected=previous)
        self.assertEqual(self.store.configuration_path.read_bytes(), external)
        self.assertFalse(list(self.store.configuration_path.parent.glob(".profile-save-*")))

    def test_external_edit_after_config_commit_is_preserved_without_false_success(self):
        old = self.snapshot()
        external = deepcopy(self.configuration)
        external["profiles"]["normal"]["label"] = "External change during mirror save"
        real_write = self.store.atomic_write
        injected = False

        def edit_after_config(path, content, **kwargs):
            nonlocal injected
            real_write(path, content, **kwargs)
            if path == self.root / "docs/shared/icon-profiles.md" and not injected:
                injected = True
                self.store.configuration_path.write_bytes(manager.json_bytes(external))

        with patch.object(self.store, "atomic_write", side_effect=edit_after_config):
            with self.assertRaisesRegex(OSError, "another editor"):
                self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(json.loads(self.store.configuration_path.read_text()), external)
        for path, content in old.items():
            if path != self.store.configuration_path:
                self.assertEqual(path.read_bytes(), content)

    def test_symlinked_target_is_rejected_before_saving(self):
        original = self.store.configuration_path.read_bytes()
        mirror = self.root / "docs/shared/icon-profiles.md"
        outside = self.root / "outside.md"
        mirror.rename(outside)
        mirror.symlink_to(outside)
        before = outside.read_bytes()
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.store.save(self.candidate(), self.initial["revision"])
        self.assertEqual(self.store.configuration_path.read_bytes(), original)
        self.assertEqual(outside.read_bytes(), before)

    def test_two_store_instances_cannot_both_save_a_stale_revision(self):
        other = manager.ProfileStore(self.root)
        barrier = threading.Barrier(2)
        outcomes = []

        def save(store):
            barrier.wait()
            try:
                store.save(self.candidate(), self.initial["revision"])
                outcomes.append("saved")
            except manager.RevisionConflict:
                outcomes.append("conflict")

        workers = [threading.Thread(target=save, args=(store,)) for store in (self.store, other)]
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join(timeout=10)
            self.assertFalse(worker.is_alive())
        self.assertCountEqual(outcomes, ["saved", "conflict"])


class ProfileManagerHttpTests(ProfileFixture, unittest.TestCase):
    def setUp(self):
        super().setUp()
        (self.root / "frontend/profiles.html").write_text("<!doctype html><title>Profile manager</title>")
        (self.root / "frontend/js/profile-manager.js").write_text("// Profile manager application")
        (self.root / "frontend/css/profiles.css").write_text("body { color: black; }")
        self.token = "test-session-token"
        self.server = manager.make_server(self.store, port=0, token=self.token)
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()
        self.addCleanup(self.shutdown)

    def shutdown(self):
        self.server.shutdown()
        self.server.server_close()
        self.worker.join(timeout=5)

    def request(self, method="GET", path="/api/profiles", payload=None, headers=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
        request_headers = {"X-Profile-Token": self.token}
        request_headers.update(headers or {})
        body = None if payload is None else manager.json_bytes(payload)
        if body is not None:
            request_headers.setdefault("Content-Type", "application/json")
        connection.request(method, path, body=body, headers=request_headers)
        response = connection.getresponse()
        status, content, response_headers = response.status, response.read(), dict(response.getheaders())
        connection.close()
        return status, content, response_headers

    def test_api_reads_and_saves_then_rejects_stale_revision(self):
        status, content, _ = self.request()
        self.assertEqual(status, 200)
        current = json.loads(content)
        payload = {"configuration": self.candidate(), "revision": current["revision"]}
        status, content, _ = self.request("PUT", payload=payload)
        self.assertEqual(status, 200, content)
        self.assertIn("badge", json.loads(content)["resolvedProfiles"])
        status, _, _ = self.request("PUT", payload=payload)
        self.assertEqual(status, 409)

    def test_api_token_origin_host_and_content_type_are_required(self):
        payload = {"configuration": self.candidate(), "revision": self.initial["revision"]}
        for headers in ({"X-Profile-Token": ""}, {"Origin": "https://example.invalid"}, {"Host": "example.invalid"}):
            with self.subTest(headers=headers):
                self.assertEqual(self.request("PUT", payload=payload, headers=headers)[0], 403)
        self.assertEqual(self.request("PUT", payload=payload, headers={"Content-Type": "text/plain"})[0], 415)
        self.assertEqual(self.store.read()["revision"], self.initial["revision"])

    def test_static_routes_do_not_expose_arbitrary_repository_files(self):
        for path in ("/", "/js/profile-manager.js", "/css/profiles.css"):
            self.assertEqual(self.request(path=path)[0], 200)
        for path in ("/editor", "/editor/", "/index.html", "/js/icon-profiles.js", "/js/app.js", "/core/icon_profiles.json", "/.git/config", "/js/../../core/icon_profiles.json", "/js/%2e%2e/%2e%2e/core/icon_profiles.json"):
            self.assertEqual(self.request(path=path)[0], 404, path)

    def test_profile_api_reads_current_json_without_stale_documentation(self):
        path = self.root / "docs/shared/icon-profiles.md"
        old_mirror = path.read_bytes()
        self.store.configuration_path.write_bytes(manager.json_bytes(self.candidate()))
        status, content, headers = self.request()
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(content)["resolvedProfiles"]["badge"]["canvas"], 40)
        self.assertEqual(path.read_bytes(), old_mirror)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["Referrer-Policy"], "no-referrer")


if __name__ == "__main__":
    unittest.main()
