Programming language: python

Execution step:
1. open terminal
2. change to working directory of assign3.py
3. add test-data file to this directory
4. enter command: python assign3.py ./data_file_name.txt query 
   - (data_file_name.txt is the name of test data file, query is the query you need to prove)

Input data:
1. count the lines in the rules file
2. use the number of lines to initialize the two-dimensional array. 
3. read file line by line.

Algorithm:
1. Backward chaining algorithm:
  - use the pseudo-code. The parameter of function slove() are rules(arrays) and goals need to be solved(the very first goals is the query we entered, such as a).
  - Each step is :
         - If goals is empty: return True
         - If goals is not empty:
              - Take one goal from the stack goals and search the rules array
                   - If match the rule header:  
                        - add the rule body to goals and use function solve() to see whether goals can all be solved by this rule:
                                - If can solve: return True
                                - If cannt solve: drop this rule body from goals and search for next match rule
                   - If no match: return false

2. Depth- first:
 - declare the goals as a first--in--last--out stack.
 
3. Backtracking:
 - Every time return False, it will backtrack to the corresponding current goal. 
 - Then drop the wrong goals, and try next rule with the help of FILO stack : goals.

Output:
The output is the process of solving the query entered and outcome
  - Such as: current goal is a
             To solve a need solve b
             To solve a need solve c
        - If we have several rules to solve b, for example 3 rules and the first two rules cannot solve then:
             - Such as: c => b
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
   -At the end of output, there will show True of all atom needed to prove query with the opposite order of backward chaining if query is True. Or it will show False if query is False.

Notice:
solve q => p , p => q
- The algorithm will stuck in infinite loop, so we can apply limited--depth to avoid this situation.
         - The limited--depth can be set at least the number of rules in rule file
