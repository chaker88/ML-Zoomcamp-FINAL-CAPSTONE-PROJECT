# Create the FASTAPI input schema
from pydantic import BaseModel, Field
from typing import Optional

class ModelInput(BaseModel):
    """Schema for model input validation"""
    Employment: int = Field(..., description="Employment status")
    PreviousSalary: float = Field(..., description="Previous salary")
    YearsCode: float = Field(..., description="Years of coding experience")
    ComputerSkills: float = Field(..., description="Computer skills rating")
    Lang_AWS: int = Field(..., description="AWS language skill (0 or 1)")
    Lang_Bash_Shell: int = Field(..., alias="Lang_Bash/Shell", description="Bash/Shell skill (0 or 1)")
    Lang_CSharp: int = Field(..., alias="Lang_C#", description="C# skill (0 or 1)")
    Lang_Docker: int = Field(..., description="Docker skill (0 or 1)")
    Lang_Git: int = Field(..., description="Git skill (0 or 1)")
    Lang_HTML_CSS: int = Field(..., alias="Lang_HTML/CSS", description="HTML/CSS skill (0 or 1)")
    Lang_Java: int = Field(..., description="Java skill (0 or 1)")
    Lang_JavaScript: int = Field(..., description="JavaScript skill (0 or 1)")
    Lang_Microsoft_SQL_Server: int = Field(..., alias="Lang_Microsoft SQL Server", description="Microsoft SQL Server skill (0 or 1)")
    Lang_MySQL: int = Field(..., description="MySQL skill (0 or 1)")
    Lang_Node_js: int = Field(..., alias="Lang_Node.js", description="Node.js skill (0 or 1)")
    Lang_Other: int = Field(..., description="Other languages skill (0 or 1)")
    Lang_PostgreSQL: int = Field(..., description="PostgreSQL skill (0 or 1)")
    Lang_Python: int = Field(..., description="Python skill (0 or 1)")
    Lang_React_js: int = Field(..., alias="Lang_React.js", description="React.js skill (0 or 1)")
    Lang_SQL: int = Field(..., description="SQL skill (0 or 1)")
    Lang_TypeScript: int = Field(..., description="TypeScript skill (0 or 1)")
    Age_gt35: int = Field(..., alias="Age (>35)", description="Age greater than 35 (0 or 1)")
    edlevel_encoded: int = Field(..., description="Education level encoded")

    class Config:
        populate_by_name = True  # Allow both field name and alias
        schema_extra = {
            "example": {
                "Employment": 1,
                "PreviousSalary": 50000.0,
                "YearsCode": 7,
                "ComputerSkills": 4,
                "Lang_AWS": 0,
                "Lang_Bash/Shell": 1,
                "Lang_C#": 0,
                "Lang_Docker": 0,
                "Lang_Git": 1,
                "Lang_HTML/CSS": 0,
                "Lang_Java": 0,
                "Lang_JavaScript": 0,
                "Lang_Microsoft SQL Server": 0,
                "Lang_MySQL": 0,
                "Lang_Node.js": 1,
                "Lang_Other": 1,
                "Lang_PostgreSQL": 1,
                "Lang_Python": 1,
                "Lang_React.js": 0,
                "Lang_SQL": 0,
                "Lang_TypeScript": 0,
                "Age (>35)": 0,
                "edlevel_encoded": 3
            }
        }
