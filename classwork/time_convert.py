# App that 
# IN: time in seconds
# OUT: time in HMS 

# INPUT

period_s = int(input("Write your period:"))

# OUTPUT
period_dd = period_s//(3600*24)
period_hh = period_s//3600
period_mm = (period_s - period_hh*3600)//60
period_ss = (period_s - period_hh*3600 - period_mm*60)

print("d:",period_dd,"h:",period_hh,"m:",period_mm,"s:",period_ss)