from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# Import your models so that SQLModel knows about them

# The SQLModel.metadata object contains all the table definitions.
# We will import this into Alembic's environment script.
metadata = SQLModel.metadata

# url: str = settings.SUPABASE_URL.get_secret_value()
# key: str = settings.SUPABASE_KEY.get_secret_value()
# supabase: Client = create_client(url, key)

# Create the SQLAlchemy engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL.get_secret_value(), echo=False)


def get_session():
    """Dependency to get a database session for each request."""
    with Session(engine) as session:
        yield session
