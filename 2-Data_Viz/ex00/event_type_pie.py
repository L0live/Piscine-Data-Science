import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database, replace all with your actual credentials
engine = create_engine("postgresql://your_login:mysecretpassword@localhost/piscineds")


df = pd.read_sql("SELECT event_type, COUNT(*) as total FROM customers GROUP BY event_type", engine)

df.set_index("event_type")["total"].plot.pie(autopct='%1.1f%%', figsize=(8, 8), startangle=100, counterclock=False)
plt.ylabel("")
plt.savefig("pie.event_type.png", dpi=150, bbox_inches='tight')