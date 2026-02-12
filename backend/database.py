# The create_engine function is a primary way to crate an engine instance which
# Acts as a central source of connectivity to a specific data base
from sqlalchemy import create_engine
# Session maker is another standardied tool that allows you to have the same configuration parameters
# Declarative base connects the Object orientated structure with the relational database.
from sqlalchemy.orm import sessionmaker, declarative_base
