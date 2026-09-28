-- Pictographic D1 schema.
--
-- Workflow tables keep the exact columns of the local feedback.sqlite3 so rows copy across
-- unchanged and the Worker's SQL can follow deploy.py statement for statement.
-- Catalog tables are new: local builds push the effective catalog (artwork choices applied)
-- because that overlay needs Python rendering. Authored SVGs are small and stay inline here;
-- R2 holds references and other large files.

-- ---------------------------------------------------------------- workflow (from deploy.py)

CREATE TABLE admin_sessions (
    token TEXT PRIMARY KEY, username TEXT NOT NULL, expires REAL NOT NULL);

CREATE TABLE reviews (
    icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('ready', 'pending', 're-generated', 'approve', 'rejected', 'claimed')),
    updated_at TEXT NOT NULL, updated_by TEXT, worker TEXT, claimed_at TEXT, note TEXT NOT NULL DEFAULT '',
    PRIMARY KEY(icon, svg_sha256));
CREATE INDEX reviews_status ON reviews(status);

CREATE TABLE feedback (
    id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
    svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL,
    reference_images TEXT NOT NULL DEFAULT '[]', author TEXT, edited_by TEXT, edited_at TEXT,
    reason TEXT NOT NULL DEFAULT 'other');
CREATE INDEX feedback_icon ON feedback(icon, id);

CREATE TABLE activity_log (
    id INTEGER PRIMARY KEY, username TEXT NOT NULL, action TEXT NOT NULL, icon TEXT,
    details TEXT NOT NULL DEFAULT '{}', created_at TEXT NOT NULL);
CREATE INDEX activity_log_user ON activity_log(username, id);
CREATE INDEX activity_log_icon ON activity_log(icon, id);

CREATE TABLE work_results (
    icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
    stage TEXT NOT NULL CHECK(stage IN ('before','after')),
    worker TEXT NOT NULL, svg TEXT NOT NULL, python_path TEXT, python_source TEXT,
    validation TEXT, note TEXT NOT NULL DEFAULT '', saved_at TEXT NOT NULL,
    PRIMARY KEY(icon, svg_sha256, stage));

CREATE TABLE icon_types (
    icon TEXT PRIMARY KEY, icon_type TEXT NOT NULL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL);

CREATE TABLE icon_flags (
    icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN
    ('container_combination','combination','text','number','other','exception')),
    updated_at TEXT NOT NULL, updated_by TEXT);

CREATE TABLE split_requests (
    id INTEGER PRIMARY KEY, icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
    combination_type TEXT NOT NULL, reason TEXT NOT NULL, reference_path TEXT NOT NULL,
    active INTEGER NOT NULL DEFAULT 1, created_at TEXT NOT NULL, created_by TEXT, restored_by TEXT, restored_at TEXT,
    UNIQUE(icon, svg_sha256));

CREATE TABLE pending_briefs (
    id INTEGER PRIMARY KEY, split_id INTEGER NOT NULL REFERENCES split_requests(id),
    position INTEGER NOT NULL, name TEXT NOT NULL, family TEXT NOT NULL,
    description TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'pending',
    generated_icon TEXT, completed_by TEXT, completed_at TEXT, UNIQUE(split_id, position));

CREATE TABLE upload_families (
    id TEXT PRIMARY KEY, name TEXT NOT NULL, canvas_size INTEGER NOT NULL,
    created_at TEXT NOT NULL, created_by TEXT NOT NULL);

CREATE TABLE uploaded_icons (
    icon TEXT PRIMARY KEY, record TEXT NOT NULL, svg TEXT NOT NULL);

CREATE TABLE primitive_status (
    uuid TEXT PRIMARY KEY, status TEXT NOT NULL CHECK(status IN ('skip')),
    reason TEXT NOT NULL CHECK(reason IN ('combination','container','text_number','other')),
    note TEXT NOT NULL DEFAULT '', updated_by TEXT NOT NULL, updated_at TEXT NOT NULL,
    combination_brief TEXT, main_brief TEXT, sub_brief TEXT, sub_position TEXT);

CREATE TABLE primitive_briefs (
    uuid TEXT PRIMARY KEY, family TEXT NOT NULL, brief TEXT NOT NULL,
    updated_by TEXT NOT NULL, updated_at TEXT NOT NULL);

CREATE TABLE primitive_symbol_links (
    uuid TEXT PRIMARY KEY, icon_key TEXT NOT NULL,
    updated_by TEXT NOT NULL, updated_at TEXT NOT NULL);

CREATE TABLE progression_imports (uuid TEXT PRIMARY KEY, updated_at TEXT NOT NULL);
CREATE TABLE progression_reviews (path TEXT PRIMARY KEY, content TEXT NOT NULL);
CREATE TABLE review_data_migrations (id TEXT PRIMARY KEY, applied_at TEXT NOT NULL, details TEXT NOT NULL);

-- ---------------------------------------------------------------- catalog (pushed by local builds)

-- One row per catalog icon (built, failed and uploaded), holding the fields routes check.
-- `record` is the full gallery record as JSON; `svg_sha256` is the effective current revision.
CREATE TABLE icons (
    key TEXT PRIMARY KEY,
    icon_id TEXT, name TEXT, family TEXT, category TEXT, profile TEXT, canvas_size INTEGER,
    svg_sha256 TEXT NOT NULL DEFAULT '',
    python_source TEXT, preview_url TEXT, original_sources TEXT NOT NULL DEFAULT '[]',
    variant_of TEXT, variant_root TEXT, variant_label TEXT,
    build_failed INTEGER NOT NULL DEFAULT 0,
    uploaded INTEGER NOT NULL DEFAULT 0,
    record TEXT NOT NULL DEFAULT '{}',
    pushed_at TEXT NOT NULL);
CREATE INDEX icons_family ON icons(family);

-- Every drawing ever pushed, by content hash. Never updated after insert.
CREATE TABLE revisions (
    svg_sha256 TEXT PRIMARY KEY, icon TEXT NOT NULL, svg TEXT NOT NULL,
    origin TEXT NOT NULL DEFAULT 'build',
    created_at TEXT NOT NULL);
CREATE INDEX revisions_icon ON revisions(icon);

-- Build metadata: which catalog push is current (release, commit, counts).
CREATE TABLE catalog_pushes (
    id INTEGER PRIMARY KEY, pushed_at TEXT NOT NULL, pushed_by TEXT NOT NULL, details TEXT NOT NULL DEFAULT '{}');

-- ---------------------------------------------------------------- stores (were folders beside the database)

-- Opaque JSON documents written by local Python (artwork choices, stroke edits):
-- the cloud stores them; only local code interprets them.
CREATE TABLE store_documents (
    store TEXT NOT NULL CHECK(store IN ('icon-artwork', 'stroke-edits')),
    key TEXT NOT NULL, document TEXT NOT NULL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL,
    PRIMARY KEY(store, key));

CREATE TABLE reference_images (
    id TEXT PRIMARY KEY, name TEXT NOT NULL, mime TEXT NOT NULL, size INTEGER NOT NULL,
    r2_key TEXT NOT NULL, uploaded_by TEXT NOT NULL, uploaded_at TEXT NOT NULL);

-- ---------------------------------------------------------------- meaning layer (seeded now, curated later)

CREATE TABLE concepts (
    concept_id TEXT PRIMARY KEY, slug TEXT NOT NULL UNIQUE, name TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '', status TEXT NOT NULL DEFAULT 'active'
        CHECK(status IN ('active', 'merged', 'retired')),
    source TEXT NOT NULL DEFAULT '');
CREATE TABLE concept_aliases (
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id), alias TEXT NOT NULL, lang TEXT NOT NULL DEFAULT 'en',
    PRIMARY KEY(concept_id, alias, lang));
CREATE TABLE categories (
    category_id TEXT PRIMARY KEY, parent_id TEXT REFERENCES categories(category_id),
    slug TEXT NOT NULL, name TEXT NOT NULL);
CREATE TABLE concept_categories (
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    category_id TEXT NOT NULL REFERENCES categories(category_id),
    is_primary INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(concept_id, category_id));
CREATE TABLE physicals (
    physical_id TEXT PRIMARY KEY, slug TEXT NOT NULL UNIQUE, name TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '', kind TEXT NOT NULL CHECK(kind IN ('single', 'composite')),
    status TEXT NOT NULL DEFAULT 'candidate' CHECK(status IN ('candidate', 'active', 'merged', 'retired')));
CREATE TABLE concept_physicals (
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    physical_id TEXT NOT NULL REFERENCES physicals(physical_id),
    rank INTEGER NOT NULL DEFAULT 1, PRIMARY KEY(concept_id, physical_id));
CREATE TABLE physical_parts (
    composite_id TEXT NOT NULL REFERENCES physicals(physical_id),
    part_id TEXT NOT NULL REFERENCES physicals(physical_id),
    role TEXT NOT NULL CHECK(role IN ('main', 'sub', 'container', 'symbol')),
    position TEXT CHECK(position IN ('tl', 'tr', 'bl', 'br', 'center')),
    PRIMARY KEY(composite_id, role));
CREATE TABLE "references" (
    reference_id TEXT PRIMARY KEY, kind TEXT NOT NULL CHECK(kind IN ('single', 'combination')),
    concept TEXT, old_concept TEXT, categories TEXT, folder TEXT, file TEXT,
    r2_key TEXT, source TEXT NOT NULL, license TEXT,
    concept_id TEXT REFERENCES concepts(concept_id), physical_id TEXT REFERENCES physicals(physical_id));
CREATE TABLE reference_parts (
    reference_id TEXT NOT NULL REFERENCES "references"(reference_id),
    role TEXT NOT NULL CHECK(role IN ('main', 'sub', 'container', 'symbol')),
    part_reference_id TEXT NOT NULL, position TEXT,
    PRIMARY KEY(reference_id, role));
CREATE TABLE icon_references (
    icon TEXT NOT NULL, reference_id TEXT NOT NULL, PRIMARY KEY(icon, reference_id));
