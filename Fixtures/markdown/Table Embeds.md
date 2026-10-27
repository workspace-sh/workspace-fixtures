# Table embeds

A paragraph that is one link, with `embed` in its address, is an embed: Workspace draws the link's target in place, and every other Markdown tool shows the link. The tables are the examples in `../table/`, reached by relative path. Each case says what should appear.

## A table view

The tasks of the projects example, in its first view. A table with five columns and eight rows, sorted by priority. It can be edited here: a cell changed is saved to the `.table` file.

[Tasks by priority](../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&embed=1 "All tasks by priority")

This paragraph comes after the table, not under it.

## A board

The same table in its board view: a column for each status.

[Task board](../table/projects.table#table=tasks&view=Board%20by%20status&embed=1 "Tasks by status")

## A view by its id

The board again, its view named by id rather than by name: `view=` takes either. A link an app writes uses the id, which survives the view being renamed. The same board as above should appear.

[Task board, by id](../table/projects.table#table=tasks&view=mufe9nmjruiq5&embed=1 "Tasks by status")

## Another table in the same file

The projects table of the same `.table` file, in its first view. Seventeen rows, so it scrolls inside its frame.

[Projects](../table/projects.table#table=projects&view=All%20projects&embed=1 "All projects")

## A table from another file, with no view and no caption

With no `view`, the table's first view is drawn: for deals, its Pipeline board. With no title, there is no caption.

[Deals](../table/crm.table#table=deals&embed=1)

## Two in a row

[Companies](../table/crm.table#table=companies&embed=1 "Companies")

[Contacts](../table/crm.table#table=contacts&embed=1 "Contacts")

## How much is shown

The link can say how much of a view to show at once. The rest scrolls inside it.

Five rows of the projects table, with `rows=5`:

[Projects, five at a time](../table/projects.table#table=projects&view=All%20projects&rows=5&embed=1 "Five rows, then it scrolls")

Twelve rows of it, with `rows=12`: taller than an embed is when the link says nothing.

[Projects, twelve at a time](../table/projects.table#table=projects&view=All%20projects&rows=12&embed=1 "Twelve rows")

More rows than the table has, with `rows=20`: all eight tasks, and no scrolling.

[Every task](../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&rows=20&embed=1 "All eight")

A board with one card down each column, with `cards=1`:

[Tasks, one card deep](../table/projects.table#table=tasks&view=Board%20by%20status&cards=1&embed=1 "One card down each column")

A list of three rows, with `rows=3`:

[Quick list](../table/projects.table#table=projects&view=Quick%20list&rows=3&embed=1 "Three rows of a list")

A gallery of one line, with `cards=1`:

[Gallery](../table/projects.table#table=projects&view=Gallery&cards=1&embed=1 "The first line of a gallery")

A count the layout doesn't show is ignored. `cards=2` on a table leaves it the usual height:

[Projects](../table/projects.table#table=projects&view=All%20projects&cards=2&embed=1 "cards= on a table: ignored")

## Only the first few

With `rest=more` beside the count, only those rows or cards are drawn and nothing scrolls. A line beneath says how many more there are, and shows them when pressed.

The first three tasks, with `rows=3&rest=more`. Beneath: "Show 5 more rows".

[Top tasks](../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&rows=3&rest=more&embed=1 "The three most urgent")

A board one card deep, with `cards=1&rest=more`. Each column still says how many cards it has, and how many more.

[Next up](../table/projects.table#table=tasks&view=Board%20by%20status&cards=1&rest=more&embed=1 "The first card of each column")

A list of four projects, with `rows=4&rest=more`:

[Projects](../table/projects.table#table=projects&view=Quick%20list&rows=4&rest=more&embed=1 "Four of seventeen")

The deals, two rows of eight, with `rows=2&rest=more`. The totals beneath are of all eight.

[Deals](../table/crm.table#table=deals&view=All%20deals&rows=2&rest=more&embed=1 "Two deals, and the totals of all")

A count the table doesn't reach, with `rows=20&rest=more`: all eight tasks, and no line beneath.

[Every task](../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&rows=20&rest=more&embed=1)

## Not embeds

These stay links.

A link in a sentence: see [the tasks](../table/projects.table#table=tasks&embed=1) for more.

- A link alone in a list item: [the tasks](../table/projects.table#table=tasks&embed=1)

> A link alone in a quote:
>
> [the tasks](../table/projects.table#table=tasks&embed=1)

Switched off with `embed=0`:

[Tasks, as a link](../table/projects.table#table=tasks&embed=0)

Without the key:

[Tasks, as a link](../table/projects.table#table=tasks)

## What can't be drawn

Each of these should say why in place, and leave the rest of the document as it is.

A file that isn't there:

[Missing file](../table/nowhere.table#embed=1 "This file does not exist")

A table the file doesn't have:

[Missing table](../table/projects.table#table=nope&embed=1 "No such table")

A view the table doesn't have:

[Missing view](../table/projects.table#table=tasks&view=nope&embed=1 "No such view")

A file outside the folder that was opened:

[Outside](../../../outside.table#embed=1 "Outside the workspace")

## After the last embed

The document ends with ordinary text.
