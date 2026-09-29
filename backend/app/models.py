from sqlalchemy import Column, Integer, String, Float, Date, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    organism = Column(String, nullable=False)
    variety = Column(String, nullable=True)
    microorganism = Column(String, nullable=False)
    start_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_demo = Column(Boolean, default=False)
    
    treatments = relationship("Treatment", back_populates="experiment", cascade="all, delete-orphan")
    replicas = relationship("Replica", back_populates="experiment", cascade="all, delete-orphan")
    measurements = relationship("Measurement", back_populates="experiment", cascade="all, delete-orphan")

class Treatment(Base):
    __tablename__ = "treatments"

    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"), nullable=False)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    concentration = Column(Float, nullable=True)
    concentration_unit = Column(String, nullable=True)
    order_index = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    experiment = relationship("Experiment", back_populates="treatments")
    replicas = relationship("Replica", back_populates="treatment", cascade="all, delete-orphan")
    measurements = relationship("Measurement", back_populates="treatment", cascade="all, delete-orphan")

class Replica(Base):
    __tablename__ = "replicas"

    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"), nullable=False)
    treatment_id = Column(Integer, ForeignKey("treatments.id"), nullable=False)
    replica_code = Column(String, nullable=False)
    seed_batch = Column(String, nullable=True)
    inoculum_batch = Column(String, nullable=True)
    inoculation_date = Column(Date, nullable=True)
    inoculation_method = Column(String, nullable=True)
    environment_conditions = Column(Text, nullable=True)
    observations = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    experiment = relationship("Experiment", back_populates="replicas")
    treatment = relationship("Treatment", back_populates="replicas")
    measurements = relationship("Measurement", back_populates="replica", cascade="all, delete-orphan")

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"), nullable=False)
    treatment_id = Column(Integer, ForeignKey("treatments.id"), nullable=False)
    replica_id = Column(Integer, ForeignKey("replicas.id"), nullable=False)
    date = Column(Date, nullable=True)
    day_number = Column(Integer, nullable=False)
    variable_name = Column(String, nullable=False)
    variable_group = Column(String, nullable=False)
    value = Column(Float, nullable=True)
    unit = Column(String, nullable=True)
    missing_value_code = Column(String, nullable=True)
    missing_reason = Column(String, nullable=True)
    observation = Column(Text, nullable=True)
    source = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    experiment = relationship("Experiment", back_populates="measurements")
    treatment = relationship("Treatment", back_populates="measurements")
    replica = relationship("Replica", back_populates="measurements")
