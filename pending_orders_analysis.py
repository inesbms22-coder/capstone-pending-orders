import pandas as pd
import numpy as np

np.random.seed(42)

n_orders = 2000

countries = ["IT", "FR", "ES", "DE", "US", "UK"]

warehouses = [
    "WH_EU",
    "WH_US",
    "WH_UK"
]

statuses = [
    "Shipped",
    "Pending",
    "Pending",
    "Pending",
    "Cancelled"
]

issues = [
    "Stock Issue",
    "Payment Issue",
    "Warehouse Delay",
    "Shipping Error",
    "Technical Error",
    "Address Issue"
]

today = pd.Timestamp("2026-10-15")

data = []

for i in range(n_orders):

    order_date = today - pd.Timedelta(
        days=np.random.randint(0, 60)
    )

    shipment_creation_date = order_date + pd.Timedelta(
        days=np.random.randint(0, 3)
    )

    status = np.random.choice(statuses)

    if status == "Pending":
        issue = np.random.choice(issues)
    else:
        issue = None

    data.append({
        "order_id": f"ORD-{10000+i}",
        "order_date": order_date,
        "shipment_creation_date": shipment_creation_date,
        "country": np.random.choice(countries),
        "warehouse": np.random.choice(warehouses),
        "status": status,
        "issue_type": issue,
        "order_value": round(
            np.random.uniform(50, 1200),
            2
        )
    })

df = pd.DataFrame(data)

df.to_csv(
    "data/orders_raw.csv",
    index=False
)

print(df.head())

print("\nDataset creato!")

print(
    f"Numero ordini: {len(df)}"
)

# Seleziono solo gli ordini Pending
pending = df[df["status"] == "Pending"].copy()

# Calcolo da quanti giorni ogni ordine è Pending
pending["pending_days"] = (
    today - pending["shipment_creation_date"]
).dt.days.clip(lower=0)

print("\nOrdini Pending:")
print(pending.head())

print(f"\nNumero ordini Pending: {len(pending)}")

# Assegno una priorità in base ai giorni di pending
def assign_priority(days):
    if days >= 7:
        return "HIGH"
    elif days >= 3:
        return "MEDIUM"
    else:
        return "LOW"

pending["priority"] = pending["pending_days"].apply(assign_priority)

print("\nOrdini con priorità:")
print(
    pending[
        ["order_id", "pending_days", "priority"]
    ].head()
)

# Assegno l'owner in base al tipo di problema
def assign_owner(issue):
    if issue in ["Stock Issue", "Warehouse Delay"]:
        return "WAREHOUSE"

    elif issue in ["Technical Error", "Shipping Error"]:
        return "TECH"

    elif issue == "Payment Issue":
        return "BACK OFFICE"

    elif issue == "Address Issue":
        return "CUSTOMER SERVICE"

    else:
        return "OTHER"

pending["owner"] = pending["issue_type"].apply(assign_owner)

print("\nOrdini con Owner:")
print(
    pending[
        ["order_id", "issue_type", "owner"]
    ].head()
)


# Assegno l'azione da fare in base ai giorni di pending e all'owner
def assign_action(row):

    if row["pending_days"] < 3:
        return "NO ACTION"

    elif row["owner"] == "WAREHOUSE":
        return "WH FOLLOW UP"

    elif row["owner"] == "TECH":
        return "TECH FOLLOW UP"

    elif row["owner"] == "BACK OFFICE":
        return "PAYMENT CHECK"

    elif row["owner"] == "CUSTOMER SERVICE":
        return "CUSTOMER FOLLOW UP"

    else:
        return "CHECK"

pending["action"] = pending.apply(assign_action, axis=1)

print("\nOrdini con Action:")
print(
    pending[
        ["order_id", "pending_days", "owner", "action"]
    ].head()
)


# Seleziono le colonne utili per il monitoraggio
final_columns = [
    "order_id",
    "order_date",
    "shipment_creation_date",
    "country",
    "warehouse",
    "status",
    "issue_type",
    "order_value",
    "pending_days",
    "priority",
    "owner",
    "action"
]

pending_final = pending[final_columns]

# Salvo il dataset finale
pending_final.to_csv(
    "data/pending_orders_final.csv",
    index=False
)

print("\nFile finale creato!")
print(f"Totale ordini pending: {len(pending_final)}")