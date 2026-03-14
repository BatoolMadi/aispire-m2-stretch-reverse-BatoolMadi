# Stretch 2: Reverse-Engineer the Pipeline

**This assignment is optional and ungraded.** It is designed for learners who want additional practice with data cleaning and analysis pipelines.

## The Task

You have two things:

1. **Raw data** (`data/transit_ridership.csv`) — a messy public transit ridership dataset with inconsistent date formats, typos, missing values, duplicates, and invalid entries.
2. **Expected outputs** (`expected_output/`) — the cleaned summary statistics (`summary.json`) and four charts (PNGs) that a correct pipeline produces from this raw data.

Your job: **write the pipeline that transforms the raw data into these expected outputs.**

## What to Build

Write a Python script (or notebook) that:

1. Loads the raw CSV
2. Cleans and standardizes the data (dates, categories, missing values, duplicates, invalid entries)
3. Produces a `summary.json` matching the structure and values in `expected_output/summary.json`
4. Produces four charts that match the expected PNGs

## How to Validate

Compare your outputs against the expected ones:

- **summary.json** — diff your output against the expected file. Values should match exactly.
- **Charts** — visual comparison. Your charts should show the same data patterns and structure; exact styling differences are fine.

## Hints

The raw data has multiple categories of messiness. Before writing any transformation code, explore the dataset and catalog every issue you find. The expected outputs will tell you what "clean" looks like — work backward from there.

## Dataset Details

- ~2000 rows of bus route ridership data covering January–December 2024
- 10 columns: `date`, `route_id`, `direction`, `boarding_count`, `alighting_count`, `vehicle_type`, `trip_duration_min`, `weather`, `temperature_c`, `is_holiday`
