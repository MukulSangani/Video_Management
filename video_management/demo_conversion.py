import moviepy.editor as mp
import os

def convert_video_to_mp4(video_file_path):
    
    # Check if the input file has a valid extension
    if not video_file_path.lower().endswith(('.mov', '.avi', '.mkv')):
        raise ValueError("The input file must be a .mov, .avi, or .mkv file.")

    # Create output file path with .mp4 extension
    output_file_path = video_file_path.rsplit('.', 1)[0] + '_converted.mp4'

    try:
        # Load the video file
        video = mp.VideoFileClip(video_file_path)

        # Write the converted video to a new file
        video.write_videofile(output_file_path, codec='libx264')

        print(f"Video converted successfully: {output_file_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the video file to free resources
        video.close()

# Example usage
convert_video_to_mp4('C:/Users/admin/Downloads/file_example_MOV_480_700kB.mov')
