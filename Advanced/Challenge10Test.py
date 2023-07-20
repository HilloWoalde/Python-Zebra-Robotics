from pyamaze import maze, agent

m=maze(20,20)

m.CreateMaze(loopPercent=50)

a=agent(m,filled=True,footprints=False)

m.enableArrowKey(a)

m.run()