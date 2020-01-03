#!/usr/bin/python
# encoding=utf8
from climate.climate_route import climate_route
from operation.operation_route import operation_route

route_init_func = {"climate": climate_route,
                   "operation": operation_route}
