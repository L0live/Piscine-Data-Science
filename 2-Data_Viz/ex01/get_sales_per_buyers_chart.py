from pandas import read_sql, to_datetime
from numpy import arange
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database, replace all with your actual credentials
engine = create_engine("postgresql://yanolive:mysecretpassword@localhost/piscineds")

# Average sales per customer per day
df = read_sql("SELECT event_time::date, SUM(price) / COUNT(distinct user_id) as average_sales_per_user FROM customers WHERE event_type = 'purchase' GROUP BY event_time::date", engine)

# df.set_index("event_time")["average_sales_per_user"].plot()
plt.stackplot(df["event_time"], df["average_sales_per_user"])
plt.ylabel("Average spend/customers in Altairian Dollars")
plt.yticks(range(0, 60, 5), arange(0, 60, 5).round(1))
plt.xlabel("")
plt.xticks(
    [to_datetime("2022-10-01"),
     to_datetime("2022-11-01"),
     to_datetime("2022-12-01"),
     to_datetime("2023-01-01")],
     ["Oct", "Nov", "Dec", "Jan"])
plt.savefig("chart.sales_per_buyers.png", dpi=150, bbox_inches='tight')