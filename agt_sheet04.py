import gurobipy as gp
from gurobipy import GRB
from print_solution import print_solution

model = gp.Model("maximin_rock_paper_scissors")

security_level = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="security_level")
probability_of_playing_rock = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_rock")
probability_of_playing_paper = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_paper")
probability_of_playing_scissors = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_scissors")

model.addConstr(probability_of_playing_rock + probability_of_playing_paper + probability_of_playing_scissors == 1)
model.addConstr(0 * probability_of_playing_rock + 1 * probability_of_playing_paper + -1 * probability_of_playing_scissors >= security_level)
model.addConstr(-1 * probability_of_playing_rock + 0 * probability_of_playing_paper + 1 * probability_of_playing_scissors >= security_level)
model.addConstr(1 * probability_of_playing_rock + -1 * probability_of_playing_paper + 0 * probability_of_playing_scissors >= security_level)

model.setObjective(security_level, GRB.MAXIMIZE)

model.optimize()

print_solution(model)

model = gp.Model("maximin_rock_paper_scissors_well")

security_level = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="security_level")
probability_of_playing_rock = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_rock")
probability_of_playing_paper = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_paper")
probability_of_playing_scissors = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_scissors")
probability_of_playing_well = model.addVar(lb=0, ub=1, vtype=GRB.CONTINUOUS, name="probability_of_playing_well")

model.addConstr(probability_of_playing_rock + probability_of_playing_paper + probability_of_playing_scissors + probability_of_playing_well == 1)
model.addConstr(0 * probability_of_playing_rock + 1 * probability_of_playing_paper + -1 * probability_of_playing_scissors + 1 * probability_of_playing_well >= security_level)
model.addConstr(-1 * probability_of_playing_rock + 0 * probability_of_playing_paper + 1 * probability_of_playing_scissors + - 1 * probability_of_playing_well >= security_level)
model.addConstr(1 * probability_of_playing_rock + -1 * probability_of_playing_paper + 0 * probability_of_playing_scissors + 1 * probability_of_playing_well >= security_level)
model.addConstr(-1 * probability_of_playing_rock + 1 * probability_of_playing_paper + -1 * probability_of_playing_scissors + 0 * probability_of_playing_well >= security_level)

model.setObjective(security_level, GRB.MAXIMIZE)

model.optimize()

print_solution(model)