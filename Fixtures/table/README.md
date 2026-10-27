# table

The `.table` fixtures: the example tables every app and test opens, and large tables made by table-file-format's generator. This is the only copy. [workspace-sh/table-file-format](https://github.com/workspace-sh/table-file-format) mounts this repository as a submodule (`workspace-fixtures/`), and its `fixtures/` is a link to this folder. [`CHECKSUMS`](CHECKSUMS) names the commit the single files were written from.

## The example files

`crm.table`, `formula-errors.table`, `household-budget.table`, `library.table`, `projects.table` and `shop.table` are what table-file-format's tests read and what the web, Mac, iOS, Android and Linux demo apps open at launch. They're edited here, in a table-file-format checkout's `workspace-fixtures/` submodule, and committed to this repository first. table-file-format then moves its submodule to that commit.

| File | Tables | What it exercises |
|---|---|---|
| `crm.table` | companies, contacts, deals | links between tables, logos as attachments, a board, a gallery, a calendar, totals |
| `formula-errors.table` | errors | every error a formula can give, a row each, shown in plain words with its mark (table-file-format D61) |
| `household-budget.table` | budget, ledger | a sheet view (lettered columns, numbered rows), formulas, currency, totals |
| `library.table` | books | a long table (1,000 rows, nine fields) to scroll past a screen or two: a long table's layout and its header while scrolling; views All books, By genre (a board), To read (filtered), Recently added |
| `projects.table` | projects, tasks | row pages (`bodies/`), a choice list, grouping, every layout |
| `shop.table` | orders, customers, products, lines | four linked tables, formulas across tables, grouping, totals |

**After editing an example**, write its single file and `CHECKSUMS` again from a table-file-format checkout:

```sh
npm run fixtures:export -- workspace-fixtures/Fixtures/table           # in place: single-file/ and CHECKSUMS
npm run fixtures:export -- workspace-fixtures/Fixtures/table --check   # names each file that differs
```

In place, it leaves the folders as they are and writes only `single-file/` and `CHECKSUMS`; it touches nothing else here (`large/`, this README). The same command writes the examples into any other folder a test needs.

### As single files (`single-file/`)

A `.table` is a folder or a single file, the same document either way (table-file-format SPEC section 13, D49, D50). Each example is here in both forms: the folder above, and in `single-file/` a single file of the same name (a folder and a file can't share a name in one folder). Each single file holds one `<name>.table/` root that unzips to its folder, byte for byte, attachments included (the CRM's logos). There is no `.table.zip`: a `.table.zip` from before is a single-file `.table` with `.zip` added, and renaming it is all it needs.

Both forms are written together by `fixtures:export`, above. The same folder always gives the same bytes, and each single file is read back as its folder before it's written. Their SHA-256 sums are in [`CHECKSUMS`](CHECKSUMS).

## Large tables (`large/`)

One `deals` table of N rows, about 185 bytes a row: a title, a stage from six choices, an amount, a probability, an owner, a close date, a short note, and one formula column (weighted = amount × probability). The data is seeded, so it is the same on every run. Every id is z-base-32 as an app mints it (26 characters a row, 13 a field; table-file-format D23, D62), and each table is written by table-core's own writer, as an app saves one.

| File | Rows | Rows files | Single file |
|---|---|---|---|
| `big-10000.table` | 10,000 | 1.8 MB | 0.4 MB |
| `big-50000.table` | 50,000 | 9.2 MB | 1.9 MB |
| `big-1000000.table` | 1,000,000 | 186 MB in 8 files | 38.6 MB |

Each is a single-file `.table` (SPEC section 13): what the apps open from Files or a file picker, as it is. To work with the folder, unzip it; each holds one `big-<rows>.table/` bundle. Each is formatVersion 3: its rows are in `tables/deals/rows/`, a new file each 25 MB (D51), so the million-row table's are `0001.ndjson` to `0008.ndjson`. The measurements in table-file-format's LARGE-TABLES.md were made on the same data with short counter ids (`d0`, `d1`, …): ids of 130 random bits don't compress, which is why the single files are about twice the size they were.

They are kept as single files because the folders are large and the single files are not: the million-row table's folder is 186 MB, its single file under 40 MB. A table whose single file passes 50 MB is not added here; it is made where it is needed (below).

They are made in a checkout of table-file-format:

```sh
node --conditions=source --import tsx scripts/big-table.mts 10000 <out-dir>
node --conditions=source --import tsx scripts/big-table.mts 50000 <out-dir>
node --max-old-space-size=4096 --conditions=source --import tsx scripts/big-table.mts 1000000 <out-dir>
```

Each writes `<out-dir>/big-<rows>.table/` and `<out-dir>/single-file/big-<rows>.table`. Other sizes are made the same way. If the generator changes, make these again and update the checksums.

SHA-256, to tell whether a copy is the one that was measured:

| File | SHA-256 |
|---|---|
| `big-10000.table` | `7043fe769e0aaf56c7b6835f04bd9cc4c538fc8e71a602e8fdb1f3916e8269fd` |
| `big-50000.table` | `acafbb11d5e14c621ad3ad5f3c5a57b68daf5b270e12b7dfc5eea5443f7a5c8e` |
| `big-1000000.table` | `d51b9a47e8e8fa49a1b90d8a92738a5b5288fb1a055cabb1b7cccf51ada70d66` |
| `big-10000.table`'s rows files inside it, joined in name order | `49680d45d50bc40e741b63c218e287930ba5bbbb5c8613ecb17a2256a7ea7397` |
| `big-50000.table`'s rows files inside it, joined in name order | `15072bc9d7bdd2fe4bf6e667f249611e908298b50466cdde21d62cbf2463d223` |
| `big-1000000.table`'s rows files inside it, joined in name order | `fbf24e25e75967c1d892fe7ea58c0dea58f45c1bbcb2bedbdb8beecc1c01434d` |

How to measure with them is in table-file-format's `docs/BENCHMARKING.md`.
