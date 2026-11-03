# Large table embeds

Embeds of a table too large to read whole: `../table/large/big-50000.table`, a single file of 50,000 deals. An app reads it through its index, and draws its first rows while the rest is still being read. [`Large Table Embeds.cases.json`](Large%20Table%20Embeds.cases.json) says what each should show, for tests.

## The first few

The first five deals, with `rows=5&rest=more`. Beneath: "Show 49,995 more rows". Pressed, all 50,000 scroll inside the frame.

[Deals, the first five](../table/large/big-50000.table#table=deals&rows=5&rest=more&embed=1 "Five of 50,000")

## The whole table

With no count, the table scrolls inside a frame of the usual height, through all 50,000 rows.

[Every deal](../table/large/big-50000.table#table=deals&embed=1 "All 50,000")

## After the last embed

The document ends with ordinary text.
