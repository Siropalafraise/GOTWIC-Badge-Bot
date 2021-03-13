#%% Imports
import numpy as np
import pulp

#%% Fonction
def FonctionBadges(NombreBase,NombreEquipments,BonusGrey=2,BonusGreen=3.75,BonusBlue=7.5,BonusPurple=15,BonusGold=25):
    """https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html"""
    
    NombreGoldMax=np.floor(NombreBase/256)
    NombrePurpleMax=np.floor((NombreBase)/64)
    NombreBlueMax=np.floor((NombreBase)/16)
    NombreGreenMax=np.floor((NombreBase)/4)
    NombreGreyMax=np.floor((NombreBase)/1)
    
    # Problem
    Problem=pulp.LpProblem("BadgeProblem",pulp.LpMaximize)
    # Variables with lower and upper bounds and type
    NombreGrey=pulp.LpVariable("NombreGrey",0,NombreGreyMax,pulp.LpInteger)
    NombreGreen=pulp.LpVariable("NombreGreen",0,NombreGreenMax,pulp.LpInteger)
    NombreBlue=pulp.LpVariable("NombreBlue",0,NombreBlueMax,pulp.LpInteger)
    NombrePurple=pulp.LpVariable("NombrePurple",0,NombrePurpleMax,pulp.LpInteger)
    NombreGold=pulp.LpVariable("NombreGold",0,NombreGoldMax,pulp.LpInteger)
    # Objective function
    Problem+=NombreGrey*BonusGrey+NombreGreen*BonusGreen+NombreBlue*BonusBlue+NombrePurple*BonusPurple+NombreGold*BonusGold, "Fonction"
    # Constraints
    Problem+=NombreGrey+NombreGreen+NombreBlue+NombrePurple+NombreGold <= NombreEquipments, ""
    Problem+=0*NombreGrey+0*NombreGreen+0*NombreBlue+0*NombrePurple+256*NombreGold <= NombreBase, ""
    Problem+=0*NombreGrey+0*NombreGreen+0*NombreBlue+64*NombrePurple+256*NombreGold <= NombreBase, ""
    Problem+=0*NombreGrey+0*NombreGreen+16*NombreBlue+64*NombrePurple+256*NombreGold <= NombreBase, ""
    Problem+=0*NombreGrey+4*NombreGreen+16*NombreBlue+64*NombrePurple+256*NombreGold <= NombreBase, ""
    Problem+=1*NombreGrey+4*NombreGreen+16*NombreBlue+64*NombrePurple+256*NombreGold <= NombreBase, ""
    # Solving using PuLP's choice of Solver
    Problem.solve()
    
    Matrice=np.zeros((1,6))
    Matrice[0,0]=Problem.variables()[3].varValue #Grey
    Matrice[0,1]=Problem.variables()[2].varValue #Green
    Matrice[0,2]=Problem.variables()[0].varValue #Blue
    Matrice[0,3]=Problem.variables()[4].varValue #Purple
    Matrice[0,4]=Problem.variables()[1].varValue #Gold
    Matrice[0,5]=Matrice[0,0]*BonusGrey+Matrice[0,1]*BonusGreen+Matrice[0,2]*BonusBlue+Matrice[0,3]*BonusPurple+Matrice[0,4]*BonusGold
    
    return Matrice
