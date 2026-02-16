from pandas import read_sql, to_datetime
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database, replace all with your actual credentials
engine = create_engine("postgresql://yanolive:mysecretpassword@localhost/piscineds")

# Number of customers who made a purchase per day
df = read_sql("SELECT event_time::date, COUNT(distinct user_id) as total_users FROM customers WHERE event_type = 'purchase' GROUP BY event_time::date", engine)

df.set_index("event_time")["total_users"].plot()
plt.ylabel("Number of Customers")
plt.xlabel("")
plt.xticks(
    [to_datetime("2022-10-01"),
     to_datetime("2022-11-01"),
     to_datetime("2022-12-01"),
     to_datetime("2023-01-01")],
     ["Oct", "Nov", "Dec", "Jan"])
plt.savefig("chart.buyers.png", dpi=150, bbox_inches='tight')