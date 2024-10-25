from fastapi import APIRouter
from sqlmodel import select

from db import SessionDep
from models import Plan

router = APIRouter()


@router.post("/plans")
def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db


@router.get("/plans", response_model=list[Plan])
def list_plan(session: SessionDep):
    plans = session.exec(select(Plan)).all()
    return plans
