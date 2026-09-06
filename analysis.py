import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("events.csv")

# Count unique users at each funnel stage
funnel_order = [
    "registration",
    "view_product",
    "add_to_cart",
    "purchase"
]

funnel = (
    df.groupby("event")["user_id"]
    .nunique()
    .reindex(funnel_order)
)

# Calculate conversion from registration
conversion = (funnel / funnel.iloc[0] * 100).round(1)

print("Users at each stage:")
print(funnel)

print("\nConversion from registration:")
print(conversion)

# Plot funnel
funnel.plot(kind="bar", title="Product Funnel")
plt.ylabel("Unique users")
plt.xlabel("Stage")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("product_funnel.png")
plt.show()
