
import sys

#backward chaining
def solve(KB, goals):
    #if there is no extra goals to be prove, then the goal is true
    if goals == []:
        return True
    #else add extra goals to be proved
    current_goal = goals.pop()
    print 'current goal is %s'%current_goal
    for i in range(0, len(KB)):
        #find the corresponding rule
        if KB[i][0] == current_goal:
            for j in range(1, len(KB[i])):
                goals.append(KB[i][j])
                print '        prove %s          need prove %s'%(current_goal, KB[i][j])
            if solve(KB, goals) == True:
                print '%s is true'%current_goal
                return True
            else:

                print 'Fail to prove'
                for k in range(1, len(KB[i])-2):
                      print goals.pop()
    print 'Fail to prove'
    return False

# read KB file, input in two-dimmensional array
file_name = sys.argv[1]
num_line = sum(1 for line in open(file_name))
file_data = open(file_name, 'r')
KB = [[] for x in range(num_line)]
for i in range(0,num_line):
    data = file_data.readline().strip()
    data2 = data.split(" ")
    for j in range(0, len(data2)):
        KB[i].append(data2[j])
file_data.close()

#read goal query from input
query = sys.argv[2]
goals = []
goals.append(query)
print 'the query is %s'%goals[0]

#solve goal query
solve(KB, goals)