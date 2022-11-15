from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


# Font names
fonts = [
    "XM_BiaoHei.ttf",
    "XM_GuFeng.ttf",
    "XM_LiuYe.ttf",
    "XM_ShuKai.ttf",
    "XM_WenJian.ttf",
    "XM_WenQin.ttf",
    "XM_XingShu.ttf",
    "XM_YaBai.ttf",
    "XM_YingBi.ttf",
    "XM_ZhengBai.ttf",
    "XM_ZhengHei.ttf"
]


# Read words from file
words = []
with open("wiktionary/words.csv", "r") as f:
  for i, line in enumerate(f):
    word = line.split()[1]
    words.append(word)


# Generate index
with open("images/index.csv", "w") as f:
    for i, word in enumerate(words):
        f.write(f"{i}, {word}\n")


# Generate images
width = 512
height = 128

for font_num, font_name in enumerate(fonts):

    font_path = "font/" + font_name
    font = ImageFont.truetype(font_path, size=100)

    for i, word in enumerate(words):

        img = Image.new("RGB", (width, height), color="white")

        imgDraw = ImageDraw.Draw(img)

        textWidth, textHeight = imgDraw.textsize(word, font=font)
        xText = (width - textWidth) / 2  # Ignore for now
        yText = (height - textHeight) / 2

        imgDraw.text((10, yText), word, font=font, fill=(0, 0, 0))
        
        output_path = Path(f"images/{i}/word{font_num+1:02d}.png")
        output_path.parent.mkdir(exist_ok=True, parents=True)
        img.save(output_path)