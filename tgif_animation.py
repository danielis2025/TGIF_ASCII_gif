import time
import os
from PIL import Image, ImageDraw, ImageFont

# ASCII Art frames for each letter
frames = [
    r"""
 _______
|__   __|
   | |   
   | |   
   |_|   
    """,
    r"""
  _____ 
 / ____|
| |  __ 
| | |_ |
| |__| |
 \_____| 
    """,
    r"""
 _____ 
|_   _|
  | |  
  | |  
 _| |_ 
|_____| 
    """,
    r"""
 ______ 
|  ____|
| |__   
|  __|  
| |     
|_|     
    """,
    r"""
🎉 Thank God It's Friday! 🎉
🎉 Thank God It's Friday! 🎉
🎉 Thank God It's Friday! 🎉
🎉 Thank God It's Friday! 🎉
    """
]

# Display animation in terminal
for frame in frames:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame)
    time.sleep(1)

# Create GIF frames
image_frames = []
font = ImageFont.load_default()
width, height = 150, 150

for frame in frames:
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), frame.strip(), font=font, fill='black')
    image_frames.append(img)

# Save as GIF
gif_path = "tgif_animation.gif"
image_frames[0].save(
    gif_path,
    save_all=True,
    append_images=image_frames[1:],
    duration=1000,
    loop=0
)

print(f"GIF animation saved as {gif_path}")

