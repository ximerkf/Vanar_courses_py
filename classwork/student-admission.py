# application -> University -> approve

# INPUT DATA (1..10)
SCHOOL_general_mark = 2.5 #float
UNIVERSITY_minimal_mark = 7.5 #float

#STUDENT_money = 5000 #int
STUDENT_monthly_earn = 1000
UNIVERSITY_contract_cost = 10000 #int

STUDENT_powerful_dad = False #bool

# PROCASSING
approve = SCHOOL_general_mark >= UNIVERSITY_minimal_mark\
            or\
            STUDENT_monthly_earn * 12 >= UNIVERSITY_contract_cost\
            or\
            STUDENT_powerful_dad

# OUTPUT DATA 

print( "Will the student be approved?", approve ) 