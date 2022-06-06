from app import app

# Import blueprint
from app.projects.dashboard.views import dashboardBlueprint
from app.projects.admin.views import adminBlueprint
from app.projects.home.views import homeBlueprint
from app.projects.errors.views import errorsBlueprint
from app.projects.database.views import databaseKema

# Register blueprint
app.register_blueprint(dashboardBlueprint, url_prefix="/dashboard")
app.register_blueprint(adminBlueprint, url_prefix="/admin")
app.register_blueprint(homeBlueprint, url_prefix="/")
app.register_blueprint(errorsBlueprint, url_prefix="/error")
app.register_blueprint(databaseKema, url_prefix="/database")
