import subprocess

file = open("C:/Users/Administrator/Desktop/test_example.txt")
line = file.readline()
i = 1
while line:
    list = line.split(' ',5)
    command = "C:\\Users\Administrator\Desktop\FeeCost_cmd "+list[0]+" "+list[1]+" "+list[2]+" "+list[3]
    p = subprocess.Popen(command,stdout=subprocess.PIPE)
    actualValue = p.stdout.readline().strip()
    actualValue = round(float(actualValue),1)
    expectValue = round(float(list[4]),1)

    if i == 1:
       print("测试编号  主叫区号 被叫区号 通话开始时间    通话时长 预期输出 实际输出 测试结论")
    if expectValue == actualValue:
        print("test", i, ": ", list[0], "    ", list[1], "    ", list[2], "   ", list[3], "  ", expectValue, "   ",
              actualValue, "   Passed")
    else:
        print("test", i, ": ", list[0], "    ", list[1], "    ", list[2], "   ", list[3], "  ", expectValue, "   ",
              actualValue, "   Failed")

    line = file.readline()
    i += 1
file.close()