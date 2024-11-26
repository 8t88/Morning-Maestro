import json
from typing import Any, List, Optional

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from model.chorus_generator import generate_wav

from loguru import logger
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]


api_router = APIRouter()


# @api_router.get("/health", response_model=schemas.Health, status_code=200)
# def health() -> dict:
#     """
#     Root Get
#     """
#     health = schemas.Health(
#         name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
#     )

#     return health.dict()


@api_router.post("/generate_chorus", response_model=PredictionResults, status_code=200)
async def generate_chorus(input_data: List) -> Any:
    """
    Make chorus 
    """

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data}")
    chorus_result = generate_wav(input_data)[0]

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return chorus_result