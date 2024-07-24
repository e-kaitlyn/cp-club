prov = ['Newfoundland','Nova Scotia','Prince Edward Island','New Brunswick','Manitoba','Saskatchewan','Alberta',"British Columbia","Nunavut or Northwest Territories",'Yukon','Quebec','Quebec','Quebec','Ontario','Ontario','Ontario','Ontario','Ontario']
char = ['A' ,'B','C','E','R','S','T','V','X','Y','G','H','J','K','L','M','N','P']
postal = input()
province=postal[0]
rural = postal[1]
ind = char.index(province)
p = prov[ind]
if rural ==0:
    r="rural"
else:
    r = "urban"

print(p,r)