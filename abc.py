string = " - effect:particlering{particle=flame;radius=%d;points=%x;amount=%x} @origin\n - delay 1"
ind = 0
news = ""
for i in range(40):
    ind += 0.25
    news += string.replace("%d",str(ind)).replace("%x",str(int(ind*7+5)))
    news += "\n"
with open("sus.txt",'w',encoding="utf-8") as f:
    f.write(news)
