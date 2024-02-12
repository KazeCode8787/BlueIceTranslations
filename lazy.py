import sys
def read(file):
    with open(file,'r',encoding="utf-8") as f:
        for line in f:
            yield line.strip()

if len(sys.argv)>1:
    datas = read(sys.argv[-1])
    def input(s=None):
        return next(datas)

name = input()
i = int(input("i="))
data = ""

while True:
    cmd = input()
    match cmd:
        case "next":
            name = input()
            i = 0
            continue
        case "stop":
            break

    # if cmd == "stop":
    #     break
    # if cmd == "next":
    #     continue

    x,y,z = cmd.split()

    a = f'''{name}{i}:
  SpawnerGroup: halloween23
  MobName: {name}
  World: world5
  X: {x}
  Y: {y}
  Z: {z}
  Yaw: 0.0
  Pitch: 0.0
  Radius: 0
  RadiusY: 1
  UseTimer: true
  MaxMobs: '1'
  MobLevel: '1'
  MobsPerSpawn: 1
  Cooldown: 5
  CooldownTimer: 0
  Warmup: 5
  WarmupTimer: 0
  CheckForPlayers: true
  ActivationRange: 40
  ScalingRange: 25.0
  LeashRange: 32
  HealOnLeash: false
  ResetThreatOnLeash: false
  ShowFlames: false
  Breakable: false
  Conditions: []
  ActiveMobs: 1\n'''
    data += a
    i += 1
    
with open("temp.txt","w",encoding="utf-8") as f:
    f.write(data)
