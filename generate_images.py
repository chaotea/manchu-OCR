import arabic_reshaper
import pandas as pd
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
words_df = pd.read_csv("data/words.csv", names=["romanization", "manchu"])

# Generate images
width = 224
height = 224
padding = 10
base_img = Image.new("RGB", (width, height), color="white")
base_draw = ImageDraw.Draw(base_img)

for i in range(len(words_df)):
    if (i + 1) % 100 == 0:
        print(f"Generated {i+1} words...")

    romanization, word = words_df.iloc[i]

    for font_num, font_name in enumerate(fonts):
        font = ImageFont.truetype(f"font/{font_name}", size=100)

        # Thanks to Jack for suggesting to use arabic
        reshaped = arabic_reshaper.reshape(word)

        left, top, right, bottom = base_draw.textbbox((0, 0), reshaped, font=font, anchor="lt", language="ar-SA")
        text_width = right - left
        text_height = bottom - top

        img = Image.new("RGB", (text_width + 2 * padding, height), color="white")
        img_draw = ImageDraw.Draw(img)
        img_draw.text((padding, height / 2), reshaped, fill=(0, 0, 0), font=font, anchor="lm", language="ar-SA")
        
        output_path = Path(f"images/images_full/{i}/{romanization}_{font_name[:-4]}.png")
        output_path.parent.mkdir(exist_ok=True, parents=True)

        img.save(output_path)