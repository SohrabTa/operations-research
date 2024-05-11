import gurobipy as gp
from gurobipy import GRB

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

if model.SolCount > 0:
    print(f"Objective value: {model.objVal:.2f}")
    all_vars = model.getVars()
    values = model.getAttr("X", all_vars)
    names = model.getAttr("VarName", all_vars)

    for name, val in zip(names, values):
        print(f"{name} = {val:.2f}")
else:
    print("No solution found.")
        