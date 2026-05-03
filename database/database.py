from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config import settings

from models import Base


engine = create_async_engine(
    url=settings.database_url,
    echo=True
)

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)
