# Every element

Generated from the same table the element sweep measures, so the two
cannot drift apart.

## paragraph

Just a paragraph.

## heading h1

# One

## heading h3

### Three

## heading h6

###### Six

## heading h2

## Two

## heading h4

#### Four

## heading h5

##### Five

## setext heading

_normalises to ATX._

Title
=====

## setext h2

_normalises to ATX._

Title
-----

## heading closed

_closing hashes dropped._

## Two ##

## frontmatter

_not editable in the surface; preserved on splice._

---
title: T
---

Body.

## escaped markers

a \*not italic\* b

## numeric entity

_resolves to the character._

a &#35; b

## nested emphasis

*a **b** c*

## code span backtick

a `` ` `` b

## entity

_entities resolve to characters._

AT&amp;T and 5 &lt; 6

## unicode

café naïve 😀 中文

## soft break

_joins to one line._

first line
second line

## bold

a **b** c

## italic

a *b* c

## bold italic

a ***b*** c

## bold italic alt

_normalises to ***._

a **_b_** c

## strikethrough

a ~~b~~ c

## inline code

a `b` c

## link

a [t](https://e.com) c

## autolink

_becomes [url](url)._

see <https://e.com> now

## mark

a <mark>b</mark> c

## kbd

a <kbd>b</kbd> c

## sub

a <sub>b</sub> c

## sup

a <sup>b</sup> c

## underline

a <u>b</u> c

## hard break

_backslash form._

a\
b

## html break

_becomes a backslash break._

a<br>b

## two-space break

_normalises to the backslash form._

a  
b

## email autolink

write <a@b.com> now

## bare autolink

_GFM extended autolink._

see www.example.com now

## angle destination

_space percent-encoded._

[t](<https://e.com/a b>)

## collapsed reference

_normalises to inline._

[collapsed][]

[collapsed]: https://e.com

## shortcut reference

_normalises to inline._

[shortcut]

[shortcut]: https://e.com

## single tilde strike

_normalises to ~~._

a ~b~ c

## link with title

_title dropped._

[t](https://e.com "T")

## reference link

_normalises to inline._

[t][reflink]

[reflink]: https://e.com

## link in emphasis

_emphasis moves inside the link._

**[t](https://e.com)**

## quote

> quoted

## quote + list

> intro
>
> - one
> - two

## quote + heading

> # Head

## quote + code

> ```js
> let x;
> ```

## nested quote

> outer
>
> > inner

## nested quote x3

> > > x

## bullet list

- one
- two

## bullet star

_normalises to -._

* one
* two

## bullet plus

_normalises to -._

+ one
+ two

## ordered paren

_normalises to .._

1) one
2) two

## ordered list

1. one
2. two

## ordered from N

3. three
4. four

## task list unchecked

- [ ] todo

## task list checked

- [x] done

## nested list

- one
  - deep

## loose list

- one

  cont

- two

## item with code

- one

  ```js
  let x;
  ```

## item with two paras

- one

  two

- three

## list in quote in list

- a

  > q

## fenced code

```js
let x;
```

## bare fence

```
plain
```

## tilde fence

_normalises to backticks._

~~~js
let x;
~~~

## indented code

_re-emits fenced._

    indented

## thematic break

a

---

b

## table

| A | B |
| --- | --- |
| 1 | 2 |

## table aligned

| A |
| :-: |
| 1 |

## table with inline

| A |
| --- |
| **b** `c` |

## table in quote

> | A |
> | --- |
> | 1 |

## table escaped pipe

| A |
| --- |
| a \| b |

## table ragged row

_short rows padded._

| A | B |
| --- | --- |
| 1 |

## alert NOTE

> [!NOTE]
> body

## alert TIP

> [!TIP]
> body

## alert IMPORTANT

> [!IMPORTANT]
> body

## alert WARNING

> [!WARNING]
> body

## alert CAUTION

> [!CAUTION]
> body

## details

<details>
<summary>S</summary>

B

</details>

## image remote

_unreachable on purpose — shows the broken-image chip._

![alt](https://e.com/i.png)

## image local

![a](pics/sample.png)

## image escaping path

_source round-trips; refused at load — outside the folder._

![a](../outside.png)

## image empty alt

![](pics/sample.png)

## image linked

[![a](pics/sample.png)](https://e.com)

## image reference

_normalises to inline._

![a][refimg]

[refimg]: pics/sample.png

## image with title

![a](pics/sample.png "T")

## image in table

| A |
| --- |
| ![a](pics/sample.png) |

## image in list

- ![a](pics/sample.png)

## two images one para

![a](pics/sample.png) and ![b](pics/wide.png)

## footnote ref

text[^a]

[^a]: note

## raw html block

_renders as HTML, read-only (#345)._

<div class="x">hi</div>

## html comment

<!-- a note -->

## html comment + text

<!-- a note -->

After.

## text + html comment

Before.

<!-- a note -->

## html div alone

_renders as HTML, read-only (#345)._

<div>x</div>

## html img

_renders as HTML, read-only (#345)._

<img src="pics/sample.png" alt="a">

## html img floated

_renders as HTML, read-only (#345)._

<img align="right" src="pics/sample.png" height="40px" alt="a">

Text beside it.

## html img sized

_renders as HTML, read-only (#345)._

<img src="pics/wide.png" width="50%" alt="w">

## html p centred

_renders as HTML, read-only (#345)._

<p align="center">
  <img src="pics/sample.png" alt="a">
  <br>
  <b>Bold</b> text
</p>

## html div around md

<div align="center">

# Title

Some **text**.

</div>

## html img in text

Built with <img src="pics/sample.png" alt="a"> care.

## disallowed raw html

_GFM filters it; we pass it through as source._

a <title>t</title> b

## inline html unknown

a <abbr>b</abbr> c

## math dollars

_passes through as text; no math rendering._

an $x$ formula
