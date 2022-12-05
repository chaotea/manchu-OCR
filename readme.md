# Manchu OCR

[words.csv](data/words.csv) contains a list of Manchu words scraped from Wiktionary.

[wiki.txt](data/wiki.txt) is the full dump of `Wp/mcn`, the incomplete Manchu Wikipedia.

To run the script to generate images, use:
```
python3 generate_images.py
```

For zipping the folder of images, use:
```
cd images
zip -r images_full.zip images_full
```