def arithmetic_arranger(problems, show=False):

    arranged_problems = ''
    if len(problems) > 5 :
      return "Error: Too many problems."

    operators = []
    operand_1 = []
    operand_2 = []
    int_operand1 = []
    int_operand2 = []
    for problem in problems:
      args = problem.split()
      operators.append(args[1])
      operand_1.append(args[0])
      operand_2.append(args[2])

    for operator in operators:
      if operator != "+" and operator != "-":
        return "Error: Operator must be '+' or '-'."

    for i in range(len(problems)):
      try:
        int_operand1.append(int(operand_1[i]))
        int_operand2.append(int(operand_2[i]))
      except:
        return "Error: Numbers must only contain digits."
  
    for i in range(len(problems)):
      if int_operand1[i] >= 10000 or int_operand2[i] >= 10000:
        return "Error: Numbers cannot be more than four digits."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(len(problems)):
      width = max( len(operand_1[i]), len(operand_2[i]) )
      # first line
      for op1 in range( (width+2) - len(operand_1[i]) ):
        line1 = line1 + ' '
      line1 = line1 + operand_1[i] + '    '
      # second line
      line2 = line2 + operators[i]
      for op2 in range( (width+1) - len(operand_2[i]) ):
        line2 = line2 + ' '
      line2 = line2 + operand_2[i] + '    '
      # third line
      for dash in range(width+2):
        line3 = line3 + '-'
      line3 = line3 + '    '
      # fourth line
      if operators[i] == '+':
        result = int_operand1[i] + int_operand2[i]
      else:
        result = int_operand1[i] - int_operand2[i]

      for res in range( (width+2) - len(str(result))):
        line4 = line4 + ' '
      line4 = line4 + str(result) +'    '
    
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    
    if show == True:
      arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 
    else:
      arranged_problems = line1 + "\n" + line2 + "\n" + line3
      
    return arranged_problems