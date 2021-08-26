from typing import Optional

from fastapi import HTTPException

from app.router import router
from modules.patients.utils import convert_to_lowercase_naming
from modules.table import exports


@router.get('/patients/{id}')
def get_patient_signatures_by_id(
        id: str,
        fields: Optional[str] = None,
        is_include: Optional[bool] = None
) -> dict:
    if patient_signatures := exports.get_data_from_table(id):
        if fields is None and is_include is None:
            return patient_signatures.dict(by_alias=True)
        elif fields is not None and is_include:
            return patient_signatures.dict(by_alias=True, include=set(convert_to_lowercase_naming(fields.split(','))))
        elif fields is not None and not is_include:
            return patient_signatures.dict(by_alias=True, exclude=set(convert_to_lowercase_naming(fields.split(','))))
    raise HTTPException(status_code=404, detail='Patient not found.')
