this code is implemented by python

1. open terminal
2. change to the directory where the assign3.py is
3. add the test data file to this work directory
4. enter command: python assign3.py ./data_file_name.txt query 
   (data_file_name.txt is the name of test data file, query is the query you are need to prove)

the output will show the steps needed to prove the query entered and the outcome 

Input data:
I first count the lines in the rules file and use this number of lines to initialize the two-dimensional
array. Then read file line by line.
Algorithm:
Backward chaining algorithm:
 I use the pseudo-code. The parameter of function slove() are rules--arrays and goals need
to be solved(the very first goals is the query we entered, such as a).
 Each step is :
 If goals is empty: return True
 If goals is not empty:
 Taking one goal from the stack goals, then search the rules array
 If match the rule header: add the rule body to goals and use function solve() to
 see whether goals can all be solved by this rule:
 If can solve: return True
 If cannt solve: drop this rule body from goals and search for next match
 rule
 If no match: return false
Depth- first:
 I declare the goals as a first--in--last--out stack.
Backtracking:
 Every time return False, it will backtrack to the corresponding current goal. Then i drop the
wrong goals, and try next rule with the help of FILO stack : goals.
Output:
The output is the process of solving the query entered.
 Such as: current goal is a
 To solve a need solve b
 To solve a need solve c
If we have several rules to solve b, for example 3 rules and the first two rules cannot solve then:
 Such as: c => b
 d^c => b
 d => b
 Current goal is b
 To solve b need solve c
 Fail
 To solve b need solve d
 To solve b need solve c
 Fail
 To solve b need solve d
 Then next goals to be solve
At the end of output, there will show True of all atom needed to prove query with the opposite
order of backward chaining if query is True. Or it will show False if query is False.
Solve q => p , p => q:
The algorithm will stuck in infinite loop, so we can apply limited--depth to avoid this situation.
The limited--depth can be set at least the number of rules in rule file