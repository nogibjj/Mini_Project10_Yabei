## Data Loading

**Result Preview:**

```markdown
|    | Model                                                         |   FuelEfficiency |   EngineCyl |   EngineDisp |   Power |   CarWeight |   ZeroToSixty |   YearModel | ManufactureRegion   |
|---:|:--------------------------------------------------------------|-----------------:|------------:|-------------:|--------:|------------:|--------------:|------------:|:--------------------|
|  0 | Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  1 | Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  2 | Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US        |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  3 | AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US             |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  4 | Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US               |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  5 | Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  6 | Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US           |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  7 | Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  8 | Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  9 | AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
```

## Data Loading

**Result Preview:**

```markdown
|    | Model                                                         |   FuelEfficiency |   EngineCyl |   EngineDisp |   Power |   CarWeight |   ZeroToSixty |   YearModel | ManufactureRegion   |
|---:|:--------------------------------------------------------------|-----------------:|------------:|-------------:|--------:|------------:|--------------:|------------:|:--------------------|
|  0 | Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  1 | Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  2 | Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US        |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  3 | AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US             |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  4 | Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US               |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  5 | Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  6 | Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US           |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  7 | Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  8 | Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
|  9 | AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     |
```

## Data Transformation

**Result Preview:**

```markdown
|    | Model                                                         |   FuelEfficiency |   EngineCyl |   EngineDisp |   Power |   CarWeight |   ZeroToSixty |   YearModel | ManufactureRegion   | RegionCategory   |
|---:|:--------------------------------------------------------------|-----------------:|------------:|-------------:|--------:|------------:|--------------:|------------:|:--------------------|:-----------------|
|  0 | Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  1 | Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  2 | Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US        |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  3 | AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US             |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  4 | Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US               |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  5 | Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  6 | Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US           |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  7 | Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  8 | Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US          |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
|  9 | AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US         |              nan |         nan |          nan |     nan |         nan |           nan |         nan |                     | Imported         |
```

