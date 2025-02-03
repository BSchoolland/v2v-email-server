"""
Custom field types for SQLAlchemy models.
"""
from typing import Any, Dict, Optional, Type

from sqlalchemy import JSON, String, TypeDecorator
import pydantic


class StrictString(TypeDecorator):
    """Strict string type that enforces max length."""
    
    impl = String
    cache_ok = True

    def process_bind_param(self, value: Optional[str], dialect: Any) -> Optional[str]:
        """Process the value before saving to database."""
        if value is not None and not isinstance(value, str):
            raise ValueError(f"Expected string, got {type(value)}")
        if value and self.impl.length and len(value) > self.impl.length:
            raise ValueError(f"String exceeds maximum length of {self.impl.length}")
        return value


class JSONType(TypeDecorator):
    """JSON type that validates against a Pydantic model."""
    
    impl = JSON
    cache_ok = True

    def __init__(self, schema: Optional[Type[pydantic.BaseModel]] = None) -> None:
        super().__init__()
        self.schema = schema

    def process_bind_param(self, value: Any, dialect: Any) -> Optional[Dict]:
        """Process the value before saving to database."""
        if value is None:
            return None
        if self.schema is not None:
            # Validate against schema if provided
            value = self.schema.model_validate(value).model_dump()
        return value

    def process_result_value(self, value: Any, dialect: Any) -> Any:
        """Process the value after loading from database."""
        if value is None:
            return None
        if self.schema is not None:
            return self.schema.model_validate(value)
        return value 