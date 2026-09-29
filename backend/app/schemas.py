from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

class ExperimentBase(BaseModel):
    name: str
    description: Optional[str] = None
    organism: str
    variety: Optional[str] = None
    microorganism: str
    start_date: Optional[date] = None
    is_demo: bool = False

class ExperimentCreate(ExperimentBase):
    pass

class ExperimentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    organism: Optional[str] = None
    variety: Optional[str] = None
    microorganism: Optional[str] = None
    start_date: Optional[date] = None

class TreatmentBase(BaseModel):
    name: str
    code: str
    concentration: Optional[float] = None
    concentration_unit: Optional[str] = None
    order_index: int

class TreatmentCreate(TreatmentBase):
    experiment_id: int

class TreatmentUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    concentration: Optional[float] = None
    concentration_unit: Optional[str] = None
    order_index: Optional[int] = None

class Treatment(TreatmentBase):
    id: int
    experiment_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ReplicaBase(BaseModel):
    replica_code: str
    seed_batch: Optional[str] = None
    inoculum_batch: Optional[str] = None
    inoculation_date: Optional[date] = None
    inoculation_method: Optional[str] = None
    environment_conditions: Optional[str] = None
    observations: Optional[str] = None

class ReplicaCreate(ReplicaBase):
    experiment_id: int
    treatment_id: int

class Replica(ReplicaBase):
    id: int
    experiment_id: int
    treatment_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class MeasurementBase(BaseModel):
    day_number: int
    variable_name: str
    variable_group: str
    value: Optional[float] = None
    unit: Optional[str] = None
    missing_value_code: Optional[str] = None
    missing_reason: Optional[str] = None
    observation: Optional[str] = None
    source: Optional[str] = None

class MeasurementCreate(MeasurementBase):
    experiment_id: int
    treatment_id: int
    replica_id: int
    date: Optional[date] = None

class MeasurementUpdate(BaseModel):
    day_number: Optional[int] = None
    value: Optional[float] = None
    unit: Optional[str] = None
    missing_value_code: Optional[str] = None
    missing_reason: Optional[str] = None
    observation: Optional[str] = None

class Measurement(MeasurementBase):
    id: int
    experiment_id: int
    treatment_id: int
    replica_id: int
    date: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class Experiment(ExperimentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    treatments: List[Treatment] = []
    replicas: List[Replica] = []
    
    class Config:
        from_attributes = True
