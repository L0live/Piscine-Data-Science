from pandas import read_sql
from numpy import arange
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database, replace all with your actual credentials
engine = create_engine("postgresql://yanolive:mysecretpassword@localhost/piscineds")

# Total sales per month
df = read_sql("SELECT date_trunc('month', event_time)::date as month, SUM(price) as total_sales FROM customers WHERE event_type = 'purchase' GROUP BY date_trunc('month', event_time)", engine)

df.set_index("month")["total_sales"].plot(kind="bar")
plt.ylabel("Total sales in millions of Altairian Dollars")
plt.yticks(range(0, 1600000, 200000), arange(0, 1.6, 0.2).round(1))
plt.xlabel("Month")
plt.xticks(range(4), ["Oct", "Nov", "Dec", "Jan"], rotation=0)
plt.savefig("chart.sales.png", dpi=150, bbox_inches='tight')