music={
    "beliver":"https://youtu.be/W0DM5lcj6mw?si=epb6zqnkDeorqGow",
    "enemy":"https://youtu.be/hHB1Ikzfpmc?si=Np0xWkHnb9SEn9MW",
    "liberation":"https://youtu.be/gUQG8CL2rfY?si=REflkBNCApw26zty",
    "overtaken":"https://youtu.be/bfW6dzCFy2A?si=mRsFFavmjfQocwrI",
    "dilbar":"https://youtu.be/TRa9IMvccjg?si=rxS3u2c4ju74UYPS",
    "Gali":"https://youtu.be/1BVgpX4w0Wk?si=5VXlxWJc3RjIywC2",
    "swag":"https://youtu.be/7TRFf7uUfhQ?si=Oaeejy9NOrMdGC6e",
    "breakup":"https://youtu.be/kd5KqlmcHNo?si=XiE9nRdql9IK_upW",
}
if __name__=="__main__":
  c="play overtaken"
  song=c.lower().split(" ")[1]
  print(song)
  link=music(song)