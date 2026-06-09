from services.database_service import DatabaseService
from views.dashboard_view import DashboardView


db = DatabaseService()
db.create_tables()

app = DashboardView()
app.mainloop()