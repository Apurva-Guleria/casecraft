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
    
class ClueDB(Base):
    __tablename__ = "clues"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_important = Column(Boolean, nullable=False)
    
class InvestigationDB(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    clue_id = Column(Integer, ForeignKey("clues.id"), nullable=False)
    is_discovered = Column(Boolean, nullable=False)