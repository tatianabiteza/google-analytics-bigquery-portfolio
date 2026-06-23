print("\nTop events:")
print(df["event_name"].value_counts())
import matplotlib.pyplot as plt

# --------------------------
# 1. Event count chart
# --------------------------
event_counts = df["event_name"].value_counts()

plt.figure(figsize=(8,5))
event_counts.plot(kind="bar", color="skyblue")
plt.title("Website Events Overview")
plt.xlabel("Event Type")
plt.ylabel("Count")

plt.savefig("event_chart.png")
plt.close()

print("Chart saved: event_chart.png")


# --------------------------
# 2. Top events pie chart (optional but nice)
# --------------------------
plt.figure(figsize=(6,6))
event_counts.plot(kind="pie", autopct='%1.1f%%')
plt.title("Event Distribution")

plt.savefig("event_pie.png")
plt.close()

print("Pie chart saved: event_pie.png")
