from pyamaze import maze, agent, COLOR

m=maze(20,20)

m.CreateMaze(loopPercent=50)

a=agent(m,filled=True,footprints=True, color=COLOR.red)

b=agent(m,filled=True,footprints=False)

m.tracePath({a:m.path}, kill=True, delay=52)

m.enableWASD(b)
m.enableArrowKey(b)

m.run()