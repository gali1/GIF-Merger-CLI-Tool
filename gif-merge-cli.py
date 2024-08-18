import os
from PIL import Image
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def get_user_input():
    print("Welcome to the GIF Merger CLI Tool")

    files = []
    while True:
        file_path = input("Enter path to GIF file (or 'done' to finish): ").strip()
        if file_path.lower() == 'done':
            break

        if os.path.isfile(file_path) and file_path.lower().endswith('.gif'):
            files.append(file_path)
        else:
            print("Invalid file path or not a GIF file. Please ensure the file exists and is a GIF.")

    if len(files) < 2:
        raise ValueError("You need at least two GIF files to merge.")

    output_path = input("Enter path for the output merged GIF file (e.g., 'output.gif'): ").strip()
    if not output_path.lower().endswith('.gif'):
        output_path += '.gif'

    orientation = input("Enter orientation ('horizontal' or 'vertical'): ").strip().lower()
    if orientation not in ['horizontal', 'vertical']:
        raise ValueError("Invalid orientation. Choose 'horizontal' or 'vertical'.")

    return files, output_path, orientation

def extract_frames(file):
    with Image.open(file) as img:
        frames = []
        durations = []
        try:
            while True:
                frames.append(img.copy())
                durations.append(img.info.get('duration', 100))  # Default duration if not present
                img.seek(img.tell() + 1)
        except EOFError:
            pass
    return frames, durations

def merge_gifs(files, output_path, orientation):
    gif_data = []
    
    # Extract frames and durations in parallel
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(extract_frames, file) for file in files]
        for future in tqdm(futures, desc="Processing GIFs"):
            gif_data.append(future.result())

    frames_list = []
    max_frames = max(len(frames) for frames, _ in gif_data)
    
    frame_widths = [frames[0].width for frames, _ in gif_data]
    frame_heights = [frames[0].height for frames, _ in gif_data]
    
    if orientation == 'horizontal':
        total_width = sum(frame_widths)
        max_height = max(frame_heights)
        new_gif = Image.new('RGBA', (total_width, max_height))
    else:
        max_width = max(frame_widths)
        total_height = sum(frame_heights)
        new_gif = Image.new('RGBA', (max_width, total_height))
    
    last_valid_frames = [None] * len(gif_data)
    last_valid_index = [0] * len(gif_data)
    
    for frame_index in range(max_frames):
        if orientation == 'horizontal':
            new_frame = Image.new('RGBA', (total_width, max_height))
            x_offset = 0
            for gif_index, (frames, _) in enumerate(gif_data):
                if frame_index < len(frames):
                    new_frame.paste(frames[frame_index], (x_offset, 0))
                    last_valid_frames[gif_index] = frames[frame_index]
                    last_valid_index[gif_index] = frame_index
                else:
                    if last_valid_frames[gif_index] is not None:
                        new_frame.paste(last_valid_frames[gif_index], (x_offset, 0))
                    else:
                        new_frame.paste(Image.new('RGBA', (frame_widths[gif_index], max_height)), (x_offset, 0))
                x_offset += frame_widths[gif_index]
            frames_list.append(new_frame)
        else:
            new_frame = Image.new('RGBA', (max_width, total_height))
            y_offset = 0
            for gif_index, (frames, _) in enumerate(gif_data):
                if frame_index < len(frames):
                    new_frame.paste(frames[frame_index], (0, y_offset))
                    last_valid_frames[gif_index] = frames[frame_index]
                    last_valid_index[gif_index] = frame_index
                else:
                    if last_valid_frames[gif_index] is not None:
                        new_frame.paste(last_valid_frames[gif_index], (0, y_offset))
                    else:
                        new_frame.paste(Image.new('RGBA', (max_width, frame_heights[gif_index])), (0, y_offset))
                y_offset += frame_heights[gif_index]
            frames_list.append(new_frame)
    
    frame_durations_combined = []
    for frame_index in range(max_frames):
        duration = max(
            gif_data[gif_index][1][frame_index] if frame_index < len(gif_data[gif_index][1]) else gif_data[gif_index][1][-1]
            for gif_index in range(len(gif_data))
        )
        frame_durations_combined.append(duration)
    
    try:
        new_gif.save(output_path, save_all=True, append_images=frames_list[1:], loop=0, duration=frame_durations_combined)
        print(f"GIF merged and saved to {output_path}")
    except Exception as e:
        print(f"Failed to save GIF: {e}")

if __name__ == "__main__":
    try:
        files, output_path, orientation = get_user_input()
        merge_gifs(files, output_path, orientation)
    except Exception as e:
        print(f"Error: {e}")
