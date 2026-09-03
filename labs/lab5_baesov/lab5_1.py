from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


#levo afektira desno
model=DiscreteBayesianNetwork([('Budget', 'Interest'),('Marketing', 'Interest'), ('Interest', 'Review'), ('Interest', 'Testdrive'), ('Review', 'Purchase'), ('Testdrive', 'Purchase'), ('Discount', 'Purchase')])

cpd_budget=TabularCPD(
    variable='Budget',
    variable_card=2,
    values=[[0.65], [0.35]]
)

cpd_marketing=TabularCPD(
    variable='Marketing',
    variable_card=2,
    values=[[0.55], [0.45]]
)

cpd_discount=TabularCPD(
    variable='Discount',
    variable_card=2,
    values=[[0.75], [0.25]]
)


cpd_interest=TabularCPD(
    variable='Interest',
    variable_card=2,
    values=[[0.88, 0.35, 0.28, 0.07],
            [0.12, 0.65, 0.72, 0.93]],
    evidence=['Budget', 'Marketing'],
    evidence_card=[2,2]
)

cpd_review=TabularCPD(
    variable='Review',
    variable_card=2,
    values=[
        [0.80, 0.20],
        [0.20, 0.80]
    ],
    evidence=['Interest'],
    evidence_card=[2]
)

cpd_testdrive=TabularCPD(
    variable='Testdrive',
    variable_card=2,
    values=[
        [0.70, 0.15],
        [0.30, 0.85]
    ],
    evidence=['Interest'],
    evidence_card=[2]
)

cpd_purchase=TabularCPD(
    variable='Purchase',
    variable_card=2,
    values=[
        [0.96, 0.68, 0.52, 0.25, 0.45, 0.22, 0.12, 0.03],
        [0.04, 0.32, 0.48, 0.75, 0.55, 0.78, 0.88, 0.97]
    ],
    evidence=['Review', 'Testdrive', 'Discount'],
    evidence_card=[2, 2, 2]
)


model.add_cpds(cpd_budget, cpd_marketing, cpd_interest, cpd_review, cpd_testdrive, cpd_discount, cpd_purchase)
model.check_model()

#1.P(I=1 | B=1, M=1)
inf=VariableElimination(model)
result1=inf.query(variables=['Interest'], evidence={'Budget':1, 'Marketing':1})
#print(result1)

#2.P(R=1 | I = 1)
result2=inf.query(variables=['Review'], evidence={'Interest':1})
#print(result2)

#3.P(C=1 | T = 1)
result3=inf.query(variables=['Purchase'], evidence={'Testdrive':1})
#print(result3)

#4.P(B=1 | I = 1)
result4=inf.query(variables=['Budget'], evidence={'Interest':1})
#print(result4)

#5.P(M=1 | I = 1)
result5=inf.query(variables=['Marketing'], evidence={'Interest':1})
#print(result5)

#6.P(T=1 | C = 1, R = 0)
result6=inf.query(variables=['Testdrive'], evidence={'Purchase':1, 'Review':0})
print(result6)