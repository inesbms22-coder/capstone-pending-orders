# Pending Orders Monitoring Dashboard

Capstone Project sviluppato durante il percorso Data Analytics di EPICODE.

## Project Overview

Il progetto ha l'obiettivo di analizzare e monitorare gli ordini pending di un e-commerce, individuando eventuali criticità come ritardi, errori operativi e ordini bloccati nel processo di evasione.

## Technologies

- Python
- Pandas
- NumPy
- Power BI

## Data Analysis

Python è stato utilizzato per:

- generare e preparare il dataset
- individuare gli ordini pending
- calcolare i giorni di permanenza nello stato pending
- classificare gli ordini per livello di priorità
- assegnare l'owner responsabile
- definire l'azione da intraprendere

Le principali informazioni generate sono:

- Pending Days
- Priority
- Owner
- Action
- Issue Type

## Power BI Dashboard

I dati elaborati con Python sono stati utilizzati in Power BI per creare una dashboard interattiva contenente:

- Total Pending Orders
- High Priority Orders
- Average Pending Days
- Total Pending Value
- Pending Orders by Owner
- Pending Orders by Issue Type
- filtri per Country, Warehouse, Owner e Priority
- tabella di dettaglio degli ordini pending


## Project Structure

```text
Capstone_Pending_Orders
│
├── data
│   ├── orders_raw.csv
│   └── pending_orders_final.csv
│
├── pending_orders_analysis.py
│
└── Pending_Orders_Monitoring_Dashboard.pbix

```

## Author

Ines
