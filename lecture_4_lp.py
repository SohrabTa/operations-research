import gurobipy as gp
from gurobipy import GRB

from print_solution import print_solution

model = gp.Model("service_technicians")

experienced_technicians_in_month_1 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="experienced_technicians_in_month_1")
experienced_technicians_in_month_2 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="experienced_technicians_in_month_2")
experienced_technicians_in_month_3 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="experienced_technicians_in_month_3")
experienced_technicians_in_month_4 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="experienced_technicians_in_month_4")
experienced_technicians_in_month_5 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="experienced_technicians_in_month_5")

trainee_technicians_in_month_1 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="trainee_technicians_in_month_1")
trainee_technicians_in_month_2 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="trainee_technicians_in_month_2")
trainee_technicians_in_month_3 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="trainee_technicians_in_month_3")
trainee_technicians_in_month_4 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="trainee_technicians_in_month_4")
trainee_technicians_in_month_5 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="trainee_technicians_in_month_5")

model.addConstr(experienced_technicians_in_month_1 == 50)
model.addConstr(experienced_technicians_in_month_2 == 0.95 * experienced_technicians_in_month_1 + trainee_technicians_in_month_1)
model.addConstr(experienced_technicians_in_month_3 == 0.95 * experienced_technicians_in_month_2 + trainee_technicians_in_month_2)
model.addConstr(experienced_technicians_in_month_4 == 0.95 * experienced_technicians_in_month_3 + trainee_technicians_in_month_3)
model.addConstr(experienced_technicians_in_month_5 == 0.95 * experienced_technicians_in_month_4 + trainee_technicians_in_month_4)
model.addConstr(160 * experienced_technicians_in_month_1 - 50 * trainee_technicians_in_month_1 >= 6000)
model.addConstr(160 * experienced_technicians_in_month_2 - 50 * trainee_technicians_in_month_2 >= 7000)
model.addConstr(160 * experienced_technicians_in_month_3 - 50 * trainee_technicians_in_month_3 >= 8000)
model.addConstr(160 * experienced_technicians_in_month_4 - 50 * trainee_technicians_in_month_4 >= 9500)
model.addConstr(160 * experienced_technicians_in_month_5 - 50 * trainee_technicians_in_month_5 >= 11000)

model.setObjective(2000 * (experienced_technicians_in_month_1 + experienced_technicians_in_month_2 + experienced_technicians_in_month_3 + experienced_technicians_in_month_4 + experienced_technicians_in_month_5) + 1000 * (trainee_technicians_in_month_1 + trainee_technicians_in_month_2 + trainee_technicians_in_month_3 + trainee_technicians_in_month_4 + trainee_technicians_in_month_5), GRB.MINIMIZE)

model.optimize()

print_solution(model)