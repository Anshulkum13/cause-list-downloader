# 🏛️ Real-Time Cause List Downloader

A web-based UI tool to fetch and download daily cause lists from Indian eCourts portals in **real time**, based on user input. Supports both granular court selection and bulk downloads for entire court complexes.

## 🔗 Live Sources
- [eCourts Cause List Portal](https://services.ecourts.gov.in/ecourtindia_v6/?p=cause_list/)
- [Delhi District Courts Daily Board](https://newdelhi.dcourts.gov.in/cause-list-%e2%81%84-daily-board/)

---

## 📦 Features

- 🔍 Real-time data fetch: Select State, District, Court Complex, and Court Name dynamically.
- 📅 Date-based filtering: Choose any date to fetch the corresponding cause list.
- 📥 PDF download: Automatically downloads cause list PDFs for selected courts.
- 🧠 Smart bulk mode: Enter only Court Complex to fetch cause lists for **all judges** in that complex.
- ⚡ No local storage: Data is fetched live from official portals—no sample caching.

---

## 🖥️ UI Overview

| Field            | Description                                      |
|------------------|--------------------------------------------------|
| State Name       | Dropdown populated from live portal              |
| District         | Auto-populated based on selected state           |
| Court Complex    | Select or input manually                         |
| Court Name       | Optional – leave blank to fetch all in complex   |
| Date             | Select any valid date for cause list             |

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/cause-list-downloader.git
cd cause-list-downloader
