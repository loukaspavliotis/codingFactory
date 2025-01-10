from dataclasses import dataclass
from datetime import datetime

# DTO for User Creation
@dataclass
class UserCreateDTO:
    username: str
    password: str
    email: str

# DTO for User Summary
@dataclass
class UserSummaryDTO:
    username: str
    email: str
    date_joined: datetime

# DTO for Platform Statistics
@dataclass
class PlatformStatsDTO:
    total_users: int
    active_users: int
    latest_users: list  # List of UserSummaryDTO
    active_user_percentage: float  # New field to store active user percentage