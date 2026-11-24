---
title: Markdown feature test
author: markdownwise
---

# Markdown feature test

This file checks how a Markdown tool handles the features people actually use. Each section names
what should happen, so a result can be checked by eye.

## 1. Text styles

Plain text, **bold**, *italic*, ***bold italic***, ~~strikethrough~~, `inline code` and a
[link to example.com](https://example.com). A bare address should also become a link:
https://example.com/page. Smart quotes: "double" and 'single', an apostrophe in don't, and a dash --
like this.

## 2. Headings

### Third level

#### Fourth level

## 3. Lists

- First item
- Second item with a nested list:
  - Nested item one
  - Nested item two
- Third item

1. Step one
2. Step two
   1. Sub-step a
   2. Sub-step b
3. Step three

## 4. Task list

- [x] Done task (should show a ticked box)
- [ ] Open task (should show an empty box)

## 5. Table with alignment

| Planet  | Moons | Distance (AU) | Notes             |
|:--------|------:|:-------------:|-------------------|
| Mercury |     0 |     0.39      | closest to the Sun|
| Earth   |     1 |     1.00      | home              |
| Jupiter |    95 |     5.20      | largest planet    |
| Neptune |    16 |    30.07      | farthest planet   |

Left column left-aligned, Moons right-aligned, Distance centred.

## 6. Code

```python
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"  # should be colour-highlighted
```

```
A plain code block keeps    its spacing.
```

A very long line inside code should wrap or scroll, not run off the page:

```bash
curl -s https://example.com/an/extremely/long/path/that/keeps/going/and/going/until/it/is/far/wider/than/any/page/could/ever/be/printed
```

## 7. Quote

> A blockquote should be indented or marked with a bar.
>
> It can have more than one paragraph.

## 8. Footnote

This sentence has a footnote.[^1] The note should appear at the end, with a link back.

[^1]: This is the footnote text.

## 9. Maths

Inline maths: $E = mc^2$. A display equation:

$$
\int_0^1 x^2 \, dx = \frac{1}{3}
$$

## 10. Definition list

Term
: The definition of the term.

## 11. Horizontal rule

Text above the line.

---

Text below the line.

## 12. Characters

Accents: café, naïve, Zürich. Greek: α β γ. Symbols: © ® ™ € £ ¥ → ≤ ≥. Japanese: 日本語.

## 13. Raw HTML

<b>This HTML tag</b> should either render as bold or be shown as text, never run as code.
<script>alert("this must never run")</script>

## 14. A long table that crosses a page

| # | Item | Value |
|---|------|-------|
| 1 | alpha | 101 |
| 2 | beta | 102 |
| 3 | gamma | 103 |
| 4 | delta | 104 |
| 5 | epsilon | 105 |
| 6 | zeta | 106 |
| 7 | eta | 107 |
| 8 | theta | 108 |
| 9 | iota | 109 |
| 10 | kappa | 110 |
| 11 | lambda | 111 |
| 12 | mu | 112 |
| 13 | nu | 113 |
| 14 | xi | 114 |
| 15 | omicron | 115 |
| 16 | pi | 116 |
| 17 | rho | 117 |
| 18 | sigma | 118 |
| 19 | tau | 119 |
| 20 | upsilon | 120 |
| 21 | phi | 121 |
| 22 | chi | 122 |
| 23 | psi | 123 |
| 24 | omega | 124 |

If this table crosses a page in a PDF, its header row should repeat on the next page.
