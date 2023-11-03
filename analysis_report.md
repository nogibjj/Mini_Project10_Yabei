
## Data Loading

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       |
```

## Data Description

**Result Preview:**

```markdown
|    | summary   | Car                     |       MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |     Model | Origin   |
|---:|:----------|:------------------------|----------:|------------:|---------------:|-------------:|---------:|---------------:|----------:|:---------|
|  0 | count     | 406                     | 406       |   406       |        406     |     406      |  406     |      406       | 406       | 406      |
|  1 | mean      |                         |  23.0512  |     5.47537 |        194.78  |     103.53   | 2979.41  |       15.5197  |  75.9212  |          |
|  2 | stddev    |                         |   8.40178 |     1.71216 |        104.922 |      40.5207 |  847.004 |        2.80336 |   3.74874 |          |
|  3 | min       | AMC Ambassador Brougham |   0       |     3       |         68     |       0      | 1613     |        8       |  70       | Europe   |
|  4 | max       | Volvo Diesel            |  46.6     |     8       |        455     |     230      | 5140     |       24.8     |  82       | US       |
```

## Data Loading

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       |
```

## Data Transformation

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   | RegionCategory   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|:-----------------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       | Domestic         |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       | Domestic         |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       | Domestic         |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       | Domestic         |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       | Domestic         |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       | Domestic         |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       | Domestic         |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       | Domestic         |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       | Domestic         |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       | Domestic         |
```

## Data Loading

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       |
```

## Data Loading

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       |
```

## Data Description

**Result Preview:**

```markdown
|    | summary   | Car                     |       MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |     Model | Origin   |
|---:|:----------|:------------------------|----------:|------------:|---------------:|-------------:|---------:|---------------:|----------:|:---------|
|  0 | count     | 406                     | 406       |   406       |        406     |     406      |  406     |      406       | 406       | 406      |
|  1 | mean      |                         |  23.0512  |     5.47537 |        194.78  |     103.53   | 2979.41  |       15.5197  |  75.9212  |          |
|  2 | stddev    |                         |   8.40178 |     1.71216 |        104.922 |      40.5207 |  847.004 |        2.80336 |   3.74874 |          |
|  3 | min       | AMC Ambassador Brougham |   0       |     3       |         68     |       0      | 1613     |        8       |  70       | Europe   |
|  4 | max       | Volvo Diesel            |  46.6     |     8       |        455     |     230      | 5140     |       24.8     |  82       | US       |
```

## Data Loading

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       |
```

## Data Transformation

**Result Preview:**

```markdown
|    | Car                       |   MPG |   Cylinders |   Displacement |   Horsepower |   Weight |   Acceleration |   Model | Origin   | RegionCategory   |
|---:|:--------------------------|------:|------------:|---------------:|-------------:|---------:|---------------:|--------:|:---------|:-----------------|
|  0 | Chevrolet Chevelle Malibu |    18 |           8 |            307 |          130 |     3504 |           12   |      70 | US       | Domestic         |
|  1 | Buick Skylark 320         |    15 |           8 |            350 |          165 |     3693 |           11.5 |      70 | US       | Domestic         |
|  2 | Plymouth Satellite        |    18 |           8 |            318 |          150 |     3436 |           11   |      70 | US       | Domestic         |
|  3 | AMC Rebel SST             |    16 |           8 |            304 |          150 |     3433 |           12   |      70 | US       | Domestic         |
|  4 | Ford Torino               |    17 |           8 |            302 |          140 |     3449 |           10.5 |      70 | US       | Domestic         |
|  5 | Ford Galaxie 500          |    15 |           8 |            429 |          198 |     4341 |           10   |      70 | US       | Domestic         |
|  6 | Chevrolet Impala          |    14 |           8 |            454 |          220 |     4354 |            9   |      70 | US       | Domestic         |
|  7 | Plymouth Fury iii         |    14 |           8 |            440 |          215 |     4312 |            8.5 |      70 | US       | Domestic         |
|  8 | Pontiac Catalina          |    14 |           8 |            455 |          225 |     4425 |           10   |      70 | US       | Domestic         |
|  9 | AMC Ambassador DPL        |    15 |           8 |            390 |          190 |     3850 |            8.5 |      70 | US       | Domestic         |
```

