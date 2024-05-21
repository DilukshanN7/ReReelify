import os
import cv2
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, TextClip, ColorClip
import pytesseract
from hugchat import hugchat
from hugchat.login import Login

# HuggingFace Credentials
EMAIL = "##########@gmail.com" 
PASSWD = "###########"

cookies_folder = 'cookies'
file_path = os.path.join(cookies_folder, EMAIL + '.json')

if os.path.exists(file_path):
    print("Authentication with HuggingChat is Successful")
else:
    cookie_path_dir = "./cookies/"
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

def find_crop_bounds(frame):
    """Find the cropping bounds to remove black bars."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None
    
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    return y, y + h, x, x + w

def crop_video(input_path):
    clip = VideoFileClip(input_path)
    
    frame = clip.get_frame(0)
    crop_bounds = find_crop_bounds(frame)
    
    if crop_bounds:
        top, bottom, left, right = crop_bounds
        cropped_clip = clip.crop(y1=top, y2=bottom, x1=left, x2=right)
        return cropped_clip
    else:
        print(f"No cropping needed for {input_path}")
        return clip

def extract_text_from_frame(frame):
    """Extract text from a video frame using OCR."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    lines = text.split('\n')
    desired_text = "\n".join(lines[2:])
    return desired_text

def get_text_variation(original_text):
    chatbot = hugchat.ChatBot(cookie_path="dilukshann7@gmail.com.json")
    response = chatbot.chat(f"Provide a formal VERY SLIGHT variation of the following text (only give me the response don't say anything, and dont include any usernames (like BROOD, MUZZ) in the variation even if that's in the text, also avoid if there's any random word in that, only take the part where it looks like a complete sentence): {original_text}")
    print(response)
    ask = input("Is this Caption okay with you or Do you need to change it? if then type it here or just press enter: ")
    if ask == "":
        return response
    else:
        return ask

def create_9_16_video_with_logo_and_text(input_path, output_path, logo_path, logo_scale=0.2, text_padding=20, element_padding=10):
    cropped_clip = crop_video(input_path)
    if not cropped_clip:
        return
    
    original_clip = VideoFileClip(input_path)
    frame = original_clip.get_frame(0)
    original_text = extract_text_from_frame(frame)
    
    if original_text:
        text = str(get_text_variation(original_text))
    else:
        text = "Sample Text for the Video"
    
    original_width, original_height = cropped_clip.size
    
    target_width = original_width
    target_height = int(target_width * 16 / 9)
    
    if original_height > target_height:
        target_height = original_height
        target_width = int(target_height * 9 / 16)
    
    logo = ImageClip(logo_path)
    
    logo_width = original_width * logo_scale
    logo = logo.resize(width=logo_width)
    
    logo = logo.set_duration(cropped_clip.duration)
    
    text_clip = TextClip(text, fontsize=45, color='white', bg_color='black', font="poppins", method='caption', size=(target_width - 2 * text_padding, None))
    text_clip = text_clip.set_duration(cropped_clip.duration)
    
    total_height = logo.size[1] + text_clip.size[1] + original_height + 2 * element_padding 
    
    start_y = (target_height - total_height) / 2
    
    logo_y_pos = start_y
    text_y_pos = logo_y_pos + logo.size[1] + element_padding 
    video_y_pos = text_y_pos + text_clip.size[1] + element_padding 

    x_center = (target_width - original_width) / 2
    logo_x_pos = (target_width - logo.size[0]) / 2
    text_x_pos = text_padding
    
    background = ColorClip(size=(target_width, target_height), color=(0, 0, 0), duration=cropped_clip.duration)
    
    final_clip = CompositeVideoClip([
        background,
        cropped_clip.set_position((x_center, video_y_pos)),
        logo.set_position((logo_x_pos, logo_y_pos)),
        text_clip.set_position((text_x_pos, text_y_pos))
    ], size=(target_width, target_height))
    
    frame_rate = final_clip.fps
    duration_last_10_frames = 10 / frame_rate
    new_duration = final_clip.duration - duration_last_10_frames
    trimmed_clip = final_clip.subclip(0, new_duration)
    trimmed_clip.write_videofile(output_path, codec='libx264')


def process_folder(input_folder, output_folder, logo_path, logo_scale=0.2, text_padding=20, element_padding=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            print(f"Processing {input_path}")
            
            create_9_16_video_with_logo_and_text(input_path, output_path, logo_path, logo_scale, text_padding, element_padding)
            print(f"Saved 9:16 video to {output_path}")

# Parameters
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Update this path as necessary
input_folder = 'folder'
output_folder = 'folder2'
logo_path = '1.png'  # Path to your logo image
logo_scale = 0.75  # Adjust the scale to make the logo larger (e.g., 0.4 for 40% of the video width)
text_padding = 20  # Adjust the padding as needed
element_padding = 30  # Padding between the logo, text, and video

process_folder(input_folder, output_folder, logo_path, logo_scale, text_padding, element_padding)
