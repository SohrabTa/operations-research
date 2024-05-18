import gurobipy as gp

def print_solution(model: gp.Model):
    if model.SolCount > 0:
        print(f"Objective value: {model.objVal:.2f}")
        all_vars = model.getVars()
        values = model.getAttr("X", all_vars)
        names = model.getAttr("VarName", all_vars)

        for name, val in zip(names, values):
            print(f"{name} = {val:.2f}")
    else:
        print("No solution found.")
            