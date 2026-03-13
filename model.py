from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    age: int
    gender: str
    income: float
    occupation: str
    category: Optional[str] = "General"
    marital_status: Optional[str] = "Single"
    state_of_residence: str

class Scheme(BaseModel):
    id: int
    name: str
    description: str
    required_age_min: Optional[int] = None
    required_age_max: Optional[int] = None
    max_income: Optional[float] = None
    target_gender: Optional[str] = "All"
    target_occupation: Optional[str] = "All"
    benefits: str

