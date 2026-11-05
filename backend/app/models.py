from sqlalchemy import Column, Integer, String , Boolean , ForeignKey
from backend.app.database import Base


class CaseDB(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)

class SuspectDB(Base):
    __tablename__ = "suspects"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_guilty = Column(Boolean, nullable=False) 