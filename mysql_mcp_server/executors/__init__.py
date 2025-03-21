# -*- coding:utf-8 -*-
import inspect
import sys

from .create_table import execute_create_table
from .desc_table import execute_desc_table
from .explain import execute_explain
from .insert_query import execute_insert_query
from .insight_starter import execute_insight_starter
from .invoke_viz_pro import excute_invoke_viz_pro
from .select_query import execute_select_query
from .show_tables import execute_show_tables

__all__ = [
    "execute_create_table",
    "execute_desc_table",
    "execute_explain",
    "execute_insert_query",
    "execute_insight_starter",
    "excute_invoke_viz_pro",
    "execute_select_query",
    "execute_show_tables",
]

TOOLS_DEFINITION = [
    obj
    for name, obj in inspect.getmembers(sys.modules[__name__])
    if inspect.isfunction(obj) and hasattr(obj, "_is_tool") and obj._is_tool
]
