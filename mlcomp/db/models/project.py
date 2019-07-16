import sqlalchemy as sa

from mlcomp.db.models.base import Base


class Project(Base):
    __tablename__ = 'project'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    class_names = sa.Column(sa.LargeBinary, nullable=False)


__all__ = ['Project']