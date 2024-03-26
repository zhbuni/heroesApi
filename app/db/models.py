from sqlalchemy import Column, Integer, ForeignKey, Double, String, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class RolePresences(Base):
    __tablename__ = "role_presences"
    id: Mapped[int] = Column(Integer, primary_key=True)
    winrate = Column(Double, nullable=False)
    presence = Column(Double, nullable=False)
    hero_id = Column(Integer, ForeignKey("heroes.id"), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    role: Mapped["Roles"] = relationship()


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return "<Role(name='%s')>" % self.name


class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return "<Hero(name='%s')>" % self.name


class CounterHeroes(Base):
    __tablename__ = "counter_heroes"

    id = Column(Integer, primary_key=True)
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"), nullable=False)
    counter_hero_id: Mapped[int] = mapped_column(
        ForeignKey("heroes.id"), nullable=False
    )
    winrate: Mapped[int]

    hero: Mapped["Heroes"] = relationship(foreign_keys=[hero_id])

    counter_hero: Mapped["Heroes"] = relationship(foreign_keys=[counter_hero_id])
