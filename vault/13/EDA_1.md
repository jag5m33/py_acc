---

## project: dataset: source: stage: EDA step: 1 status: in-progress date: {{date}} notebook: tags: [eda, eda/01] next: "[[EDA 02 - Missing Values]]"

# EDA 01 — First Look

> [!abstract] Goal of this step Understand **what the data is** before touching it. Observe and record only — no cleaning, no dropping. Every decision gets logged at the bottom and actioned in a later step.

---

## 1. Context

|Item|Answer|
|---|---|
|Source / link||
|What does **one row** represent?||
|Time span covered||
|Target variable||
|Problem type|regression / classification / ordinal|
|What is known **at prediction time**?||

---

## 2. Loading

|Item|Value|
|---|---|
|File format||
|File size on disk||
|Load method|pandas / DuckDB|
|Full dataset or sample?||
|Sample size & method||
|Random seed||
|Why the sample is representative||

```python
# load code
```

> [!tip] If sampling Check the sample against the full data on 2–3 key columns (target distribution, a date range, a major category). Record the comparison here.

---

## 3. Shape & structure

|Metric|Value|
|---|---|
|Rows||
|Columns||
|Memory usage||
|Duplicate rows||

```python
# shape, info, memory, duplicates
```

---

## 4. Column inventory

Type key: `num` numeric · `cat` categorical · `ord` ordinal · `dt` datetime · `bool` · `id` · `text`

|Column|Loaded dtype|Should be|Type|% missing|n unique|Example value|Notes|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||

---

## 5. First impressions

Observations from `head()`, `tail()` and a random sample:

---

## 6. Target — first look

|Item|Value|
|---|---|
|dtype||
|Distribution / class counts||
|Imbalance?||
|Missing in target||

```python
# target value_counts / describe
```

![[target-distribution.png]]

---

## 7. Quick flags

- [ ] Wrong dtypes (dates as strings, numbers as objects)
- [ ] Constant or near-constant columns
- [ ] ID / free-text columns with no predictive use
- [ ] Highly redundant columns (same info twice)
- [ ] **Leakage suspects** — not available at prediction time
- [ ] Impossible values spotted (negative ages, future dates)
- [ ] Mixed units or inconsistent category labels

## Details:

---

## 8. Questions to carry forward

- [ ]
- [ ]

---

## 9. Decision log

> [!warning] Record, don't action Decisions are proposed here and carried out in the cleaning notes.

| Column(s) | Proposed decision | Reason | Actioned in |
| --------- | ----------------- | ------ | ----------- |
|           |                   |        |             |
|           |                   |        |             |

---

## Links

Next → [[EDA 02 - Missing Values]] Related → [[Project Overview]] · [[Decision Log]]