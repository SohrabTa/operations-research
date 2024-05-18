import gurobipy as gp
from gurobipy import GRB

from print_solution import print_solution

model = gp.Model("airline_shift")

shift_1 = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="shift_1")
shift_2 = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="shift_2")
shift_3 = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="shift_3")
shift_4 = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="shift_4")
shift_5 = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="shift_5")

model.addConstr(shift_1 >= 48)
model.addConstr(shift_1 + shift_2 >= 79)
model.addConstr(shift_1 + shift_2 + shift_3 >= 87)
model.addConstr(shift_2 + shift_3 >= 64)
model.addConstr(shift_3 + shift_4 >= 82)
model.addConstr(shift_4 >= 43)
model.addConstr(shift_4 + shift_5 >= 52)
model.addConstr(shift_5 >= 15)


model.setObjective(shift_1 + shift_2 + shift_3 + shift_4 + shift_5, GRB.MINIMIZE)

model.optimize()

print_solution(model)