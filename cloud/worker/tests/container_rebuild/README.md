# Isolated container rebuild regression

These fixtures use invented circle/arrow artwork, a selected older upload, and an
unselected control. They contain no production records or credentials.

1. Build `cloud/worker/app` with `worker-build --release`.
2. Create a temporary Wrangler config pointing at that build, a new local D1,
   local R2, and `ADMIN_USERS = '{"tester":"preview-only"}'`. Do not copy production
   service bindings, secrets, account IDs, or remote bindings.
3. Apply migrations with `wrangler d1 migrations apply ... --local` into a fresh
   temporary persistence directory. Migration 0024 is required.
4. Run `python3 cloud/worker/tests/container_rebuild/seed.py /tmp/container-fixture`.
   Import its `seed.sql` into that empty local D1 using `wrangler d1 execute ...
   --local --file /tmp/container-fixture/seed.sql` with the same persistence path.
5. Run the Worker locally on `127.0.0.1:8891`, then run
   `python3 cloud/worker/tests/container_rebuild/check_local.py`.

The HTTP check uses the real composition engine and Worker. It verifies that a
build supersedes an older selected upload, preserves its candidate, serves the
new hash, rejects a stale save, and supports repeated saves. It also checks a
pair with no artwork selection. Use a fresh fixture for each run. `demo-arrow`
is reserved for browser verification and is not changed by the HTTP check.

`cargo test -p pictographic-core --test combination_build` additionally tests
selection/part races and all-or-nothing rollback using the SQL used by the Worker.
No test contacts production. The HTTP check refuses non-loopback base URLs.
