import gurobipy as gp
from gurobipy import GRB

from print_solution import print_solution

model = gp.Model("study_hours")

subject_1_first_30_hours = model.addVar(lb= 0, ub=30, vtype=GRB.CONTINUOUS, name="subject_1_first_30_hours")
subject_1_after_30_hours = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="subject_1_after_30_hours")
subject_2_first_6_hours = model.addVar(lb= 0, ub=6, vtype=GRB.CONTINUOUS, name="subject_2_first_6_hours")
subject_2_after_6_hours = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="subject_2_after_6_hours")
subject_3_first_5_hours = model.addVar(lb= 0, ub=5, vtype=GRB.CONTINUOUS, name="subject_3_first_5_hours")
subject_3_next_10_hours = model.addVar(lb= 0, ub=10, vtype=GRB.CONTINUOUS, name="subject_3_next_10_hours")
subject_3_after_15_hours = model.addVar(lb= 0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="subject_3_after_15_hours")
grade_subject_1 = model.addVar(lb= 1.0, ub=4.0, vtype=GRB.CONTINUOUS, name="grade_subject_1")
grade_subject_2 = model.addVar(lb= 1.0, ub=4.0, vtype=GRB.CONTINUOUS, name="grade_subject_2")
grade_subject_3 = model.addVar(lb= 1.0, ub=4.0, vtype=GRB.CONTINUOUS, name="grade_subject_3")

model.addConstr(grade_subject_1 == 8.0 - 0.1 * subject_1_first_30_hours - 0.05 * subject_1_after_30_hours)
model.addConstr(grade_subject_2 == 3.4 - 0.1 * subject_2_first_6_hours - 0.06 * subject_2_after_6_hours)
model.addConstr(grade_subject_3 == 6.0 - 0.2 * subject_3_first_5_hours - 0.1 * subject_3_next_10_hours - 0.05 * subject_3_after_15_hours)
model.addConstr(subject_1_first_30_hours + subject_1_after_30_hours + subject_2_first_6_hours + subject_2_after_6_hours + subject_3_first_5_hours + subject_3_next_10_hours + subject_3_after_15_hours <= 150)

model.setObjective(grade_subject_1 + grade_subject_2 + grade_subject_3, GRB.MINIMIZE)

model.optimize()

print_solution(model)